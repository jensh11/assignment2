# @author Jens Hartmark - October 2013

# imports the exit and randint functions from lib
from sys import exit
from random import randint

class Scene(object):

	def enter(self):
		print "This scene is not yet configured. Subclass it and implement enter()."
		exit(1)

# the engine class starts the game and selects scene maps		
class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map
		
	def play(self):
		current_scene = self.scene_map.opening_scene()
		
		while True:
			print "\n*************"
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)
			
			
class Impossible(Scene):

	def enter(self):
		print "In order to resurrect you must guess the magic word."
		print "A voice inside you tells you a riddle."
		print "What is creeping up, so near you can feel it, yet you try to get away from it."
		code = "death"
		quess = raw_input("[keypad]> ")
		guesses = 1
		
		while guess != code and guesses < 10:
			print "WRONG!"
			guesses += 1
			quess = raw_input("[keypad]> ")
			
			if guess == code:
				print "A white spirit appears in the air."
				print "Your body turns from cold to hot."
				print "You feel your strength coming back once again."
				return 'luhos'
				
			else:
				print "You fade away."
				print "There is no turning back now."
				print "Only death..."
				return 'death'


# the death scene returns prints for when you die and exits the game			
class Death(Scene):
	
	quips = [
		"You trip and fall, and your enemy chops your head off.",
		"It appears you are not as deadly as you thought. RIP.",
		"What a bloodbath. You get shred to pieces.",
		"You are no match for your nemesis. Blood gushing out. RIP.",
		"You are exhausted and fall on you sword, piercing your own heart",
		"Weak and pathetic. Your soul leaves your body."
	]
	
	def enter(self):
		print Death.quips[randint(0, len(self.quips)-1)]
		exit(1)

		
# the starting scene of the game		
class Coliseum(Scene):
	
	def enter(self):
		print "\tYou are the gladiator Spartacon, a Thracian soldier who has been captured and sold into slavery."
		print "Now you are standing in the middle of the Coliseum in ancient Rome awaiting your challenges."
		print "It is packed with people, who have all come to see blood spilled."
		print "In order to regain your freedom, you must defeat five challengers."
		print "The challengers are Eranos, a master swordsman, Khorok a true ranged combatant,"
		print "Lady Serana, a witch who conjures dark powers, Kirgor Back Breaker,"
		print "a monstrous figure with unbelievable powers, and last but not least,"
		print "Luhos, a killer with near-godly powers."
		print "\n"
		print "\tShould you defeat all five challengers, you will be rich beyond your wildest dreams,"
		print "and last but not least, you will regain your freedom."
		print "Should you fail, however, your head will be put on a spike."
		print "\n"
		print "***Are you ready to start the first challenge?***"
		
		# raw_input where the user selects yes or no
		action = raw_input("> ")
		
		# starts an if-sequence, which either returns first challenge or death or error message
		if action == "yes":
			return 'eranos'
		
		# returns death class
		elif action =="no":
			print "Since you refuse to battle, Caesar decides your fate."
			return 'death'
		
		# returns error message and the coliseum class
		else:
			print "DOES NOT COMPUTE!"
			return 'coliseum'
		
class Eranos(Scene):
	
	def enter(self):
		print "The crowd goes wild as the first gate opens."
		print "You hear the rumbling of horses and carriages."
		print "Out of the gates comes Eranos, a master swordsman."
		print "He steps off of his carriage and draws his two swords."
		print "He rushes towards you with both blades raised."
		print "\n"
		print "You raise your axe, but what do you do?"
		
		action = raw_input("> ")
		
		if action == "pierce":
			print "Eranos shatters your axe!"
			print "Without a weapon you are helpless."
			print "Eranos cuts your head off!"
			return 'death'
		
		elif action == "run":
			print "The crowd boos!"
			print "Eranos throws his swords."
			print "The swords pierce your heart and stomach."
			return 'death'
		
		elif action == "throw axe":
			print "Your axe misses."
			print "You are left without a weapon."
			print "Eranos rips your heart out."
			return 'death'
			
		elif action == "slash ancles":
			print "You slash Eranos' ancles."
			print "He is rendered helpless."
			print "You finishes him with a chop to the chest."
			print "The crowd goes wild as you defeat your first challenge!"
			return 'khorok'
		
		else:
			print "DOES NOT COMPUTE!"
			return 'coliseum'
			
		
class Khorok(Scene):
	
	def enter(self):
		print "Khorok enters the stadium."
		print "He does not bat an eye as he treads over Eranos' dead body."
		print "He raises his sword and looks at you."
		print "Khorok is ready to fight."
		print "What do you do?"
		
		action = raw_input("> ")
		
		if action == "Slash":
			print "Your swing with your axe is blocked by Korok's armor."
			print "Khorok smirks as he raises his sword up high."
			print "He swings and off goes your legs."
			print "A quick blow to the chest and it is all over."
			return 'death'
			
		elif action == "Run":
			print "You try to run away."
			print "But Khorok is too fast."
			print "He hunts you down and you hit the ground."
			return 'death'
			
		elif action == "Beg":
			print "You surrender your axe and kneel."
			print "Khorok shows no mercy."
			print "Caesar gives Khorok a look of approval."
			print "A shiny blade is the last thing you see."
			return 'death'
			
		elif action == "Cry":
			print "You cry for help!"
			print "No one hears you over the crowd."
			print "Khorok laughs as he severs your hear."
			return 'death'
			
		elif action == "Charge":
			print "You charge towards Khorok."
			print "Axe raised!"
			print "Khorok tries to block."
			print "You are too fast, and Khorok falls to the ground, bleeding..."
			return 'lady_serana'
			
		else:
			print "DOES NOT COMPUTE!"
			return 'coliseum'
		
				
class LadySerana(Scene):
	
	def enter(self):
		print "Your next challenger is Lady Serana"
		print "She is the most deadly ranger in all of Rome"
		print "Lady Serana enters the stadium."
		print "Her crossbow is loaded."
		print "She aims at you and says 'time to die'"
		print "What is your next move?"
		
		action = raw_input("> ")
			
		if action == "Stealth":
			print "You try to sneak up on Serana."
			print "You are easily spotted."
			print "With one arrow she takes you down."
			return 'death'
				
		elif action == "Throw":
			print "You try to throw your axe at Serana."
			print "With her swift moves she easily dodges it."
			print "One arrow is all it takes."
			print "Everything turns black."
			return 'death'
				
		elif action == "Charge":
			print "You trie to charge with brute force."
			print "Your axe misses."
			print "A dagger to the neck is what you get."
			return 'death'
				
		elif action == "Shout":
			print "Your trembling shout frightens her."
			print "In a moment of weakness you land your axe."
			print "The raw steel runs through her."
			print "Serana lets out a squeel as she falls to the ground."
			return 'kirgor_back_breaker'
				
		else:
			print "DOES NOT COMPUTE!"
			return 'coliseum'
				
		
class KirgorBackBreaker(Scene):
	
	def enter(self):
		print "The ground on which you stand trembles."
		print "Out from the largest gate comes a monster of a man, Kirgor Back Breaker."
		print "His size allows him to dual wield the largest axes you have ever seen."
		print "He lets out a battle cry that makes the hairs on you neck stand up."
		print "Kirgor raises his axes as he walks towards you."
		print "How do you wish to deal with him? Charge, run or outsmart..."
		
		acton = raw_input("> ")
		
		if action == "Charge":
			print "You charge Kirgor"
			print "He flicks you away and splits you in half."
			return 'death'
			
		if action == "Run":
			print "You try to run."
			print "Kirgor throws one of his axes after you."
			print "Its size makes it impossible to dodge."
			print "To the ground you fall."
			return 'death'
			
		if action == "Outsmart":
			print "Kirgor is a half-wit."
			print "All he has to show for is raw strength."
			print "You throw your axe to the ground and start to taunt Kirgor."
			print "He looks at you, baffled."
			print "As he goes to pick up your axe you sneak up behind him."
			print "Multiple quick stabs with your dagger to his back."
			print "The large monstrosity falls to the ground."
			return 'luhos'
			
		else:
			print "DOES NOT COMPUTE!"
			return 'coliseum'
					
		
class Luhos(Scene):

	def enter(self):
		print "Your final challenge awaits you."
		print "The crows goes silent. Fear spreads as Luhos enters the arena."
		print "The most feared warrior in all of ancient Rome."
		print "His armor is made of black steel."
		print "His mace is sharper than diamond."
		print "He looks disappointed when he sees his opponent."
		print "How do you deal with Luhos? Brute force, speed or forfeit?"
		
		action = raw_input("> ")
		
		if action == "Brute force":
			print "You are no match for the mighty Luhos."
			print "A swing of his mace lights you on fire."
			print "Your death is painful."
			return 'death'
			
		if action == "Speed":
			print "You try to run around Luhos to attack from behind."
			print "He is too fast."
			print "His diamond-cut mace smashes you to dust."
			return 'death'
			
		if action == "Forfeit":
			print "You throw your axe on the ground."
			print "Waving hte white flag."
			print "I give up!"
			print "Luhos laughs and splits you in half."
			return 'impossible'
			
		if action == "Summon":
			print "You call upon the spirits of fallen champions."
			print "Ghosts rise from their graves."
			print "They all rush towards Luhos."
			print "You are victorious!"
			return 'victory'
			
			
class Victory(Scene):
	def enter(self):
		print "You have defeated all challengers."
		print "The true gladiator is you."
		print "The crows goes wild, all cheering for you!"
		print "Congratulations!"
		exit(1)
			
class Map(object):

	scenes = {
		'coliseum': Coliseum(),
		'eranos': Eranos(),
		'khorok': Khorok(),
		'lady_serana': LadySerana(),
		'kirgor_back_breaker': KirgorBackBreaker(),
		'luhos': Luhos(),
		'death': Death(),
		'impossible': Impossible()
	}

	def __init__(self, start_scene):
		self.start_scene = start_scene
		
	def next_scene(self, scene_name):
		return Map.scenes.get(scene_name)
		
	def opening_scene(self):
		return self.next_scene(self.start_scene)
		
a_map = Map('coliseum')
a_game = Engine(a_map)
a_game.play()