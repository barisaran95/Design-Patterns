from Gladiator import *
from Audience import *


class Arena:
    def __init__(self):
        self.audiences = []
        self.gladiators = []
        self.setGladiators()
        self.setAudiences()
        self.setStrategies()
            
    def registers(self, glad1, glad2):    
        for audience in self.audiences:
            i=random.randint(1,2)       #randomly supporting one of the gladiators on the stage
            if i==1:
                glad1.attach(audience)
                
            else:
                glad2.attach(audience)
        
    def deregister(self,glad1,glad2):    
        glad1.detach()
        glad2.detach()

            
    def round(self):
        i = random.randint(0,len(self.gladiators)-1)     #random gladiator index1
        j = random.randint(0,len(self.gladiators)-1)     #random gladiator index2
        
        while(j == i):
            j= random.randint(0,len(self.gladiators)-1)
        
        print("The match is about the begin between {} and {}.".format(self.gladiators[i].name, self.gladiators[j].name))    
        print("=============================================")
        self.registers(self.gladiators[i], self.gladiators[j])
        defeated = self.battle(self.gladiators[i], self.gladiators[j])
        self.deregister(self.gladiators[i], self.gladiators[j])
        
        if(defeated == self.gladiators[i]):
            del self.gladiators[i]
            
        elif(defeated == self.gladiators[j]):
            del self.gladiators[j]
            
        else:
            pass
        
        if(len(self.gladiators)==1):
            print("Hail to the winner! Glorius {}!!!".format(self.gladiators[0].name))
        
    #Returns the defeated gladiator if he is sentenced to die
    #Returns None if nobody is sentenced to die
    def battle(self, gladiator1, gladiator2):
        responseString = ""
        
        while(gladiator1.health > 0 and gladiator2.health > 0):
            i = random.randint(1,100)
            j = random.randint(1,100)
            dodge_possibilty = random.randint(1,100)
            l = random.randint(1,100)
            
            
            if (dodge_possibilty > 10):    #%10 dodge
            
                if (i < 6):   #%5 chance
                    gladiator2.health -= gladiator1.attackPower*2 #critical hit
                    gladiator2.set_state("n_crit_damaged")
                    gladiator1.set_state("p_crit_hit")
                    
                else:
                    gladiator2.health -= gladiator1.attackPower   #normal hit
                    gladiator2.set_state("n_damaged")
                    gladiator1.set_state("p_hit")
                    
            else:
                gladiator2.set_state("p_dodge")
                gladiator1.set_state("n_dodgedby")
                
            if (gladiator2.health <= 0):  
                #gladiator2 lost,gladiator1 win
                print("=============================================")
                print("{} is won the fight! Will audiences let {} live or send him to the ground!".format(gladiator1.name, gladiator2.name))
                gladiator1.attackPower += gladiator1.attackPower*20/100
                gladiator1.previous_wins += 1
                gladiator1.health = gladiator1.originalHealth
                gladiator2.set_state("n_died")      #lost
                gladiator1.set_state("p_killed")    #won
                return self.thumbs(gladiator2,gladiator1)
                
            else:   
                
                if (l > 10):    #%10 dodge
                    if (j<6):   #%5 chance
                        gladiator1.health -= gladiator2.attackPower*2 #critical hit
                        gladiator1.set_state("n_crit_damaged")
                        gladiator2.set_state("p_crit_hit")
                    else:
                        gladiator1.health-=gladiator2.attackPower   #normal hit
                        gladiator1.set_state("n_damaged")
                        gladiator2.set_state("p_hit")
                else:
                    gladiator1.set_state("p_dodge")
                    gladiator2.set_state("n_dodgedby")
                    
                if (gladiator1.health <= 0):
                    #gladiator1 lost,gladiator2 win
                    print("=============================================")
                    print("{} is won the fight! Will audiences let {} live or send him to the ground!".format(gladiator2.name, gladiator1.name))
                    gladiator1.set_state("n_died")      #lost
                    gladiator2.set_state("p_killed")    #won
                    gladiator2.attackPower += gladiator2.attackPower*20/100
                    gladiator2.previous_wins += 1
                    gladiator2.health = gladiator2.originalHealth
                    return self.thumbs(gladiator1,gladiator2)
            for each_audience in self.audiences:
                responseString += each_audience.getResponse()
                responseString += ".."
            
            print("The audiences yells.....{}. ".format(responseString))
    
    def thumbs(self,defeatedGladiator,victoriousGladiator):
        #eger iyi savasmis ise hayatta kalma sansi artsin
        #misal karsi tarafin %95 canini goturmusse seyircinin %75 thumbs up verme sansi
        chanceToSurvive = random.randint(1,100)
        deathSentence=True
        if (victoriousGladiator.health <= victoriousGladiator.originalHealth * 5/100):
            if(chanceToSurvive <= 70):
                deathSentence = False
            # %70 thumbs up
        elif(victoriousGladiator.health <= victoriousGladiator.originalHealth*1/10):
            if(chanceToSurvive <= 60):
                deathSentence = False
            # %60 thumbs up
        elif(victoriousGladiator.health <= victoriousGladiator.originalHealth*2/10):
            if(chanceToSurvive <= 50):
                deathSentence = False
            # %50 thumbs up
        elif(victoriousGladiator.health <= victoriousGladiator.originalHealth*3/10):
            if(chanceToSurvive <= 40):
                deathSentence = False
            # %40 thumbs up
        else:
            if(chanceToSurvive <= 30):
                deathSentence = False
            # %30 thumbs up
        if(deathSentence):
            print("{} is dead!".format(defeatedGladiator.name))
            return defeatedGladiator
            
        else:
            print("Audiences let {} live for a reward of a great war".format(defeatedGladiator.name))
            defeatedGladiator.health = defeatedGladiator.originalHealth
            #reset health and keep fighting
            return None
        
    
    def setGladiators(self):
        gladiator_number = 0
        while(True):
            created_gladiator = Gladiator().createGladiator(gladiator_number)
            if(created_gladiator == False):
                break
            self.gladiators.append(created_gladiator)
            gladiator_number += 1
            
    def setAudiences(self):
        for audience_number in range(0,100):
            created_audience = ConcreteAudience()
            self.audiences.append(created_audience)
            
    def setStrategies(self):
        for audience in self.audiences:
            rand_strategy = random.randint(1,3)
            
            if(rand_strategy == 1):
                response = Responses(PositiveAudienceStrategy())
                audience.setStrategy(response.response_context())
                
            elif(rand_strategy == 2):
                response = Responses(NegativeAudienceStrategy())
                audience.setStrategy(response.response_context())
                
            else:
                response = Responses(HybridStrategy())
                audience.setStrategy(response.response_context())
            audience.setGoodResponse(response.cheers)
            audience.setBadResponse(response.barks)