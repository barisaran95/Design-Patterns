import requests
import json
from APIProxy import *

class EventAPI(APIProxy):
	
	def getInfo(self):
		r = requests.get('https://rest.bandsintown.com/artists/'+self.artist+'/events?app_id=baran1&date=upcoming')
		body = json.loads(r.text)
		date=body[0]['datetime']
		city=body[0]['venue']['city']
		event_name=body[0]['venue']['name']
		country=body[0]['venue']['country']
		event_info=[]
		event_info.append(self.artist)
		event_info.append(date)
		event_info.append(event_name)
		event_info.append(city)
		event_info.append(country)
		return event_info	
