flag=False;
maxAge=0;
while(flag == False):
	candidAge=int(input());
	if(candidAge==-1):
		flag=True;
	if(candidAge > maxAge):
		maxAge = candidAge;
print(maxAge);