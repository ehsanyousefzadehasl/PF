inputNum = int(input());
inputString = input();
charsList = inputString.split();

numbersList = list(map(int, charsList))

# print(numbersList);
# for el in numbersList:
# 	print(el)
playersList=list()
for element in numbersList:
	if(element <= 2):
		playersList.append(element);

print(len(playersList)//3)