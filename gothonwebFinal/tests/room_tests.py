from nose.tools import *
from gothonweb.maps import *
from bin.app import GameEngine

def test_room():
	coliseum = Room("Coliseum",
					"""This is the main room, here you choose to
					say yes or no.""")
	assert_equal(coliseum.name, "Coliseum")
	asser_equal(coliseum.paths, {})
	
def test_room_paths():
	yes = Room("Yes", "Move on.")
	no = Room("No", "Death.")
