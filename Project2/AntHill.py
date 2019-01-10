from Room import *
import random

class AntHill:
	def __init__(self, room, food, ants, cell, team):
        	self.ants = []
        	self.rooms = []
        	#self.numWorker = 2
		self.warriors=[]
		self.foragers=[]
		self.workers=[]
		self.food=food
		self.team=team
        	for i in range(room):
            		baris = random.randint(1,3)
            		if baris == 1:
                		self.rooms.append(WarriorRoom())
            		elif baris == 2:
                		self.rooms.append(WorkerRoom())
            		else:
                		self.rooms.append(ForagerRoom())

        	for k in range(ants):
            		alp = random.randint(1,3)
            		if alp == 1:
				warrior=WarriorAnt(str(self.team),1,cell)
                		self.ants.append(warrior)
				self.warriors.append(warrior)
				cell.ants.append(warrior)
            		elif alp == 2:
				worker=WorkerAnt(str(self.team),1,cell)
                		self.ants.append(worker)
				self.workers.append(worker)
            		else:
				forager=ForagerAnt(str(self.team),1,cell)
                		self.ants.append(forager)
				self.foragers.append(forager)
				cell.ants.append(forager)




    	# room yaratinca food -= 1 ve workersant -= 1
	#20x20 ise 20den fazla karincan olamiyor

    	def cycle2(self,turn,cell,events):
		#if len(self.foragers)>0:
		#	print self.team, " ", self.foragers[0].cell.k , " ",self.foragers[0].cell.l
		
		#print "=========Team",self.team
		#print self.food,"Food"
		#print len(self.warriors), "Warriors"
		#print len(self.foragers), "Foragers"	
		#print len(self.workers), "Workers"
		#print len(self.ants), "Total Ants"
		while self.food>=1:      	
			if len(self.workers)>=1:
				self.food-=1
				worker=self.workers[0]
				del self.ants[self.ants.index(worker)]
				del self.workers[0]
				baris = random.randint(1,3)
            			if baris == 1:
                			self.rooms.append(WarriorRoom())
					events.append("A worker from team "+ str(self.team) +" sacrificed himself for a warrior room")
            			elif baris == 2:
                			self.rooms.append(WorkerRoom())
					events.append("A worker from team " + str(self.team) + " sacrificed himself for a worker room")
            			else:
                			self.rooms.append(ForagerRoom())
					events.append("A worker from team " + str(self.team) + " sacrificed himself for a forager room")
			else:
				break
				
		for i in range(len(self.workers)):
			if len(self.ants)<20:		#If amount of ants is <= grid size 
				ape=random.randint(0,len(self.rooms)-1)
				ant=self.rooms[ape].createAnt(self.team,turn,cell)
				self.ants.append(ant)
				cell.ants.append(ant)
				if ant.type == "fr":
                			self.foragers.append(ant)
            			elif ant.type == "wa":
                			self.warriors.append(ant)
            			else:
                			self.workers.append(ant)
				
					
		
				
				
				













			
