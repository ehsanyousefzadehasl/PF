import math;

def truncate(f, n):
    return math.floor(f*10**n)/10**n;


numOfNumbers = int(input());
inputNumbers = list();
for i in range(0, numOfNumbers):
    temp = int(input());
    inputNumbers.append(temp);

outNumbers = list();
i = 0;
for num in inputNumbers:
    outNumbers.append(math.sqrt(inputNumbers[i]));
    i = i + 1;

for num in outNumbers:
    #print("%.4f"%num);
    #print(num);
    tmp = str(num).split('.');
    a = tmp[0];
    b = tmp[1];
    #print(a);
    #print(b[0:4])
    outNumber = float(a+"."+b[0:4]);
    print("%.4f"%outNumber);
