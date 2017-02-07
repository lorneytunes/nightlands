"""
Characters

Characters are (by default) Objects setup to be puppeted by Players.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.

"""
from evennia import DefaultCharacter

class Character(DefaultCharacter):
    def at_object_creation(self):
        self.db.strength = 2
        self.db.dexterity = 2
        self.db.constitution = 2
        self.db.wisdom = 2
        self.db.charisma = 2
        self.db.intelligence = 2
        self.db.freepoints = 8
    
    #Getters and setters
    def get_abilities(self):
        return self.db.strength, self.db.dexterity, self.db.constitution, self.db.wisdom, self.db.charisma, self.db.intelligence
    def get_freepoints(self):
        return self.db.freepoints
    pass