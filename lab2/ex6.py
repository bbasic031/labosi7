import json

class Employee:

    def __init__(self, name, title, age, office):
        self.name = name
        self.title = title
        self.age = age
        self.office = office
    
    def as_dict(self):
            return {'employee': self.name, 'title': self.title, 'age': self.age, 'office':self.office}

    def __str__(self):
        return f"{self.name} ({self.age}), {self.title} @ {self.office}"


class Company:

    def __init__(self, name):
        self.name = name
        self.employees = []

    def __str__(self):
        return f"{self.name} ({len(self.employees)} employees)"

    def employ(self, name, title, age, office):
        new_employee = Employee(name, title, age, office)
        self.employees.append(new_employee)

    def fire(self, name):
        for e in self.employees:
            if e.name == name:
                self.employees.remove(e)

    def load_from_json(self, path_to_json):
        f=open(path_to_json)
        data=json.load(f)
        for _ in data:
            _ = Employee(_['employee'],_['title'],_['age'],_['office'])
            self.employees.append
        f.close()
        # Loads the json from the path_to_json
        # Creates an Employee object for each json object (dictionary)
        # Adds each created Employee object to self.employees list
        pass

    def save_to_json(self, path_to_json):
        listOfEmployees=[]
        output=open("ex6-employees.json","w")
        for e in self.employees:
            x=e.as_dict()
            listOfEmployees.append(x)
        json.dump(listOfEmployees,output)
        output.close()
        # Convert every Employee from self.employees into a dictionary 
        # (use method as_dict() which you have to implement in the Employee class)
        # Build a list of employees where every employee is a dict
        # json.dump the whole list
        pass

    def print_employees(self):
        print(self.name)
        print("\n---------------\n")
        for i in range (1, len(self.employees)+1):
            print(f'{i}. {self.employees[i-1].name} ({self.employees[i-1].age}), {self.employees[i-1].title} @ {self.employees[i-1].office}')


def main():
    nike = Company("Nike")
    print(nike)

    nike.employ("Homer Simpson", "CEO", 44, "Lobby")
    nike.employ("Marge Simpson", "CTO", 33, "Lobby")
    print(nike)

    nike.fire("Homer Simpson")
    print(nike)

    # Implement load_from_json, save_to_json and print_employees methods
    # Then uncomment the implemented methods
    adidas = Company("Adidas")
    adidas.load_from_json("ex4-employees.json")
    # After loading from json, adidas should have all the employees from
    # json file
    print(adidas)
    # Print employees should now print all the employees
    adidas.print_employees()

    adidas.employ("Homer Simpson", "CEO", 44, "Lobby")
    adidas.employ("Marge Simpson", "CTO", 33, "Lobby")
    adidas.employ("Bart Simpson", "CEO", 44, "Lobby")
    adidas.employ("Lisa Simpson", "CTO", 33, "Lobby")
    print(adidas)
    adidas.print_employees()

    adidas.fire("Homer Simpson")
    adidas.fire("Marge Simpson")
    print(adidas)
    adidas.print_employees()

    # Saving employees db to a new file, the file should now have 2 more
    # employees (Bart and Lisa, since Homer and Marge were fired)
    adidas.save_to_json("ex6-employees.json")

if __name__ == "__main__":
    main()

