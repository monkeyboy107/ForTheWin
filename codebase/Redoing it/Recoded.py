#!/usr/bin/env python3
##########################################################################################
#Programmer: Isaac Kerley
#Date: 10/22/2015
#Purpose:This is For The Win
##########################################################################################
#Imports
import random
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
class item:
	can_heal = False
	is_weapon = False
class weapon(item):
	is_weapon = True
class aid(item):
	can_heal = True
class player(character):
	isPlayable = True
class enemy(character):
	inv = [sword]
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
BattleFieldEnemy = [Creatures[RanCreature],Creatures[RanCreature],Creatures[RanCreature],People[RanPeople]]
'''
StoreItems = ['Sword','Bow','25 Arrows']
#Varibles
'Note to self I need to seriously clean up the varibles I use'
PlayerName = 0
RandomNum = random.randrange(5)
PlayerAge = 0
RanPlayerAge = random.randrange(100) + 1
HP = 100
MaxHP = 100
SP = 25
MaxSP = 25
RandomNum = random.randrange(5)
DayCount = 0
ErrorCheck = 0
PlacesTwo = 0
ArrayNum = 0
Areas = 0
FakePlayerName = 0
PlayerStr = str(PlayerName)
Going = 0
PlayerChoice = 0
Currency = 0
RanPlayerAge = int(RanPlayerAge)
RanCreature = random.randrange(len(Creatures))
RanPeople = random.randrange(len(People))
##########################################################################################
#Main Code
##Player Setup
while ErrorCheck != 1:
	PlayerName = input("What is your name? ")
	try:
		str(PlayerName)
		ErrorCheck = ErrorCheck	+ 1
	except:
		input("Im sorry but that is not an accepted name ")
while ErrorCheck != 2:
	PlayerAge = input("What is your age? ")
	try:
		int(PlayerAge)
		PlayerAge = int(PlayerAge)
		ErrorCheck = ErrorCheck + 1
	except:
		input("That is not a number. ")
if PlayerAge == RanPlayerAge:
	input("I knew your age was that! ")
elif PlayerAge < RanPlayerAge:
	input("I thought you where much younger... infact I thought you where " + str(RanPlayerAge) + " years old. My bad. ")
elif PlayerAge > str(RanPlayerAge):
	input("I thought you where much older... infact I thought you where " + str(RanPlayerAge) + " years old. My bad. ")
##Player Startup
input("Stranger: Oh no! ")
input(str(PlayerName) + ": Ah my hea- ")
input("(Loud thud)")
input("Stranger: Oh no! ")
if Areas == 0:
		input("You wake up in a house, in a warm bed. The smell of food reaches your nose. ")
		input("Stranger: Ah good you are awake ")
		input(str(PlayerName) + ": Yes I am. Who are you exactly ")
		input("John: My name is John. Might you tell me what yours is? ")
		PlayerFakenName = (PlayerStr + ": My name is ")
##Places
while Areas == 1:
	Going = input("Where would you like to go? (1 is John's House, 2 is a battlefield, 3 is a mineshaft, 4 is a shop) ") - 1
	if Going == 0:
		PlayerChoice = input("What would you like to do? (1 is where you sleep, 2 is where you talk to John, 3 is where you leave) ")
		if PlayerChoice == 1:
			HP = int(MaxHP)
			SP = int(MaxSP)
		if PlayerChoice == 2:
			input("You talk to John")
	if Going == 1:
		PlayersChoice = input("You arive at a battlefield. Where would you like to go? ")
	if Going == 2:
		PlayersChoice = input("You arrive at a mineshaft. What would you like to do? ")
		
	if Going == 3:
		input("You enter a shop. You see a shop keeper. ")
		PlayersChoice = input("Shop Keeper: What'll you be having? (item 1 item 2 item 3) ")
		input("I'll like to have " + str(PlayerChoice))
	if Going == 4:
		PlayerChoice("Are you sure you want to exit? (Y is Yes and n is No) ")
		if PlayerChoice == Y:
			exit()
		if PlayerChoice == n:
			input("Okay")
		#if PlayerChoice #This checks for if it is one of the choices
	if Going <= 5:
		input("Im sorry but that is not one of the choices. Please select another one ") #The point of this is to prevent the player from accidently doing a invalid number
	Areas = 1