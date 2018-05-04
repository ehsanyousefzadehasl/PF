
inputString = input();
charsList = inputString.split();

inputList = list(map(int, charsList))

# for el in inputList:
# 	print(el);


average = (inputList[0]+inputList[1]+inputList[2])/3;

distance1 = abs(average - inputList[0]);
distance2 = abs(average - inputList[1]);
distance3 = abs(average - inputList[2]);

minimumDistance = distance1 + distance2 + distance3;

minimumDistance=str(minimumDistance);
if(minimumDistance[-2:] == '.0'):
	minimumDistance=minimumDistance[:-2];

print(minimumDistance);