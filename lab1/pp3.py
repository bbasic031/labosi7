from cgi import print_arguments
from re import X


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if i<5:
        print(i)

x=[]
for i in a:
    if i<5:
        x.append(i)
print(x)

y=[]
y=[y.append(i) for i in a if i<5]
print(y)

nums=input("Unesi brojeve: ")
nums=[int(x) for x in nums.split(',')]
print(nums)

