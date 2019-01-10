class Planet:
	def __init__(self,distance):
		#life olmasi icin yildizinin goldilocks zone unda olmali ve habitable olmali
		self.distance=distance
		self.life=False

class RockyPlanet(Planet):
	def __init__(self,distance):
		Planet.__init__(self,distance)
		self.planetId='r'
		pass

class GaseousPlanet(Planet):
	def __init__(self,distance):
		Planet.__init__(self,distance)
		self.planetId='g'
		#if(distance) yasam var
		pass

class HabitablePlanet(Planet):
	def __init__(self,distance):
		Planet.__init__(self,distance)
		self.planetId='h'
		pass
