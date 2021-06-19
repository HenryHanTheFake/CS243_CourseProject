import manip as m
import time

def main():
	
	initializationFile = open("initialization\initialization1.txt")
	preferenceFile = open("preference\preference1.txt")	
	connectionFile = open("connection\connection1.txt")
	
	candidateList = []
	voterList = []
	
	print("                                                                     ")
	print("--------------------- CS243 AGT Course Project ----------------------")
	print("                                                                     ")
	print("-------------------- Poll Manipulation Simulator --------------------")
	print("                                                                     ")
	
	print("------------------- Simulation Enviroment Setting -------------------")
	for i in range(0,7):
		initializationLine = initializationFile.readline()
		initializationLine = initializationLine.strip("\n").split(" ")
		if i == 0:
			votingRule = initializationLine[0]
			print("Voting rule is :",votingRule)
		elif i == 1:
			manipulation = initializationLine[0]
			print("Manipulation goal is :",manipulation)
		elif i == 2:
			initializationLine = list(map(int,initializationLine))
			numCandidates = initializationLine[0]
			print("Number of candidates :",numCandidates)
		elif i == 3:
			initializationLine = list(map(int,initializationLine))
			numVoters = initializationLine[0]
			print("Number of voters :",numVoters)
		elif i == 4:
			initializationLine = list(map(int,initializationLine))
			targetCandidate = initializationLine[0]
			print("The ID of target candidate :",targetCandidate)
		elif i == 5:
			initializationLine = list(map(int,initializationLine))
			pollDistance = initializationLine[0]
			print("The restricted distance of poll :",pollDistance)
		elif i == 6:
			initializationLine = list(map(int,initializationLine))
			voterDistance = initializationLine[0]
			print("The restricted distance of voter :",voterDistance)
	print("                                                                     ")		
	time.sleep(1)
	
	print("-------------------------- Initialization ---------------------------")
	print("Create ",numCandidates," Candidates.")
	print("Creating...")
	for i in range(0,numCandidates):
		candidateList.append(m.candidate(i+1))
	print("Success.")
	print("------------------------------------")
	time.sleep(1)
	
	print("Create ",numVoters," Voters.")
	print("Creating...")
	for i in range(0,numVoters):
		voter = m.voter(i,voterDistance)
		
		preferenceLine = preferenceFile.readline()
		preferenceLine = preferenceLine.strip("\n").split(" ")
		voter.setPreference(list(map(int,preferenceLine)))
		
		connectionLine = connectionFile.readline()
		connectionLine = connectionLine.strip("\n").split(" ")
		connectionLine = list(map(int,connectionLine))
		
		for j in range(0,len(connectionLine)):
			if connectionLine[0] != -1:
				voter.setConnection(connectionLine[j])
			else:
				pass
		voter.setTruthfulBallot(votingRule)
		voterList.append(voter)
	print("Success.")
	print("------------------------------------")	
	time.sleep(1)
	
	print("Create Polling Agency.")
	print("Creating...")
	pollingAgencyInstance = m.pollingAgency(votingRule,manipulation,targetCandidate,pollDistance)
	print("Success.")
	time.sleep(1)
	
	print("                                                                     ")
	print("--------------------------- Manipulation ----------------------------")
	print("Manipulation Starts.")
	print("--------------------")
	time.sleep(1)
	pollingAgencyInstance.setNum(len(candidateList),len(voterList))
	pollingAgencyInstance.setTieBreaking([3,2,1,4])
	pollingAgencyInstance.setDeviationSequence([4,3,2,1,5,6,7,8,9,10])
	pollingAgencyInstance.setInitialPollStrategic(candidateList,voterList)	
	pollingAgencyInstance.setInitialPollTruthful(candidateList,voterList)
	pollingAgencyInstance.manipulate(candidateList,voterList)
	pollingAgencyInstance.realWinnerDetermination(candidateList)
	print("------------------")
	print("Manipulation Ends.")
	print("---------------------------------------------------------------------")
	
if __name__ == '__main__':
	main()
	
	