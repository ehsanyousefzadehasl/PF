import hashlib
import csv

def hash_password_hack(input_file_name, output_file_name):
    hashMapDisctionary = dict()
    nameList = list()
    passwordList = list()

    for i in range(0, 10000):
        hash_object = hashlib.sha256(str(i).encode())
        hex_dig = hash_object.hexdigest()
        hashMapDisctionary[hex_dig] = i

    with open(str(input_file_name)) as inFile:
        reader=csv.reader(inFile);
        for row in reader:
            name = row[0]
            nameList.append(name)
            hashedPassword = row[1]
            passwordList.append(hashMapDisctionary[hashedPassword])

    with open(str(output_file_name), 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        i = 0;
        for name in nameList:
            writer.writerow([name]+[passwordList[i]])
            i = i + 1

# hash_password_hack("input.csv", "output.csv")
