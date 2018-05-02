inNum=input();
iterator = 2;
numOfDivisors = 0;
while(iterator <= int(inNum)/2):
	if(int(inNum)%iterator == 0):
		numOfDivisors = numOfDivisors + 1;
	iterator = iterator + 1;
if(numOfDivisors > 0):
	print("not prime");
else:
	print("prime");
