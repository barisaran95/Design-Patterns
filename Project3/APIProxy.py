import requests
from abc import ABC, abstractmethod

class APIProxy(ABC):
	
	def __init__(self,artist):
		self.artist=artist
	
	@abstractmethod
	def getInfo(self):
		pass	
