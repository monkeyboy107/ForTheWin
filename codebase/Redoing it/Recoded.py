#!/usr/bin/env python3
##########################################################################################
#Programmer: Isaac Kerley
#Date: 10/22/2015 -
#Purpose:This is For The Win
##########################################################################################
#Imports
import random
import Items
import character
#classes
class character:
	health = 100
	isPlayable = False
	inv = []
	def __init__(self, name):
		self.name = name
	def equip(self, item):
		self.held = item
	def unequip(self)
		self.equip(None)
	def attack(self, enemy):
		if self.held == None:
			print("You are not currently holding any items")
		elif self.held.is_weapon == False:
			print("You lack any weapon of any sort")
		else:
			enemy.health -= weapon.damage
	def heal(self, person):
		if held.can_heal == None:
			print("You are not currently holding any items... I dont like that fact I hurt you")
			self.health -= 1
		elif self.held.aid == False:
			print("The item you are holding is not a weapon")
		else:
			self.health += aid.heal
##Items
class item:
	can_heal = False
	is_weapon = False
class weapon(item):
	is_weapon = True
class aid(item):
	can_heal = True
class sword(weapon):
	weapon.damage = 10
class club(weapon):
	weapon.damage = 5
class knife(weapon):
	weapon.damage = 3
class lightSword(weapon):
	weapon.damage = 25
class potion(aid):
	aid.heal = 25
class apple(aid):
	aid.heal = 5
##Characters
class player(character):
	isPlayable = True
class enemy(character):
	inv = [sword]
    self.equip(sword)
#Functions
'''
def ResetVar():
def PlaceCheck():
	while PlacesNum
'''
#Arrays
'''
inv = [0]
RanMineItem = ['Coal','Coal','Dirt','Dirt','Dirt','Rock','Rock','Rock']
Creatures = ['Weak Creature','Weak Creature','Weak Creature','Weak Creature','Weak Creature','Weak Creature','Regular Creature','Regular Creature','Regular Creature','Regular Creature','Regular Creature','Regular Creature','Regular Creature','Hard Creature','Rare Creature']
People = ['Villigar','Villigar','Villigar','Villigar','Villigar','Rich Kid','Rich Kid','Rich Kid','Rich Kid','Poor Fighter','Poor Fighter','Poor Fighter','Poor Fighter','Poor Fighter','Poor Fighter','Poor Fighter','Poor Fighter','Poor Fighter','Poor Fighter','Poor Fighter','Good Fighter','Good Fighter','Nearly Invincible Enemy']
BattleFieldEnemy = [Creatures[ranCreature],Creatures[ranCreature],Creatures[ranCreature],People[ranPeople]]
'''
StoreItems = ['Sword','Bow','25 Arrows']
#Varibles
'Note to self I need to seriously clean up the varibles I use'
playerName = 0
ranNum = random.randrange(5)
playerAge = 0
ranPlayerAge = random.randrange(100) + 1
HP = 100
maxHP = 100
SP = 25
maxSP = 25
dayCount = 0
errorCheck = 0
placesTwo = 0
arrayNum = 0
area = 0
fakeplayerName = 0
playerStr = str(playerName)
going = 0
playerChoice = 0
currency = 0
ranPlayerAge = int(ranPlayerAge)
ranCreature = random.randrange(len(Creatures))
ranPeople = random.randrange(len(People))
##########################################################################################
#Main Code
##Player Setup
while errorCheck != 1:
	playerName = input("What is your name? ")
	try:
		str(playerName)
		errorCheck = errorCheck	+ 1
	except:
		input("Im sorry but that is not an accepted name ")
while errorCheck != 2:
	playerAge = input("What is your age? ")
	try:
		int(playerAge)
		playerAge = int(playerAge)
		errorCheck = errorCheck + 1
	except:
		input("That is not a number. ")
if playerAge == ranPlayerAge:
	input("I knew your age was that! ")
elif playerAge < ranPlayerAge:
	input("I thought you where much younger... infact I thought you where " + str(ranPlayerAge) + " years old. My bad. ")
elif playerAge > str(ranPlayerAge):
	input("I thought you where much older... infact I thought you where " + str(ranPlayerAge) + " years old. My bad. ")
##Player Startup
input("Stranger: Oh no! ")
input(str(playerName) + ": Ah my hea- ")
input("(Loud thud)")
input("Stranger: Oh no! ")
if area == 0:
		input("You wake up in a house, in a warm bed. The smell of food reaches your nose. ")
		input("Stranger: Ah good you are awake ")
		input(str(playerName) + ": Yes I am. Who are you exactly ")
		input("John: My name is John. Might you tell me what yours is? ")
		PlayerFakenName = (playerStr + ": My name is ")
##Places
while area == 1:
	going = input("Where would you like to go? (1 is John's House, 2 is a battlefield, 3 is a mineshaft, 4 is a shop) ") - 1
	if going == 0:
		playerChoice = input("What would you like to do? (1 is where you sleep, 2 is where you talk to John, 3 is where you leave) ")
		if playerChoice == 1:
			HP = int(maxHP)
			SP = int(maxSP)
		if playerChoice == 2:
			input("You talk to John")
	if going == 1:
		PlayersChoice = input("You arive at a battlefield. Where would you like to go? ")
	if going == 2:
		PlayersChoice = input("You arrive at a mineshaft. What would you like to do? ")
		
	if going == 3:
		input("You enter a shop. You see a shop keeper. ")
		PlayersChoice = input("Shop Keeper: What'll you be having? (item 1 item 2 item 3) ")
		input("I'll like to have " + str(playerChoice))
	if going == 4:
		playerChoice("Are you sure you want to exit? (Y is Yes and n is No) ")
		if playerChoice == Y:
			exit()
		if playerChoice == n:
			input("Okay")
		#if playerChoice #This checks for if it is one of the choices
	if going <= 5:
		input("Im sorry but that is not one of the choices. Please select another one ") #The point of this is to prevent the player from accidently doing a invalid number
	area = 1