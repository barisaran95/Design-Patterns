import requests
import base64
import json

from APIProxy import *

class MusicAPI(APIProxy):
		
	def getInfo(self):
		header = {"Authorization": 'Basic ' + 
			str(base64.b64encode(("131a4b9f2dc444f5a2bb97b40a93573c" + ":" + "5ce4bf58ad35437eb7a2f32580a0e2d6").encode()))[2:-1]
		}
		params = {'grant_type':'client_credentials', 
			'client_id': '131a4b9f2dc444f5a2bb97b40a93573c',
			'client_secret':'5ce4bf58ad35437eb7a2f32580a0e2d6'}

		r = requests.post('https://accounts.spotify.com/api/token',data=params,headers=header)
		body = json.loads(r.text)
		token = body['access_token']
	
		bombik={'Authorization':'Bearer '+ token }

		r = requests.get('https://api.spotify.com/v1/search?q='+self.artist+'&type=artist',headers=bombik)
		body = json.loads(r.text)
		artist_id=body['artists']['items'][0]['id']

		r = requests.get("https://api.spotify.com/v1/artists/"+artist_id+"/top-tracks?country=US",headers=bombik)
		body = json.loads(r.text)
		song_info=[]
		self.top_song=body['tracks'][0]['name']
		song_album=body['tracks'][0]['album']['name']
		release_date=body['tracks'][0]['album']['release_date']	
		song_info.append(self.artist)
		song_info.append(self.top_song)
		song_info.append(song_album)
		song_info.append(release_date)
		return song_info










