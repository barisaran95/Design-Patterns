from Responses import *
import random


class Audience:
    def __init__(self):
        self.strategyList = []
        self.goodResponses = []
        self.badResponses = []
        self.observingGladiator = None
        self.eventType = None
    
    def update(self, event):
        pass
    
    def setGoodResponse(self, responseType):
        self.goodResponses = responseType
        
    def setBadResponse(self, responseType):
        self.badResponses = responseType
        
    def getResponse(self):
        if(self.eventType != None):
            if(self.eventType[0] == "p"):
                return self.goodResponses[random.randint(0, len(self.goodResponses) - 1)]
            else:
                return self.badResponses[random.randint(0, len(self.badResponses) - 1)]
        else:
            return ""

    def setStrategy(self, strList):
        self.strategyList = strList
        

class ConcreteAudience(Audience):

    def update(self, event):
        self.eventType = event