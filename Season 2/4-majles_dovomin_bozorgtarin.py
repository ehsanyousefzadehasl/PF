flag=False;
firstMaxAge=0;
secondMaxAge=0;
ageList = list()
while(flag == False):
	candidAge=int(input());
	ageList.append(candidAge);
	if(candidAge==-1):
		flag=True;

for element in ageList:
	#print(element)
	if(element > firstMaxAge):
		firstMaxAge = element;

for element in ageList:
	if(element > secondMaxAge and element < firstMaxAge):
		secondMaxAge = element;
#print(ageList);
print(firstMaxAge, secondMaxAge);