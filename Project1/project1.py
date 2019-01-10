from Universe import *
from Probe import *
import random
def main():
	universe1=Universe(2**10)
	universe1.printStars()
	probeStart=Coordinate(random.randint(1,242)+22,random.randint(1,242)+22,random.randint(1,242)+22)
	probe=Probe(probeStart,2**80)
	print("==================================")
	probe.hashMapCreate(universe1)
	probe.travelStars(universe1)	

if(__name__ == "__main__"):
    main()

