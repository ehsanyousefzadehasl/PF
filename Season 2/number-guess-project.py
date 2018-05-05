import random;
a=1;
b=99;
flag=False;
cmpGuess = random.randint(a, b);

while(flag==False):
	print(cmpGuess);
	usrSub=input();
	if(usrSub=='k'):
		b = cmpGuess;
		cmpGuess=random.randint(a, b - 1);
	elif(usrSub=='b'):
		a = cmpGuess;
		cmpGuess=random.randint(a + 1, b);
	elif(usrSub=='d'):
		flag=True;