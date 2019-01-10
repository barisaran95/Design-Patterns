from EventAPI import *
from LyricsAPI import *
from MusicAPI import *
from Viewer import *
from Log import *

class Controller:
	def __init__(self):
		self.viewer=Viewer()
		self.logger=Log()

	def musicAPI(self,artist):
		try:
			song_info=MusicAPI(artist).getInfo()
			self.logger.log('MusicAPI.log','Someone has searched for '+artist+'. MusicAPI succesful.')			
			return song_info
		except:
			self.logger.log('MusicAPI.log','Someone has searched for '+artist+'. MusicAPI unsuccesful.')	
			return '!The band does not exist!'

	def lyricsAPI(self,artist,top_song):
		try:
			lyrics=LyricsAPI(artist).getInfo(top_song)
			self.logger.log('LyricsAPI.log','Someone has searched for '+artist+'. LyricsAPI succesful.')
			return lyrics
		except:
			self.logger.log('LyricsAPI.log','Someone has searched for '+artist+'. LyricsAPI unsuccesful.' )
			return "!Lyrics not found!"

	def eventAPI(self,artist):
		try:
			event=EventAPI(artist).getInfo()
			self.logger.log('EventAPI.log','Someone has searched for '+artist+'. EventAPI succesful.')
			return event
		except:	
			self.logger.log('EventAPI.log','Someone has searched for '+artist+'. EventAPI unsuccesful.')
			return '!No events found!' 

	def mainloop(self):
		while(True):
			artist=self.viewer.getArtist()
			music=self.musicAPI(artist)
			lyrics=self.lyricsAPI(artist,music[1])
			event=self.eventAPI(artist)
			self.viewer.display(music,lyrics,event)




