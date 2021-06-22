import time

class pollingAgency:
	def __init__ (self,votingRule,manipulation,targetCandidate,distance):
		self.votingRule = votingRule
		self.manipulation = manipulation
		self.targetCandidate = targetCandidate
		self.restrictedDistance = distance
		self.tieBreaking = []
		self.deviationSequence = []
		self.possiblePollTruthful = []
		self.possiblePollStrategic = []
		self.candidatesNum = 0
		self.votersNum = 0
		self.difference = 0
		#print("Polling Agency Created!")
		
	def setTieBreaking(self,tieBreakingList):
		self.tieBreaking = tieBreakingList
		
	def setDeviationSequence(self,deviationSequenceList):
		self.deviationSequence = deviationSequenceList
		
	def setInitialPollTruthful(self,candidateList,voterList):
		PollTruthful = []
		for i in range(0,len(candidateList)):
			PollTruthful.append(0)
		for i in range(0,len(voterList)):
			index = voterList[i].ballotTruthful
			PollTruthful[index-1] += 1
			
		if self.difference <= 4000:
			for i in range(0,len(candidateList)):
				PollTruthfulCopy = PollTruthful.copy()
				self.possiblePollTruthful.append(PollTruthfulCopy)	
			
		print("Initial truthful poll is :",self.possiblePollTruthful[0])
	
	def setInitialPollStrategic(self,candidateList,voterList):
		PollStrategic = []
		for i in range(0,len(candidateList)):
			PollStrategic.append(0)
			
		for i in range(0,len(voterList)):
			temp = []
			for count in range(0,len(candidateList)):
				temp.append(0)
				
			if len(voterList[i].network) == 0:
				continue
			else:
				for j in range(0,len(voterList[i].network)):
					index = voterList[voterList[i].network[j]].ballotTruthful
					temp[index-1] += 1
				for k in range(0,len(candidateList)):
					if PollStrategic[k] < temp[k]:
						PollStrategic[k] = temp[k]
						
		difference = self.votersNum - sum(PollStrategic)
		self.difference = difference
		
		print("Difference is :",difference)
		print("Initial strategic poll is :",PollStrategic)
		
		if self.difference <= 10:
			for i in range(0,len(candidateList)):
				PollStrategicCopy = PollStrategic.copy()
				PollStrategicCopy[i] += difference
				self.possiblePollStrategic.append(PollStrategicCopy)
		elif self.difference > 10:
			for i in range(0,len(candidateList)):
				PollStrategicCopy = PollStrategic.copy()
				PollStrategicCopy[i] += difference
				self.possiblePollStrategic.append(PollStrategicCopy)
		
	def tryPollStrategic(self,increment,decrement,index):
		tempPollStrategic = self.possiblePollStrategic[index].copy()
		tempPollStrategic[increment-1] += 1
		tempPollStrategic[decrement-1] -= 1
		return tempPollStrategic
		
	def updatePoll(self,increment,decrement,index):
		self.possiblePollStrategic[index][increment-1] += 1
		self.possiblePollStrategic[index][decrement-1] -= 1
		self.possiblePollTruthful[index][increment-1] += 1
		self.possiblePollTruthful[index][decrement-1] -= 1
		#print("Strategic poll :",self.possiblePollStrategic[index])
		#print("Truthful poll  :",self.possiblePollTruthful[index])
		
	def setNum(self,candidatesNum,votersNum):
		self.candidatesNum = candidatesNum
		self.votersNum = votersNum
		
	def realWinnerDetermination(self,candidateList):
		successCount = 0
		guessCount = 2
		if self.votingRule == "Plurality":
			for k in range(0,len(candidateList)):
				index = 0
				max = self.possiblePollTruthful[k][0]
				for i in range(1,len(self.possiblePollTruthful[k])):
					if self.possiblePollTruthful[k][i] > max:
						max = self.possiblePollTruthful[k][i]
						index = i 
					elif self.possiblePollTruthful[k][i] == max:
						index1 = self.tieBreaking.index(index+1)
						index2 = self.tieBreaking.index(i+1)
						if index2 < index1:
							max = self.possiblePollTruthful[k][i]
							index = i
				if (candidateList[index].candidateID == self.targetCandidate) and self.manipulation == "Constructive":
					successCount += 1
					print("Winner ID :",candidateList[index].candidateID," Manipulation succeeds.")
				elif (candidateList[index].candidateID == self.targetCandidate) and self.manipulation == "Destructive":
					print("Winner ID :",candidateList[index].candidateID," Manipulation fails.")
				elif (candidateList[index].candidateID != self.targetCandidate) and self.manipulation == "Constructive":
					print("Winner ID :",candidateList[index].candidateID," Manipulation fails.")
				elif (candidateList[index].candidateID != self.targetCandidate) and self.manipulation == "Destructive":
					successCount += 1
					print("Winner ID :",candidateList[index].candidateID," Manipulation succeeds.")
			print("...")
			print("Manipulation success count : ", successCount * guessCount)
			print("Manipulation success probability :",successCount * guessCount/(len(candidateList)*50))
			
		elif self.votingRule == "Veto":
			for k in range(0,len(candidateList)):
				index = 0
				min = self.possiblePollTruthful[k][0]
				for i in range(1,len(self.possiblePollTruthful[k])):
					if self.possiblePollTruthful[k][i] < min:
						min = self.possiblePollTruthful[k][i]
						index = i 
					elif self.possiblePollTruthful[k][i] == min:
						index1 = self.tieBreaking.index(index+1)
						index2 = self.tieBreaking.index(i+1)
						if index2 < index1:
							min = self.possiblePollTruthful[k][i]
							index = i
				if (candidateList[index].candidateID == self.targetCandidate) and self.manipulation == "Constructive":
					successCount += 1
					print("Winner ID :",candidateList[index].candidateID," Manipulation succeeds.")
				elif (candidateList[index].candidateID == self.targetCandidate) and self.manipulation == "Destructive":
					print("Winner ID :",candidateList[index].candidateID," Manipulation fails.")
				elif (candidateList[index].candidateID != self.targetCandidate) and self.manipulation == "Constructive":
					print("Winner ID :",candidateList[index].candidateID," Manipulation fails.")
				elif (candidateList[index].candidateID != self.targetCandidate) and self.manipulation == "Destructive":
					successCount += 1
					print("Winner ID :",candidateList[index].candidateID," Manipulation succeeds.")
				time.sleep(1)
			print("...")
			print("Manipulation success count : ", successCount * guessCount)
			print("Manipulation success probability :",successCount * guessCount/(len(candidateList)*50))
			
			
	def fakeWinnerDetermination(self,candidateList,PollStrategic):
		if self.votingRule == "Plurality":
			index = 0
			max = PollStrategic[0]
			for i in range(1,len(PollStrategic)):
				if PollStrategic[i] > max:
					max = PollStrategic[i]
					index = i 
				elif PollStrategic[i] == max:
					index1 = self.tieBreaking.index(index+1)
					index2 = self.tieBreaking.index(i+1)
					if index2 < index1:
						max = PollStrategic[i]
						index = i
			return candidateList[index].candidateID
			
		elif self.votingRule == "Veto":
			index = 0
			min = PollStrategic[0]
			for i in range(1,len(PollStrategic)):
				if PollStrategic[i] < min:
					min = PollStrategic[i]
					index = i 
				elif PollStrategic[i] == min:
					index1 = self.tieBreaking.index(index+1)
					index2 = self.tieBreaking.index(i+1)
					if index2 < index1:
						min = PollStrategic[i]
						index = i
			return candidateList[index].candidateID
			
	def manipulate(self,candidateList,voterList):
		for k in range (0,len(candidateList)):
			print("Manipulation round :",k)
			time.sleep(1)
			for i in range(0,len(self.deviationSequence)):
				index = self.deviationSequence[i]-1
				voterList[index].deviateBallot(self,candidateList,k)
		print("...")
		time.sleep(10)
		print("   ")
		print("Total round :",len(candidateList)*50)
		print("----------------------")
				
			
class candidate:
	def __init__(self,ID):
		self.candidateID = ID
		#print("Candidate Created! ID:",self.candidateID)
	
class voter:
	def __init__(self,ID,distance):
		self.voterID = ID
		self.restrictedDistance = distance
		self.preference = []
		self.network = []
		self.ballotTruthful = 0
		self.ballotStrategic = 0
		#print("Voter Created! ID:",self.voterID)

	def setPreference(self,preferenceList):
		self.preference = preferenceList
		
	def setConnection(self,neighbour):
		self.network.append(neighbour)
		
	def setTruthfulBallot(self,votingRule):
		self.votingRule = votingRule
		if votingRule == "Plurality":
			self.ballotTruthful = self.preference[0]
		elif votingRule == "Veto":
			self.ballotTruthful = self.preference[-1]
			
	def deviateBallot(self,pollingAgency,candidateList,index):
		if self.votingRule == "Plurality":
			if self.preference[0] == pollingAgency.fakeWinnerDetermination(candidateList,pollingAgency.possiblePollStrategic[index]):
				pass
			else:
				increment = pollingAgency.fakeWinnerDetermination(candidateList,pollingAgency.possiblePollStrategic[index])
				decrement = self.preference[0]
				for i in range(0,len(pollingAgency.possiblePollStrategic)):
					tempPollStrategic = pollingAgency.tryPollStrategic(increment,decrement,i)
					if self.preference[-1] == pollingAgency.fakeWinnerDetermination(candidateList,tempPollStrategic):
						pass
					else:
						pollingAgency.updatePoll(increment,decrement,index)
				
		elif self.votingRule == "Veto":
			if self.preference[0] == pollingAgency.fakeWinnerDetermination(candidateList,pollingAgency.possiblePollStrategic[index]):
				pass
			else:
				increment = pollingAgency.fakeWinnerDetermination(candidateList,pollingAgency.possiblePollStrategic[index])
				decrement = self.preference[-1]
				for i in range(0,len(pollingAgency.possiblePollStrategic)):
					tempPollStrategic = pollingAgency.tryPollStrategic(increment,decrement,i)
					if self.preference[-1] == pollingAgency.fakeWinnerDetermination(candidateList,tempPollStrategic):
						pass
					else:
						pollingAgency.updatePoll(increment,decrement,index)

