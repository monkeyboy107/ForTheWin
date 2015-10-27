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