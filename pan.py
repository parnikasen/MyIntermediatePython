import pandas as pd
name=[]
age=[]
marks=[]
n=int(input())
for i in range(n):
    data=input().split()
    name.append(data[0])
    age.append(int(data[1]))
    marks.append(int(data[2]))
df=pd.DataFrame({'Name': name, 'Age': age, 'Marks': marks})
df=df[df['Marks'>=80]]
print(df[['Name', 'Marks']].to_string(index=False))