totalScore=0;
numOfWins=0;
for iterator in range(30):
	inScore = int(input());
	totalScore = totalScore + inScore;
	if(inScore == 3):
		numOfWins = numOfWins + 1;

print(totalScore, numOfWins);