import csv

with open("students.csv","w",newline="") as file:
    writer=csv.writer(file)
    writer.writerow(["Roll No","Name","Marks"])
    data=[
        [101,"Parnika",95],
        [102,"Rahul",88],
        [103,"Ananya",91],
        [104,"Amit",76],
        [105,"Sneha",84],
        [106,"Rohan",90],
        [107,"Priya",87],
        [108,"Karan",79],
        [109,"Neha",93],
        [110,"Arjun",85]
    ]
    writer.writerows(data)

print("10 records stored successfully in students.csv")