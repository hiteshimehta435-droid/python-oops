while True:
    print("\n---OOP Wrapper---")
    print("1. person Data")
    print("2. Employee Data")
    print("3. Manager Data")
    print("4. Developer Data")
    print("5. Method overloading")
    print("6. Exit")

    option = int(input("Enter your option: "))

    if option == 1:
        print("\n---person Data---")
        class user:
            def __init__(self, name, age):
                self.name = name
                self.age = age

            def display(self):
                print("Name:", self.name)
                print("Age:", self.age)

        User = user("park jimin", 29)
        User.display()

    elif option == 2:
        print("\n---Employee Data---")
        class person:
            def __init__(self, id, name, age):
                self.id = id
                self.name = name
                self.age = age

        class Employee(person):
            def __init__(self, id, name, age, salary):
                super().__init__(id ,name, age)
                self.salary = salary

            def display(self):
                print("ID:", self.id)
                print("Name:", self.name)
                print("Age:", self.age)
                print("Salary:", self.salary)

        e = Employee(101, "kim seok-jin", 30, 100000)
        e.display()
    
    elif option == 3:
        print("\n---Manager Data---")
        class Employee:
            def __init__(self, id, name, deparment):
                self.id = id
                self.name = name
                self.deparment = deparment

        class Manager(Employee):
            def __init__(self, id, name, deparment, salary):
                super().__init__(id, name, deparment)
                self.salary = salary

            def display(self):
                print("ID:", self.id)
                print("Name:", self.name)
                print("Deparment:", self.deparment)
                print("Salary:", self.salary)

        m = Manager(102, "Jung Ho-seok", "Finance", 5000000)
        m.display()

    elif option == 4:
        print("\n---Developer Data---")
        class Employee:
            def __init__(self, id, name, programming_language_name):
                self.id = id
                self.name = name
                self.programming_language_name = programming_language_name

        class Developer(Employee):
            def __init__(self, id, name, programming_language_name, salary):
                super().__init__(id, name, programming_language_name)
                self.salary = salary

            def display(self):
                print("ID:", self.id)
                print("Name:", self.name)
                print("Programming language name:", self.programming_language_name)
                print("Salary:", self.salary)

        d = Developer(103, "Jeon Jung-kook", "Python", 9000000)
        d.display()

    elif option == 5:
        print("\n---Method overloading---")
        class Method_overloading:
            def add(self, a, b, c):
                return a + b + c

        m = Method_overloading()
        print("Total:",(m.add(100000, 5000000, 9000000)))

    elif option == 6:
         print("\n--Exit--")
         print("Thank you for ues my project.")
         print("Good bye! , Have nice day.")

    else:
        print("Invaild option")
        break

    
