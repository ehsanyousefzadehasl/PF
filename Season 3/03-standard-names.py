inStrsList=list();
for i in range(10):
	inStrsList.append(input().lower());

# for str in inStrsList:
# 	print(str)

for i in range(10):
	char = inStrsList[i][0];
	remain = inStrsList[i][1:];
	inStrsList[i] = char.upper() + remain;


for str in inStrsList:
	print(str)	