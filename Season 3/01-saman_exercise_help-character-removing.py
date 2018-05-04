inStr=input();
inStr = inStr.lower();
i = 0;

inStr = inStr.replace("a", "")
inStr = inStr.replace("e", "")
inStr = inStr.replace("i", "")
inStr = inStr.replace("u", "")
inStr = inStr.replace("o", "")

#print(inStr)
if(inStr[0] != '.'):
	inStr = '.' + inStr;

#print(inStr)

indexes = list();
i = len(inStr);
while(i != 1):
	if(inStr[i-2] != '.' and inStr[i-1] != '.'):
		indexes.append(i-1);
	i = i - 1;


for i in indexes:
	inStr = inStr[:i] + '.' + inStr[i:];


print(inStr);