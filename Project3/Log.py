class Log:
	def log(self,logfile,result):
		fileX=open(logfile,'a')
		fileX.write(result+"\n")
		fileX.close()

