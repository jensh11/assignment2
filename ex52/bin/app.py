import web
import maps

urls = (
	'/game', 'GameEngine',
	'/index', 'Index',
	'/', 'Index',
	'/credits', 'Credits',
	'/quit', 'Quit'
)

app = web.application(urls, globals())
render = web.template.render('templates/', base="layout")



if web.config.get('_session') is None:
	store = web.session.DiskStore('sessions')
	session = web.session.Session(app, store, initializer={'room': None})
	web.config._session = session
else:
	session = web.config._session


class Index(object):

	def GET(self):
		# start the session with starting values then move to engine
		session.room = maps.START
		web.seeother("/game")
		
# displays some info about the game/creator		
class Credits(object):

	def GET(self):
		return render.credits()
# simply quits the game		
class Quit(object):

	def GET(self):
		return render.quit()
	
# the game engine, which runs the different commands for the game and starts it	
class GameEngine(object):

	def __init__(self):
		self.commands = {'help': session.room._help, 'l33t': session.room.leet, 'restart': self.restart, 'quit': self.quit, 'credits': self.credits}
		
	def credits(self):
		session.room.output = "Main Programmer: Jens Hartmark. Go to /credits for more information."
		return render.credits()
	
	def restart(self):
		session.room = maps.START
		web.seeother('/game')

		
	def quit(self):
		session.room.output = "You quit. Go to /quit for more information."
		return render.quit()

	def GET(self):
		if session.room:
			return render.show_room(room=session.room)
		else:
			return render.you_died()

			
	def POST(self):
		form = web.input(action=None)
		
		if form.action and session.room:
			if '*' in session.room.paths:
				if form.action != session.room.num and form.action not in self.commands:
					session.room.guess -= 1
					session.room.output = "..." % session.room.guess
					if session.room.guess == 0:
						session.room = session.room.go('*')
				elif form.action == session.room.num:
					session.room = session.room.go('x')			
			else:
				transition = session.room.go(form.action)
				if transition == None:
					session.room.output = "You cannot do that."
				elif transition != None:
					session.room = transition
				else:
					session.room.output = "Please enter a command."
		
		if form.action in self.commands:
			self.commands[form.action]()
	
		web.seeother('/game')

		
if __name__ == '__main__':
	app.run()