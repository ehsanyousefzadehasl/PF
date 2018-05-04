inStr=input();
inStr=inStr.lower();

numbersList = list();
for letter in inStr:
	if(letter=='1' or letter =='2' or letter=='3'):
		numbersList.append(int(letter));

# for number in numbersList:
# 	print(number);
# 	print(type(number));

numbersList = sorted(numbersList);
#print(numbersList)

outString = '';
for number in numbersList:
	outString = outString + str(number) + '+';

if(outString[len(outString)-1] == '+'):
	outString = outString[:len(outString)-1]

print(outString)