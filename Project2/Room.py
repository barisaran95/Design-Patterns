from Ant import *

class Room:
    	def __init__(self):
        	pass

class ForagerRoom(Room):

    	def __init__(self):
        	Room.__init__(self)	
        	pass

    	def createAnt(self,team,turn,cell):
        	return ForagerAnt(team,turn,cell)

class WarriorRoom(Room):
    	def __init__(self):
        	Room.__init__(self)       	
		pass

    	def createAnt(self,team,turn,cell):
        	return WarriorAnt(team,turn,cell)


class WorkerRoom(Room):
    	def __init__(self):
        	Room.__init__(self)
        	pass

    	def createAnt(self,team,turn,cell):
        	return WorkerAnt(team,turn,cell)
