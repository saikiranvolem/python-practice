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
# without Encapsulation
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

# b = Bank()
# b.balance = 0
# b.show_balance()

# with encapsulation
# class Bank:
#     def __init__(self):
#         self.__balance = 1000  # private variable
    
#     def show_balance(self):
#         print("Balance:", self.__balance)
        
#     def deposit(self, amount):
#         self.__balance += amount
#         print("Deposited:", amount)
        
#     def withdraw(self, amount):
#         self.__balance -= amount
#         print("Withdrawn:", amount)
        
# b = Bank()
# b.deposit(500)
# b.withdraw(800)
# b.__balance = 0
# b.show_balance()
# -------------------------------------
# with inheritance
# class Empolyee:
#     def work(self):
#         print("Employee is working")
# class Manager(Empolyee):
#     def manage(self):
#         print("Manager is managing")
# class Developer(Empolyee):
#     def develop(self):
#         print("Developer is developing")

# m = Manager()
# m.work()
# m.manage()
# print("\n")
# d = Developer()
# d.work()
# d.develop()
# -------------------------------------
# Without Polymorphism
# class Employee:
#     def work(self):
#         print("Employee is working")
# class Developer(Employee):
#     def work(self):
#         print("Developer is developing")
# class Tester(Employee):
#     def work(self):
#         print("Tester is testing")
        
# d = Developer()
# d.work()
# print("\n")
# t = Tester()
# t.work()

# with Polymorphism
# class Employee:
#     def work(self):
#         print("Employee is working")
# class Developer(Employee):
#     def execute(self):
#         super().work()
#     def work(self):
#         print("Developer is developing")
# class Tester(Employee):
#     def execute(self):
#         super().work()
#     def work(self):
#         print("Tester is testing")

# d = Developer()
# d.execute()
# d.work()
# print("\n")
# t = Tester()
# t.execute()
# t.work()
# -------------------------------------
# Abstraction
# from abc import ABC, abstractmethod
# class ATM(ABC):
#     @abstractmethod
#     def withdraw(self):
#         pass
# class SBI(ATM):
#     def withdraw(self):
#         print("SBI: Withdrawn")
# class HDFC(ATM):
#     def withdraw(self):
#         print("HDFC: Withdrawn")
# atm1 = SBI()
# atm2 = HDFC()
# atm1.withdraw()
# atm2.withdraw()