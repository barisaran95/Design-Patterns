from Star import *

import random

class Universe:
	#starType=""

	def __init__(self,starNum):
		self.starNum=starNum
		self.dwarf=[]
		self.medium=[]
		self.giant=[]
		self.coordinates=[]
		self.allStars=[]
		
		for i in range(starNum):
			#print("Amca")
			j=random.randint(1,3)
			coordinate = Universe.uniqueCoordinate(self.coordinates)
			if j==1:
				self.dwarf.append(DwarfStar(coordinate))
				self.allStars.append(DwarfStar(coordinate))
			elif j==2:
				self.medium.append(MediumStar(coordinate))
				self.allStars.append(MediumStar(coordinate))
			else:
				self.giant.append(GiantStar(coordinate))
				self.allStars.append(GiantStar(coordinate))
			self.coordinates.append(coordinate)

			
	def printStars(self):
		print("Total number of stars in my universe:" , self.starNum)
		print("There are " , len(self.dwarf) , "Dwarf Stars with:")
		Universe.countPlanets(self.dwarf)
		print("There are " , len(self.medium) , "Medium Stars with:")
		Universe.countPlanets(self.medium)
		print("There are " , len(self.giant) , "Giant Stars with:")
		Universe.countPlanets(self.giant)

	@staticmethod
	def countPlanets(starList):
		#counter=0
		numRocky=0
		numGaseous=0
		numHabitable=0
		numLife=0
		for i in range(len(starList)):
				for j in range(len(starList[i].planets)):
					planetId=starList[i].planets[j].planetId
					if planetId[0][0]=='r':
						numRocky=numRocky+1
					elif planetId[0][0]=='g':
						numGaseous=numGaseous+1
					elif planetId[0][0]=='h':
						numHabitable=numHabitable+1
					else:
						print("Problem")
					if starList[i].planets[j].life:
						numLife=numLife+1
		print("-----",numGaseous," Gaseous Planets")
		print("-----",numRocky," Rocky Planets")
		print("-----",numHabitable," Habitable Planets")
		print("-----",numLife,"Planets with Intelligent Life")
	
	@staticmethod
	def uniqueCoordinate(coordinates):
		coordinate=Coordinate((random.randint(1,242)+22)**10*7,(random.randint(1,242)+22)**10*7,(random.randint(1,242)+22)**10*7)
		for i in range(len(coordinates)):	
			if coordinate.x==coordinates[i].x and coordinate.y==coordinates[i].y and coordinate.z==coordinates[i].z:
				#print("There is a star at: ", coordinate.x,coordinate.y,coordinate.z)
				Universe.uniqueCoordinate(coordinates)
		return coordinate
			
							
		

























