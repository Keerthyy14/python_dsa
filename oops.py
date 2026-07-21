# 4 pillars of oops
# Encapsulation
#access modifiers

# class A:
#     def __init__(self,name,age,gender):#constructor
#         self.__name=name
#         self._age=age
#         self.gender=gender#public variable can be accessed inside of same class and outside of all classes which defines with no prefix
#     def display(self):
#         print(self.__name)
#         print(self._age)
#         print(self.gender)
#     def setAge(self,age):
#         self._age=age
#     def getAge(self):
#         return self._age
# a1=A("Keerthi",21,"female")
# a2=A("kavya",21,"female")

# #print(a1.gender) #public variable can be acessed
# #print(a2.gender) #public variable can be acessed
# print(a1.display())
# a1.setAge(19)
# print(a2.display())
# print(a2.gender)


#Abstraction
# from abc import ABC,abstractmethod
# class BankAccount(ABC):
#     def __init__(self,balance):
#         self.__balance=balance
#     def deposit(self,amount):
#         self.__balance+=amount
#     def withdraw(self,amount):
#         self.__balance-=amount
#     def getBalance(self):
#         return self.__balance
#     @abstractmethod
#     def interestcalc(self):
#         pass
# class SavingsAccount(BankAccount):
#     def interestcalc(self):
#         return self.getBalance()*0.05
# a=SavingsAccount(5000)
# print(a.getBalance())
# a.withdraw(500)
# print(a.getBalance())
# print(a.interestcalc())

#Inheritance
#Polymorphism
# class Animal:
#     print("Animal Sound")
# class Dog(Animal):
#     def sound(self):
#         print("Woof")
# class Cat(Animal):
#     def sound(self):
#         print("Meow")
# a=Cat()
# b=Dog()
# print(a.sound())
# print(b.sound())