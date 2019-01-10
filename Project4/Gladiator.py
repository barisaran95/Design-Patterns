import json


class Gladiator:
    def __init__(self):
        self.observers = []
        self.gladiator_state = None
        self.name = ""
        self.age = None
        self.birthplace = ""
        self.health = 0
        self.originalHealth = 0
        self.previous_wins = 0
        self.attackPower=10
        
    def attach(self, observer):
        observer.observingGladiator = self
        self.observers.append(observer)
    
    def detach(self):
        for observer in self.observers:
            observer.observingGladiator = None
            observer.eventType = None
        del self.observers[:]
        
    def notify(self):
        for observer in self.observers:
            observer.update(self.gladiator_state)
        
    def set_state(self, arg):
        self.gladiator_state = arg
        self.notify()
    
    def createGladiator(self, listIndex):
        with open("gladiators.json") as datas:
            getDatas = json.load(datas)
            
        if(len(getDatas) > listIndex):    
            self.name = getDatas[listIndex]['name']
            self.age = getDatas[listIndex]['age']
            self.birthplace = getDatas[listIndex]['birthplace']
            self.health = getDatas[listIndex]['health']
            self.originalHealth = getDatas[listIndex]['health']
            return self
        return False
