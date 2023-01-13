name=input("Unesi ime: ")
age=input("Unesi godine: ")

count=int(input("Upisi koliko puta zelis vidjeti proslu poruku: \n"))

age100=100-int(age)+2022
for i in range(count):
    print(f"Bok {name}, imat ces 100 {age100}. godine")
