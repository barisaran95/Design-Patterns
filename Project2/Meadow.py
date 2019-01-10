from Cell import *
from Queen import *

class Meadow:
	def __init__(self):
		self.matrix = []
		self.winner=False
       		for i in range(0, 20):
        		x = []
			self.matrix.append(x)
           		for j in range(0, 20):
                		x.append(Cell(i,j))
                		
		


       		numQueens = random.randint(3, 4) #3-4 anthills
       		#print numQueensbbbbb

       		for team in range(numQueens):
					
        	    	x = random.randint(0, 19)
        	    	y = random.randint(0, 19)
			
        	    	while self.matrix[x][y].hill != None:
        	        	x = random.randint(0, 19)
        	        	y = random.randint(0, 19)
		
        	 
			self.matrix[x][y].hill=Queen(self.matrix[x][y], team+1).product
			
			#anthill=AntHill(10, 1, 10, x, y)
			#self.matrix[x][y].hill=anthill
			#print(x,y)
        	    	#print "x=", x, ", y=", y
        	    	#print "y= ", y
        	    	#print "Builder product x= ", builder.product.x
        	    	#print "Builder product y= ", builder.product.y
			#print "Cell x", self.matrix[x][y].hill.x
			#print "Cell y", self.matrix[x][y].hill.y
			#print "======="
		

    	def cycle(self,menu,turn,winner):
		#print("ICERDEYIM ABI")
		#turn+=1
		events=[]
 		
		for i in range(3):
			x = random.randint(0, 19)
               		y = random.randint(0, 19)
			while self.matrix[x][y].hill != None:
				x = random.randint(0, 19)
                		y = random.randint(0, 19)
			self.matrix[x][y].food += 1

		
		for k in range(20):									#move vs
			for l in range(20):
				#print self.matrix[k][l].ants[0].team
				if self.matrix[k][l].hill!=None:
					self.matrix[k][l].hill.cycle2(turn,self.matrix[k][l], events)
				antAmount=len(self.matrix[k][l].ants)				
				while antAmount>0:
				#for m in range(len(self.matrix[k][l].ants)-1):
					#print str(k)+"-"+str(l)+" = " + str(len(self.matrix[k][l].ants))+str(antAmount)
					if len(self.matrix[k][l].ants) >= antAmount:
						if self.matrix[k][l].ants[antAmount-1].type=="fr" and self.matrix[k][l].ants[antAmount-1].food>0:	#if the ant is a forager with food
						#print " ", k,l
							Meadow.backToHome(self.matrix[k][l].ants[antAmount-1], k, l, self.matrix,turn,antAmount-1)		#return to anthill
						else:	
							if self.matrix[k][l].ants[antAmount-1].type!="wo":	
								Meadow.move(self.matrix[k][l].ants[antAmount-1], k, l, self.matrix, turn, antAmount-1, events)
					antAmount-=1 						#sondaki turn olayi cakisirsa biseyler oluyo

		for k in range(20):									#destroy anthill if no forager
			for l in range(20):
				if self.matrix[k][l].hill!=None:
					if len(self.matrix[k][l].hill.foragers)==0:			#EMIN OL
						evnt="Anthill "+str(self.matrix[k][l].hill.team)+ " has been destroyed because of lack of forager ants."
						events.append(evnt)
						#print "Burdayim"
						Meadow.destroyAnthill(self.matrix,self.matrix[k][l].hill,k,l)
		counter=0
		hill=None
		for k in range(20):									#endgame
			for l in range(20):
				if self.matrix[k][l].hill!=None:
					counter+=1
					hill=self.matrix[k][l].hill
		if counter<=1:
			events.append("Game Over")
			if counter==1:
				events.append("Team "+str(hill.team)+" has won!")
			elif counter==0:
				events.append("No survivors")				
			self.winner=True	
					
				
		while menu:
            		print ("=====================MENU====================")
			print "||TURN:",str(turn)
            		print ("|| 1. Display the Meadow                   ||")
            		print ("|| 2. Run the next n cycle without halting ||")
			print ("=============================================")
				
            		answer = input()

            		if answer == 1:	
				for i in range(len(events)):
					print events[i]			
               			return 0
            		elif answer == 2:
               			print ("Enter the number of cycle:")
               			number = input()
				if number>0:	
					return number
				print("!!!!!Should be more than 0!!!!!")
            		else:
               			print("!!!!!Wrong input!!!!!")

		for a in range(len(events)):
			print events[a]


	def endgame(self):
		return self.winner
		
		
	@staticmethod
	def destroyAnt(ant,i,j,matrix,m):
		for a in range(20):
			for b in range(20):
				if matrix[a][b].hill!=None:
					if matrix[a][b].hill.team == ant.team:
						for k in range(len(matrix[a][b].hill.ants)):
							if ant.type==matrix[a][b].hill.ants[k].type and ant.antId==matrix[a][b].hill.ants[k].antId:	
								del matrix[a][b].hill.ants[k]
								break
						if ant.type=="fr":
							for l in range(len(matrix[a][b].hill.foragers)):
								if ant.antId==matrix[a][b].hill.foragers[l].antId:
									del matrix[a][b].hill.foragers[l]
									break
						elif ant.type=="wa":
							for l in range(len(matrix[a][b].hill.warriors)):
								if ant.antId==matrix[a][b].hill.warriors[l].antId:
									del matrix[a][b].hill.warriors[l]
									break
		del ant
		


	@staticmethod
	def destroyAnthill(matrix,anthill,i,j):
		for a in range(20):
			for b in range(20):
				if len(matrix[a][b].ants)>0:
					for c in range(len(matrix[a][b].ants)):
						if c < len(matrix[a][b].ants):
							if matrix[a][b].ants[c].team==anthill.team:
								#sonuncu yanma muhabbeti
								del matrix[a][b].ants[c]
							
		#print "Anthill ", anthill.team,"has been destroyed!"
		del matrix[i][j].hill
		matrix[i][j].hill=None
		
		
	@staticmethod
	def backToHome(ant,k,l,matrix,turn,antAmount):
		
		if ant.turn == turn:
			a=k
			b=l
			for i in range(20):
				for j in range(20):
					if matrix[i][j].hill!=None:
						if(matrix[i][j].hill.team == ant.team):
							
							if(k < i):
								a += 1
								matrix[a][b].ants.append(matrix[k][l].ants[antAmount])
								del matrix[k][l].ants[antAmount]
								matrix[i][j].ants[len(matrix[i][j].ants)-1].cell=matrix[i][j]
							elif(k > i):
								a -= 1
								matrix[a][b].ants.append(matrix[k][l].ants[antAmount])
								del matrix[k][l].ants[antAmount]
							elif(l < j):
								b += 1
								matrix[a][b].ants.append(matrix[k][l].ants[antAmount])
								del matrix[k][l].ants[antAmount]
							elif(l > j):
								b -=1
								matrix[a][b].ants.append(matrix[k][l].ants[antAmount])
								del matrix[k][l].ants[antAmount]
							else:
								matrix[k][l].ants[antAmount].food -= 1
								matrix[i][j].hill.food += 1
								evnt="A food has been returned to team "+str(matrix[i][j])
								events.append(evtn)
							break
				break

	
	@staticmethod
	def move(ant,k,l,matrix,turn,antAmount,events):
		if ant.turn==turn:
			i=k
			j=l
			
			if k==0 and l==0:
				#print "Kosedeyim1 ",  k,l
				number=random.randint(1,2)
				if number==1:
					i+=1					
					matrix[i][j].ants.append(matrix[k][l].ants[antAmount])
					del matrix[k][l].ants[antAmount]
					matrix[i][j].ants[len(matrix[i][j].ants)-1].cell=matrix[i][j]
					
				else:
					j+=1
					matrix[i][j].ants.append(matrix[k][l].ants[antAmount])
					del matrix[k][l].ants[antAmount]
					matrix[i][j].ants[len(matrix[i][j].ants)-1].cell=matrix[i][j]
			elif k==0 and l==19:
				#print "Kosedeyim2 ",  k,l
				number=random.randint(1,2)
				if number==1:
					i+=1
					matrix[i][j].ants.append(matrix[k][l].ants[antAmount])
					del matrix[k][l].ants[antAmount]
					matrix[i][j].ants[len(matrix[i][j].ants)-1].cell=matrix[i][j]
				else:
					j-=1
					matrix[i][j].ants.append(matrix[k][l].ants[antAmount])
					del matrix[k][l].ants[antAmount]
					matrix[i][j].ants[len(matrix[i][j].ants)-1].cell=matrix[i][j]
			elif k==19 and l==0:
				#print "Kosedeyim3 ",  k,l
				number=random.randint(1,2)
				if number==1:
					i-=1
					matrix[i][j].ants.append(matrix[k][l].ants[antAmount])
					del matrix[k][l].ants[antAmount]
					matrix[i][j].ants[len(matrix[i][j].ants)-1].cell=matrix[i][j]
				else:
					j+=1
					matrix[i][j].ants.append(matrix[k][l].ants[antAmount])
					del matrix[k][l].ants[antAmount]
					matrix[i][j].ants[len(matrix[i][j].ants)-1].cell=matrix[i][j]
			elif k==19 and l==19:
				#print "Kosedeyim4 ",  k,l
				number=random.randint(1,2)
				if number==1:
					i-=1
					matrix[i][j].ants.append(matrix[k][l].ants[antAmount])
					del matrix[k][l].ants[antAmount]
					matrix[i][j].ants[len(matrix[i][j].ants)-1].cell=matrix[i][j]
				else:
					j-=1
					matrix[i][j].ants.append(matrix[k][l].ants[antAmount])
					del matrix[k][l].ants[antAmount]
					matrix[i][j].ants[len(matrix[i][j].ants)-1].cell=matrix[i][j]
			elif k==0:
				#print "Kenardayim1 ",  k,l
				number=random.randint(1,3)
				if number==1:
					i+=1
					matrix[i][j].ants.append(matrix[k][l].ants[antAmount])
					del matrix[k][l].ants[antAmount]
					matrix[i][j].ants[len(matrix[i][j].ants)-1].cell=matrix[i][j]
				elif(number==2):
					j-=1
					matrix[i][j].ants.append(matrix[k][l].ants[antAmount])
					del matrix[k][l].ants[antAmount]
					matrix[i][j].ants[len(matrix[i][j].ants)-1].cell=matrix[i][j]
				else:
					j+=1
					matrix[i][j].ants.append(matrix[k][l].ants[antAmount])
					del matrix[k][l].ants[antAmount]		
					matrix[i][j].ants[len(matrix[i][j].ants)-1].cell=matrix[i][j]
			elif k==19:
				#print "Kenardayim2 ",  k,l
				number=random.randint(1,3)
				if number==1:
					i-=1
					matrix[i][j].ants.append(matrix[k][l].ants[antAmount])
					del matrix[k][l].ants[antAmount]
					matrix[i][j].ants[len(matrix[i][j].ants)-1].cell=matrix[i][j]
				elif(number==2):
					j-=1
					matrix[i][j].ants.append(matrix[k][l].ants[antAmount])
					del matrix[k][l].ants[antAmount]
					matrix[i][j].ants[len(matrix[i][j].ants)-1].cell=matrix[i][j]
				else:
					j+=1
					matrix[i][j].ants.append(matrix[k][l].ants[antAmount])
					del matrix[k][l].ants[antAmount]
					matrix[i][j].ants[len(matrix[i][j].ants)-1].cell=matrix[i][j]
			elif l==0:
				#print "Kenardayim3 ",  k,l
				number=random.randint(1,3)
				if number==1:
					i+=1
					matrix[i][j].ants.append(matrix[k][l].ants[antAmount])
					del matrix[k][l].ants[antAmount]
					matrix[i][j].ants[len(matrix[i][j].ants)-1].cell=matrix[i][j]
				elif(number==2):
					i-=1
					matrix[i][j].ants.append(matrix[k][l].ants[antAmount])
					del matrix[k][l].ants[antAmount]
					matrix[i][j].ants[len(matrix[i][j].ants)-1].cell=matrix[i][j]
				else:
					j+=1
					matrix[i][j].ants.append(matrix[k][l].ants[antAmount])
					del matrix[k][l].ants[antAmount]
					matrix[i][j].ants[len(matrix[i][j].ants)-1].cell=matrix[i][j]
			elif l==19:
				#print "Kenardayim4 ",  k,l
				number=random.randint(1,3)
				if number==1:
					i+=1
					matrix[i][j].ants.append(matrix[k][l].ants[antAmount])
					del matrix[k][l].ants[antAmount]
					matrix[i][j].ants[len(matrix[i][j].ants)-1].cell=matrix[i][j]
				elif(number==2):
					i-=1
					matrix[i][j].ants.append(matrix[k][l].ants[antAmount])
					del matrix[k][l].ants[antAmount]
					matrix[i][j].ants[len(matrix[i][j].ants)-1].cell=matrix[i][j]
				else:
					j-=1
					matrix[i][j].ants.append(matrix[k][l].ants[antAmount])
					del matrix[k][l].ants[antAmount]	
					matrix[i][j].ants[len(matrix[i][j].ants)-1].cell=matrix[i][j]
			else:
				
				number=random.randint(1,4)
				if number==1:
					i+=1
					matrix[i][j].ants.append(matrix[k][l].ants[antAmount])
					del matrix[k][l].ants[antAmount]
					matrix[i][j].ants[len(matrix[i][j].ants)-1].cell=matrix[i][j]
				elif(number==2):
					i-=1
					matrix[i][j].ants.append(matrix[k][l].ants[antAmount])
					del matrix[k][l].ants[antAmount]
					matrix[i][j].ants[len(matrix[i][j].ants)-1].cell=matrix[i][j]
				elif(number==3):
					j+=1
					matrix[i][j].ants.append(matrix[k][l].ants[antAmount])
					del matrix[k][l].ants[antAmount]
					matrix[i][j].ants[len(matrix[i][j].ants)-1].cell=matrix[i][j]
				else:
					j-=1
					matrix[i][j].ants.append(matrix[k][l].ants[antAmount])
					del matrix[k][l].ants[antAmount]
					matrix[i][j].ants[len(matrix[i][j].ants)-1].cell=matrix[i][j]

			if(matrix[i][j].ants[len(matrix[i][j].ants)-1].type=="fr"):	#Food found
				if matrix[i][j].food>0 and matrix[i][j].ants[len(matrix[i][j].ants)-1].food==0:
					evnt="A forager from team "+ str(matrix[i][j].ants[len(matrix[i][j].ants)-1].team) +" has found food."
					events.append(evnt)
					matrix[i][j].food-=1
					matrix[i][j].ants[len(matrix[i][j].ants)-1].food+=1

				
###
			elif(matrix[i][j].ants[len(matrix[i][j].ants)-1].type=="wa"):

				if matrix[i][j].hill!=None and matrix[i][j].hill.team!=matrix[i][j].ants[len(matrix[i][j].ants)-1].team:
						chance=random.randint(1,5)
						if chance==5:
							evnt = "Anthill "+str(matrix[i][j].hill.team)+" has been destroyed by a warrior from team "+str(matrix[i][j].ants[len(matrix[i][j].ants)-1].team)
							#print "Surdayim"
							Meadow.destroyAnthill(matrix,matrix[i][j].hill,i,j)
						else:
							evnt="A warrior from "+ str(matrix[i][j].ants[len(matrix[i][j].ants)-1].team) +" has failed to destroy the anthill " +  str(matrix[i][j].hill.team)
							events.append(evnt)
							Meadow.destroyAnt(matrix[i][j].ants[len(matrix[i][j].ants)-1],i,j,matrix,len(matrix[i][j].ants)-1)
							#del matrix[i][j].ants[len(matrix[i][j].ants)-1]
				else:
					for m in range(len(matrix[i][j].ants)):
						#print len(matrix[i][j].ants)," ",m
						
						if(matrix[i][j].ants[m].type=="wa"):
							
							if matrix[i][j].ants[m].team != matrix[i][j].ants[len(matrix[i][j].ants)-1].team:
								#print str(m)+ "---"+str(len(matrix[i][j].ants)-1)
								#print str(matrix[i][j].ants[m].team) + "***" + str(matrix[i][j].ants[len(matrix[i][j].ants)-1].team)
								if matrix[i][j].ants[m].power <= matrix[i][j].ants[len(matrix[i][j].ants)-1].power:
									evnt="A warrior from team "+str(matrix[i][j].ants[m].team)+" has been killed by a warrior from team "+ str(matrix[i][j].ants[len(matrix[i][j].ants)-1].team)
									events.append(evnt)
									Meadow.destroyAnt(matrix[i][j].ants[m], i, j, matrix,m)
									break	
									#del matrix[i][j].ants[m]
									#m-=1
									#decorator
								else:
									evnt="A warrior from team "+str(matrix[i][j].ants[len(matrix[i][j].ants)-1].team)+" has been killed by a warrior from team "+str(matrix[i][j].ants[m].team)
									events.append(evnt)
									Meadow.destroyAnt(matrix[i][j].ants[len(matrix[i][j].ants)-1], i, j, matrix,len(matrix[i][j].ants)-1)
									break
									#del matrix[i][j].ants[len(matrix[i][j].ants)-1]
									#m-=1
									#decorator
						elif(matrix[i][j].ants[m].type=="fr"):
							if matrix[i][j].ants[m].team != matrix[i][j].ants[len(matrix[i][j].ants)-1].team:
								chance=random.randint(1,2)
								if chance==1:
									evnt="A forager from team "+str(matrix[i][j].ants[m].team)+" has been killed by a warrior from team "+ str(matrix[i][j].ants[len(matrix[i][j].ants)-1].team)
									events.append(evnt)
									Meadow.destroyAnt(matrix[i][j].ants[m], i, j, matrix,m)
									break

			matrix[i][j].ants[len(matrix[i][j].ants)-1].turn+=1			
			






