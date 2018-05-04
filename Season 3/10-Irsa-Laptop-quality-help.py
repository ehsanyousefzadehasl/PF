numOfInputLines=int(input());

inputString = list();
for i in range(0, numOfInputLines):
	inputString.append(input())

# print(inputString)

flag = False;

for i in range(0, numOfInputLines):
	for j in range(i+1, numOfInputLines):
		c1=int(inputString[i].split()[0]);
		# print("cost1="+str(c1));
		q1=int(inputString[i].split()[1]);
		# print("quality1="+str(q1));
		c2=int(inputString[j].split()[0]);
		# print("cost2="+str(c2));
		q2=int(inputString[j].split()[1]);	
		# print("quality2="+str(q2));
		if(c1<=c2 and q1>=q2):
			flag = True

if(flag == True):
	print("happy irsa")
else:
	print("poor irsa")