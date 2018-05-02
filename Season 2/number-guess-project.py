import random;
a=0;
b=100;
flag=False;
cmpGuess = random.randint(a, b);

while(flag==False):
	print(cmpGuess);
	usrSub=input();
	if(usrSub=='k'):
		b = cmpGuess;
		cmpGuess=random.randint(a, b);
	elif(usrSub=='b'):
		a = cmpGuess;
		cmpGuess=random.randint(a, b);
	elif(usrSub=='d'):
		flag=True;