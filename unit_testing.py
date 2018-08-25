import unittest 
from unittest import TestCase
from unittest.mock import MagicMock
from main import generateItem, thing

class testing(TestCase): 
	def swordID(self): #this test will see if the game breaks when given a sword ID of 8 ((it should just decide the object is trash and not increase ID))
		swordid = 8 #could also change to len(swords)-1
		thing = generateItem()
		generateItem.method = MagicMock(return_value=-1)
		self.assertEqual(thing, -89, "passed") 
		
	def shielfID(self):
		shieldid = 9 #could also change to len(sheilds)-1
		thing = generateItem()
		generateItem.method = MagicMock(return_value = -2
		self.assertEqual(thing, -89, "passed") 
	
	def canYouMove(self): #this tests to see if you can move if the tile next to you is #
	
	def whereAreYouGoing(self): #this tests to see if the world is updated when you step on "!"
	
	def isItHere(self): #this room asserts not equal "!" room to room 1
		
		
#if __name__ == '__main__':