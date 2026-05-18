import csv
with open("students.csv",'r') as file:
    reader=csv.reader(file)
    print('\nReading from student file:\n')
    for row in reader:
        print(f"{row[0]:<10} {row[1]:<15} {row[2]:<10}")