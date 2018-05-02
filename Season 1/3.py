inputNum=input();
yekan=int(inputNum) % 10;
dahgan=(int(inputNum)//10)%10;
sadgan=int(inputNum)//100;

reverseNum=str(yekan)+''+str(dahgan)+''+str(sadgan);
doubleReverseNum=int(reverseNum)*2;
print(doubleReverseNum);