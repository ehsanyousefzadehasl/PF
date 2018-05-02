usrAge=input();
if(int(usrAge)>0 and int(usrAge)<6):
	print("khordsal");
elif(int(usrAge)>=6 and int(usrAge)<10):
	print("koodak");
elif(int(usrAge)>=10 and int(usrAge)<14):
	print("nojavan");
elif(int(usrAge)>=14 and int(usrAge)<24):
	print("javan");
elif(int(usrAge)>=24 and int(usrAge)<40):
	print("bozorgsal");
else:
	print("miansal");