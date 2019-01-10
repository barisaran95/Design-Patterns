from Meadow import *

def main():

	a = Meadow()
	winner=False
	turn=1
	while(winner==False):				#While there is no winner
    		result=a.cycle(True,turn,winner)		#Invoke cycle with menu
		turn+=1
		if result>0:				#If the user wants to pass rounds
			for i in range(result-1):
				a.cycle(False,turn,winner)	#Invoke cycle without menu
				turn+=1
		winner=a.endgame()


if(__name__ == "__main__"):
    	main()
