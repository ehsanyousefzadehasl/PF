def characterRemover(inStr ,inChar):
	i = 100;
	while(i > 0):
		inStr = inStr.replace(inChar*i, inChar);
		i = i - 1;
	return inStr;
 # --------------------------------------------------

def numOfLs(inStr):
	num = 0;
	for letter in inStr:
		if(letter == 'l'):
			num = num + 1;
	return num;

# ---------------------------------------------------

inStr=input().lower();

i = 0;
for letter in inStr:
	if(letter != 'h' and letter != 'e' and letter != 'l' and letter != 'o'):
		inStr = inStr[:i] + ' ' + inStr[i+1:];
	i = i + 1;

inStr = inStr.replace(' ', '')

numOfLs = numOfLs(inStr);

inStr = characterRemover(inStr, 'h');
inStr = characterRemover(inStr, 'e');
inStr = characterRemover(inStr, 'l');
inStr = characterRemover(inStr, 'o');


if(inStr == 'helo' and numOfLs > 0):
	print('YES')
else:
	print('NO')