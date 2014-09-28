#!/usr/bin/py
##
##    This file contains the class(es) pertaining
##  to characters.
##
##    Classes: 
##  Character


class Character:

	## Attributes
	name = None
	health = 100
	items = {}

	##-Methods-##

	## This method executes when the class is loaded
	def __init__(self):
		pass

	def say(self,words):
		test = "\t[%s]: %s"%(self.name,words)