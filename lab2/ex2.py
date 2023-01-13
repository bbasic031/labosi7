import csv
with open ('ex2-text.csv',encoding="utf-8") as file1 :
    csvReader=csv.reader(file1)
    lineCount=0
    file2=open('ex2-employees.txt','w')
    file3=open('ex2-locations.txt','w')
    for row in csvReader:
        if lineCount==0:
            file2.write(f'Column names: {row[0]}, {row[1]}\n')
            file3.write(f'Column names: {row[0]}, {row[3]}\n')
            lineCount+=1;
        else:
            file2.write(f'{row[0]}, {row[1]}\n')
            file3.write(f'{row[0]}, {row[3]}\n')
            lineCount+=1
