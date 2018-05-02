def divisorCounter(inNumber):
	#print('entered')
	iterator = 1
	numOfDivisors = 0;
	while(iterator <= inNumber):
		if(inNumber%iterator == 0):
			numOfDivisors = numOfDivisors + 1;
		iterator = iterator + 1;
	return numOfDivisors;

inNumList = list();
for iterator in range(20):
	inNumList.append(int(input()));

numOfDivisorsList = list()
for element in inNumList:
	temp = divisorCounter(element);
	numOfDivisorsList.append(temp);

maxNumOfDivisors=0;
i = 0;
maxIndex = 0;
flag = False;
for element in numOfDivisorsList:
	if(element > maxNumOfDivisors):		
		maxNumOfDivisors = element;
		maxIndex = i;
	if(element == maxNumOfDivisors and inNumList[i] > inNumList[maxIndex]):
		maxNumOfDivisors = element;
		maxIndex = i;

	i = i + 1;

print(inNumList[maxIndex], maxNumOfDivisors)