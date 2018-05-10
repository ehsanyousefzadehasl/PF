import csv
from statistics import mean

with open('grades.csv') as f:
    reader=csv.reader(f);
    #print("This is File Handler :) --> " + str(reader))
    for row in reader:
        #print(row);
        #print(type(row)) -> its type is list
        name = row[0];
        gradesList = list();
        for grade in row[1:]:
            gradesList.append(float(grade));
        print("%s: %1.0f"%(name,mean(gradesList)))
