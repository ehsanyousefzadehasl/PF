inStr=input().lower();

flag = False;

if("ab" in inStr):
	inStr=inStr.replace("ab", '')
	flag = True;
else:
	flag = False;

if("ba" in inStr):
	inStr=inStr.replace("ba", '')
	flag = True;
else:
	flag = False;

if(flag == True):
	print('YES')
else:
	print('NO')
