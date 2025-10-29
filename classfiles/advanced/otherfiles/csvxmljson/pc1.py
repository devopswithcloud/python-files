import csv

data =[
    ['Name','Age','City'],
    ['Jobe',26,'Hyd'],
    ['Alice',30,'tg']
]
with open('data.csv',mode='w') as file:
    writer =csv.writer(file)
    writer.writerows(data)


#reading csv file
with open('data.csv',mode ='r')as file:
    reader = csv.reader(file)
    for row in reader:
        print(row) # each row is list of strings

with open('data.csv',mode='r') as file:
    reader =csv.DictReader(file)
    for row in reader:
        print(row['Name'],row['Age']) # access columns by header

data1 =[
    {'Name':'John','Age':25,'City':'New yorok'}
]
with open('output.csv',mode='w') as file:
    fieldnames =['Name','Age','City']
    writer =csv.DictWriter(file,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data1)