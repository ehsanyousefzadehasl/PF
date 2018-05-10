import csv
from statistics import mean
import operator
# -------------------------------------------------------------------
# method which calculates the average of each student
# -------------------------------------------------------------------
def calculate_averages(input_file_name, output_file_name):
    nameList = list();
    averageList = list();

    with open(str(input_file_name)) as inFile:
        reader=csv.reader(inFile);

        for row in reader:
            name = row[0];
            nameList.append(name)
            gradesList = list();
            for grade in row[1:]:
                gradesList.append(float(grade));
            averageList.append(mean(gradesList));

    with open(str(output_file_name), 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        i = 0
        for name in nameList:
            #print(name + str(averageList[i]))
            writer.writerow([name]+[averageList[i]])
            i = i + 1
# ---------------------------------------------------------------------
#  method which calculates the average for each student and sorts it
# ---------------------------------------------------------------------
def calculate_sorted_averages(input_file_name, output_file_name):
    nameList = list();
    averageList = list();

    with open(str(input_file_name)) as inFile:
        reader=csv.reader(inFile);

        for row in reader:
            name = row[0];
            nameList.append(name)
            gradesList = list();
            for grade in row[1:]:
                gradesList.append(float(grade));
            averageList.append(mean(gradesList));
    i = 0
    nameAvgDict = dict();
    for average in averageList:
        nameAvgDict[nameList[i]] = average
        i = i + 1

    sortedNameAvgDict = sorted(nameAvgDict.items(), key=operator.itemgetter(1))
    # print(sortedNameAvgDict)
    with open(str(output_file_name), 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for key in sortedNameAvgDict:
            writer.writerow([key[0]]+[key[1]])
# --------------------------------------------------------------------
# method which calculates and 3 worst average to out file
# --------------------------------------------------------------------
def calculate_three_worst(input_file_name, output_file_name):
    nameList = list();
    averageList = list();

    with open(str(input_file_name)) as inFile:
        reader=csv.reader(inFile);

        for row in reader:
            name = row[0];
            nameList.append(name)
            gradesList = list();
            for grade in row[1:]:
                gradesList.append(float(grade));
            averageList.append(mean(gradesList));
    i = 0
    nameAvgDict = dict();
    for average in averageList:
        nameAvgDict[nameList[i]] = average
        i = i + 1

    sortedNameAvgDict = sorted(nameAvgDict.items(), key=operator.itemgetter(1))
    # print(sortedNameAvgDict)
    with open(str(output_file_name), 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        i = 0
        for key in sortedNameAvgDict:
            writer.writerow([key[1]])
            if(i == 2):
                break
            i = i + 1
# -------------------------------------------------------------------
# method which calculates and write 3 first students with average to file
# -------------------------------------------------------------------
def calculate_three_best(input_file_name, output_file_name):
    nameList = list();
    averageList = list();

    with open(str(input_file_name)) as inFile:
        reader=csv.reader(inFile);

        for row in reader:
            name = row[0];
            nameList.append(name)
            gradesList = list();
            for grade in row[1:]:
                gradesList.append(float(grade));
            averageList.append(mean(gradesList));
    i = 0
    nameAvgDict = dict();
    for average in averageList:
        nameAvgDict[nameList[i]] = average
        i = i + 1

    sortedNameAvgDict = sorted(nameAvgDict.items(), key=operator.itemgetter(1))
    # print(sortedNameAvgDict)
    with open(str(output_file_name), 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        j = len(sortedNameAvgDict) - 1
        i = 0
        for key in sortedNameAvgDict:
            writer.writerow([sortedNameAvgDict[j][0]]+[sortedNameAvgDict[j][1]])
            j = j - 1
            if(i == 2):
                break
            i = i + 1
def calculate_average_of_averages(input_file_name, output_file_name):
    nameList = list();
    averageList = list();

    with open(str(input_file_name)) as inFile:
        reader=csv.reader(inFile);

        for row in reader:
            name = row[0];
            nameList.append(name)
            gradesList = list();
            for grade in row[1:]:
                gradesList.append(float(grade));
            averageList.append(mean(gradesList));
    totalAverage = mean(averageList)
    # print(totalAverage)
    with open(str(output_file_name), 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([totalAverage])
# infile = 'grades.csv'
# outfile = 'nameAverage.csv'
# calculate_averages(infile, outfile);
# calculate_sorted_averages(infile, outfile);
# calculate_three_worst(infile, outfile)
# calculate_three_best(infile, outfile)
# calculate_average_of_averages(infile, outfile)
