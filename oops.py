# creating a class and object

# class Car:
#     name = "volvo"
#     color = "red"
    
# c1 = Car()
# print(c1.name)
# print(c1.color)
# ------------------------------------

# creating functions in class

# class Student:
#     def studentDetails(self):
#         print("This is a student details function")

# s1 = Student()
# s1.studentDetails()

# class Student:
#     def studentDetails(self, name, age):
#         print(name, age)
# s1 = Student()
# s1.studentDetails("John", 20)
# ------------------------------------
# self real usage

# class Car:
#     name = "volvo"
#     color = "red"
#     def speed(self):
#         print(self.name, self.color)
#         print("200kph")
# c1 = Car()
# c1.speed()
# c1 --> {name: "volvo", color: "red", speed(): print("200kph")}
# ------------------------------------
# __init__ Constructor

# class Car:
#     name = "BMW"
#     color = "Black"
#     def __init__(self):
#         print(self.name, self.color)
#         print("200kph")
# c1 = Car()

# class Car:
#     name = "BMW"
#     color = "Black"
#     def __init__(self):
#         print(self.name, self.color)
#         print("200kph")
        
#     def speed(self):
#         print("Speed is 200kph")

# c1 = Car()
# c1.speed()
# ------------------------------------
# passing arguments to init constructor

# class Car:
#     wheels = 4
#     def __init__(self, name, speed):
#         self.name = name
#         self.speed = speed
        
#     def carDetails(self):
#         print(self.name, self.speed, self.wheels)
        
# c1 = Car("BMW", 200)
# c1.carDetails()

# print("\n")

# c2 = Car("Volvo", 250)
# c2.carDetails()
# --------------------------------------------------
# Encapsulation
# class Bank:
#     def __init__(self):
#         self.balance = 1000
    
#     def show_balance(self):
#         print("Balance:", self.balance)
        
# b = Bank()
# b.show_balance()

# class Bank:
#     def __init__(self):
#         self.balance = 1000
#     def show_balance(self):
#         print("Balance:", self.balance)
#     def deposit(self, amount):
#         self.balance += amount
#         print("Deposited:", amount)

# b = Bank()
# b.show_balance()
# b.deposit(500)
# b.show_balance()