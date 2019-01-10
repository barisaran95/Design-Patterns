import requests
from APIProxy import *
import json

class LyricsAPI(APIProxy):
		
	def getInfo(self,top_song):
		r = requests.get('https://api.lyrics.ovh/v1/'+self.artist+"/"+top_song)
		

		body = json.loads(r.text)

		return body['lyrics']

