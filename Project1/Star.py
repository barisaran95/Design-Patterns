from Planet import *
from Coordinate import *
import random

class Star:
	def __init__(self, coordinate):
		self.x=coordinate.x
		self.y=coordinate.y
		self.z=coordinate.z
		self.planets=[]
		self.chanceOfLife=None
		self.numOfPlanets=None
		self.goldilocksZone=None
		self.recharge=None
		self.visited=False	

	@staticmethod
	def life(planet,chance,goldilocks):
		i=random.randint(1,10000)
		if i <= chance*10**4:
			if planet.distance > goldilocks[0] and planet.distance < goldilocks[1]:
				if planet.planetId[0][0]=='h':
					planet.life=True
		
class DwarfStar(Star):
	def __init__(self,coordinate):
		Star.__init__(self,coordinate)
		self.chanceOfLife=0.0006
		self.numOfPlanets=random.randint(1,8)+7
		self.goldilocksZone=[10**7*x for x in [30,90]]
		self.recharge=2**20
		for i in range(self.numOfPlanets):
			j=random.randint(1,3)
			k=random.randint(1,300)*10**7
			if j==1:
				self.planets.append(RockyPlanet(k))
			elif j==2:
				self.planets.append(GaseousPlanet(k))
			else:
				self.planets.append(HabitablePlanet(k))
			self.planets[i].planetId+=str(self.x%10*7)+'-'+str(self.y%10*7)+'-'+str(self.z%10*7)+'-'+str(i)
			Star.life(self.planets[i],self.chanceOfLife,self.goldilocksZone)
			

class GiantStar(Star):
	def __init__(self,coordinate):
		Star.__init__(self,coordinate)
		self.chanceOfLife=0.0005
		self.numOfPlanets=random.randint(1,6)+4
		self.goldilocksZone=[10**7*x for x in [100,250]]
		self.recharge=2**30
		for i in range(self.numOfPlanets):
			j=random.randint(1,3)
			k=random.randint(1,300)*10**7
			if j==1:
				self.planets.append(RockyPlanet(k))
			elif j==2:
				self.planets.append(GaseousPlanet(k))
			else:
				self.planets.append(HabitablePlanet(k))
			self.planets[i].planetId+=str(self.x%10*7)+'-'+str(self.y%10*7)+'-'+str(self.z%10*7)+'-'+str(i)
			Star.life(self.planets[i],self.chanceOfLife,self.goldilocksZone)

class MediumStar(Star):
	def __init__(self,coordinate):
		Star.__init__(self,coordinate)
		self.chanceOfLife=0.0009
		self.numOfPlanets=random.randint(1,8)+1
		self.goldilocksZone=[10**7*x for x in [60,140]]
		self.recharge=2**25
		for i in range(self.numOfPlanets):
			j=random.randint(1,3)
			k=random.randint(1,300)*10**7
			if j==1:
				self.planets.append(RockyPlanet(k))
			elif j==2:
				self.planets.append(GaseousPlanet(k))
			else:
				self.planets.append(HabitablePlanet(k))
			self.planets[i].planetId+=str(self.x%10*7)+'-'+str(self.y%10*7)+'-'+str(self.z%10*7)+'-'+str(i)
			Star.life(self.planets[i],self.chanceOfLife,self.goldilocksZone)







