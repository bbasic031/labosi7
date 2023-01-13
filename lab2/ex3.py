import csv
import json
with open ('ex2-text.csv','r+',encoding="utf-8") as file1 :
    csvReader=file1.read()
employees=[]
rows=csvReader.split('\n')
for i in range(1,len(rows)):
    words=rows[i].split(',')
    x={'employee':words[0],'title':words[1],'age':words[2],'office':words[3]}
    employees.append(x)
with open('ex4-employees.json', 'w', encoding='utf-8') as f:
    json.dump(employees, f)




