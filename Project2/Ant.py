import random

class Ant:
	antId=0
    	def __init__(self):
		self.__class__.antId+=1


class ForagerAnt(Ant):
	

    	def __init__(self,team,turn,cell):
        	Ant.__init__(self)
		self.type="fr"
		self.team=team
		self.food=0
		self.turn=turn
		self.cell=cell
		
		
		#yemek arama
		#eve donus
		#eve yemek birakma
        	pass


class WarriorAnt(Ant):
    	def __init__(self,team,turn,cell):
        	Ant.__init__(self)
		self.type="wa"
		self.team=team
		self.turn=turn
		self.power = random.randint(1,100)
		self.cell=cell
		#dolasma
		#savasciyla savasma/random guc/kazanirsa yeni guc kazanma
		#toplayiciyla savasma %50
		#kaleye saldirma
        	pass


class WorkerAnt(Ant):
    	def __init__(self,team,turn,cell):
        	Ant.__init__(self)
		self.type="wo"
		self.team=team
		self.turn=turn
		#karinca uretme
		#kendini feda etme/random oda uretme
        	pass
