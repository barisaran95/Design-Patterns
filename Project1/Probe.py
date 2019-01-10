from Universe import *
import bisect
import math

class Probe:
	def __init__(self, start, fuel):
	#if no life found
	#if runs out of fuel
		self.start=start
		self.fuel=fuel
		self.distanceTraveled=0
		self.numStarsExplored=0
		self.numPlanetsExplored=0
		#self.distances=[]
		#self.sortedStars=[]
		self.currentLocation=start
		self.hashMap={}
		self.lifeFound=False
		self.distanceFromStart=0
		self.planetId=None
		
	def hashMapCreate(self,universe):
		for i in range(len(universe.allStars)):
			self.hashMap[str(universe.coordinates[i])]=universe.allStars[i]
	

	def travelStars(self,universe):
		coordinateHolder=None
		distanceHolder=0
		distances=[]
		indexHolder=0
		for i in range(len(universe.allStars)):
			if universe.allStars[i].visited==False:
				j=math.sqrt((self.currentLocation.x-self.hashMap[str(universe.coordinates[i])].x)**2+(self.currentLocation.y-self.hashMap[str(universe.coordinates[i])].y)**2+(self.currentLocation.z-self.hashMap[str(universe.coordinates[i])].z)**2)
				if len(distances)==0 or j<distances[0]:
					bisect.insort(distances,j)
					distanceHolder=j
					coordinateHolder=universe.coordinates[i]
					indexHolder=i
		#print(distanceHolder)
		if self.lifeFound==False and self.fuel>=distanceHolder+self.distanceFromStart:
			self.fuel=self.fuel-distanceHolder
			if self.fuel<0:
				print("Out of fuel!")
				print("Your origin was: ",self.start.x,self.start.y,self.start.z)
				print("You have traveled ",self.distanceTraveled," miles")
				print("-----","Visited", self.numStarsExplored," stars")
				print("-----","Explored", self.numPlanetsExplored," planets")
				return
			
			universe.allStars[indexHolder].visited=True
			#print(universe.allStars[indexHolder].visited)
			#print(self.hashMap[str(coordinateHolder)].visited)
			self.fuel=self.fuel+self.hashMap[str(coordinateHolder)].recharge
			self.currenLocation=coordinateHolder
			self.distanceTraveled=self.distanceTraveled+distanceHolder
			self.numStarsExplored=self.numStarsExplored+1
			#numPlanets=self.hashMap[str(coordinateHolder)].numPlanets
			#self.fuel=self.fuel-distanceHolder
			for i in range(self.hashMap[str(coordinateHolder)].numOfPlanets):
				self.numPlanetsExplored=self.numPlanetsExplored+1
				if self.hashMap[str(coordinateHolder)].planets[i].life:
					self.lifeFound=True
					#report()
					print("Life Found on ",self.hashMap[str(coordinateHolder)].planets[i].planetId)
					self.planetId=self.hashMap[str(coordinateHolder)].planets[i].planetId
					
			self.distanceFromStart=math.sqrt((self.currentLocation.x-self.start.x)**2+(self.currentLocation.y-self.start.y)**2+(self.currentLocation.z-self.start.z)**2)
			self.travelStars(universe)
		else:
			self.fuel=self.fuel-self.distanceFromStart
			if self.fuel<0:
				print("Out of fuel!")
				print("Your origin was: ",self.start.x,self.start.y,self.start.z)
				print("You have traveled ",self.distanceTraveled," miles")
				print("-----","Visited", self.numStarsExplored," stars")
				print("-----","Explored", self.numPlanetsExplored," planets")
				return
			self.currenLocation=self.start
			self.distanceTraveled=self.distanceTraveled+self.distanceFromStart
			print("Your origin was: ",self.start.x,self.start.y,self.start.z)
			print("You have traveled ",self.distanceTraveled," miles")
			print("-----","You have ", self.fuel," remaining")
			print("-----","Visited", self.numStarsExplored," stars")
			print("-----","Explored", self.numPlanetsExplored," planets")
			if self.lifeFound:
				print("Life found on planet ",self.planetId)
			else:
				print("No life found. We are alone")
			









		
