class Viewer:
	
	def getArtist(self):
		artist = input('Enter the name of the artist:')
		return artist

	def display(self,music,lyrics,event):
		print("--------------------------------------------------------------------------------")
		if(music[0]!='!'):
			print ("The most popular song of " + music[0] + " is " + music[1] + " from album '" + music[2] + "' which has been released on " + music[3] + ".")
		else:
			print(music)
		print("--------------------------------------------------------------------------------")
		print(lyrics)
		print("--------------------------------------------------------------------------------")
		if(event[0]!='!'):
			print("Closest upcoming event of "+event[0]+" is on "+event[1]+":")
			print("The name of the event is "+event[2]+".")
			print("The event will take place in "+event[3]+","+event[4]+".")	
		else:
			print(event)
