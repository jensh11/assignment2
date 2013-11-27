from random import randint


class Room(object):
	
	def __init__(self, name, description, pic, number=None, tries=None):		
		self.name = name
		self.description = description
		self.paths = {}
		self.output = ""
		self.pic = pic
		
		
		

	def go(self, direction):
		return self.paths.get(direction, None)

	def add_paths(self, paths):
		self.paths.update(paths)
	
	def options(self):
		if self.name == "Eranos":
			return "No help to be found... Pray.. Unless you type l33t"
		elif self.paths == {}:
			pass
		else:
			return self.paths.keys()
			
	def leet(self):
		hints = {'Eranos': "Eranos is fast.. If he cannot move you won't be hurt.. Perhaps slash his ancles.."
		}
		
		if self.name in hints.keys():
			self.output = hints.get(self.name)
		else:
			self.output = "No hint available."
			
	def _help(self):
		self.output = """You are in %s. Your choices are listed above your input bar. For additional help, you can sometimes type 'l33t' for a hint, although it may not work for every room. Other commands are 'Restart', 'Credits' and 'Quit'. There's also 'Credits'""" % (self.name)

def generate(num1, num2, num3):
	global n1
	n1 = num1
	global n2
	n2 = num2
	global n3
	n3 = num3
	return '%d%d%d' % (n1, n2, n3)
	
coliseum = Room ("Coliseum", 
"""
You are the gladiator Spartacon, a Thracian soldier who has been captured and sold into slavery.
Now you are standing in the middle of the Coliseum in ancient Rome awaiting your challenges.
It is packed with people, who have all come to see blood spilled.
In order to regain your freedom, you must defeat five challengers.
The challengers are Eranos, a master swordsman, Khorok a true ranged combatant,
Lady Serana, a witch who conjures dark powers, Kirgor Back Breaker,
a monstrous figure with unbelievable powers, and last but not least,
Luhos, a killer with near-godly powers.
\n
Should you defeat all five challengers, you will be rich beyond your wildest dreams,
and last but not least, you will regain your freedom.
Should you fail, however, your head will be put on a spike.
\t
***Are you ready to start the first challenge?***
""", "coliseum.gif")

eranos = Room("Eranos",
"""
The crowd goes wild as the first gate opens.
You hear the rumbling of horses and carriages.
Out of the gates comes Eranos, a master swordsman.
He steps off of his carriage and draws his two swords.
He rushes towards you with both blades raised.
\n
You raise your axe, but what do you do?
""", "eranos.gif")

khorok = Room("Khorok",
"""
Khorok enters the stadium.
He does not bat an eye as he treads over Eranos' dead body.
He raises his sword and looks at you.
Khorok is ready to fight.
What do you do?
""", "khorok.gif")

lady_serana = Room("Lady Serana",
"""
Your next challenger is Lady Serana
She is the most deadly ranger in all of Rome
Lady Serana enters the stadium.
Her crossbow is loaded.
She aims at you and says 'time to die'
What is your next move?
""", "lady_serana.gif")

kirgor_back_breaker = Room("Kirgor Back Breaker",
"""
The ground on which you stand trembles.
Out from the largest gate comes a monster of a man, Kirgor Back Breaker.
His size allows him to dual wield the largest axes you have ever seen.
He lets out a battle cry that makes the hairs on you neck stand up.
Kirgor raises his axes as he walks towards you.
How do you wish to deal with him? Charge, run or outsmart...
""", "kirgor_back_breaker.gif")

luhos = Room("Luhos",
"""
Your final challenge awaits you.
The crows goes silent. Fear spreads as Luhos enters the arena.
The most feared warrior in all of ancient Rome.
His armor is made of black steel.
His mace is sharper than diamond.
He looks disappointed when he sees his opponent.
How do you deal with Luhos? Brute force, speed or forfeit?
""", "luhos.gif")

victory = Room("Victory",
"""
You are the true Gladiator of the Coliseum!
The crowd welcomes and cheers for you!
\n
You won!
""", "victory.gif")

loser = Room("The End",
"""
Get out of Rome!
This is no place for you.
""", "death.gif")


generic_death = Room("death", "You died!", "death.gif")

coliseum_death1 = Room("death",
"""
You refuse to fight?! Caesar makes quick work of you,
as he releases lions from their cages.
They rip you apart within seconds...""", "death.gif")

coliseum_death2 = Room("death",
"""
Cowards have no place in Rome!
The archers hit you with their arrows.
You die...
""", "death.gif")

eranos_death = Room("death",
"""
Your swing with your axe is blocked by Eranos' armor.
Khorok smirks as he raises his sword up high.
He swings and off goes your legs.
A quick blow to the chest and it is all over.
""", "death.gif")

khorok_death = Room("death",
"""
You are no match to the migthy Khorok.
He kills you with ease.""", "death.gif")

lady_serana_death = Room("death",
"""
Lady Serana is a much more skilled warrior than you
You die...""", "death.gif")

kirgor_back_breaker_death = Room("death",
"""
You turn to dust at the hands of Kirgor.
Death is inevitable...""", "death.gif")

luhos_death = Room("death",
"""
Luhos is knowns as the true Gladiator of Rome.
The fact that you made it this far proves nothing.
Luhos gets pleasure out of killing you.""", "death.gif")

luhos.add_paths({
	'forfeit': luhos_death,
	'speed': luhos_death,
	'summon': victory
})

kirgor_back_breaker.add_paths({
	'run': kirgor_back_breaker_death,
	'charge': kirgor_back_breaker_death,
	'outsmart': luhos
})

lady_serana.add_paths({
	'cut': lady_serana_death,
	'flee': lady_serana_death,
	'shout': kirgor_back_breaker
})

khorok.add_paths({
	'spit': khorok_death,
	'stab' : khorok_death,
	'charge': lady_serana
})

eranos.add_paths({
	'slash ancles' : khorok,
	'pierce' : eranos_death,
	'run' : eranos_death
})

coliseum.add_paths({
	'no': coliseum_death1,
	'yes': eranos
})


##########################
#  For testing purposes  #
##########################
START = coliseum
SECOND = eranos
THIRD = khorok
FOURTH = lady_serana
FIFTH = kirgor_back_breaker
SIXTH = luhos
END1 = victory
END2 = loser