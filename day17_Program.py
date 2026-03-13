#1. Public Variable
class Student:
    def __init__(self, name):
        self.name = name

s = Student("Diksha")

print(s.name)

#2. Protected Variable(_)
class Student:
    def __init__(self, name):
        self._name = name

s = Student("Diksha")

print(s._name)

#3. Private Variable(__)
class Student:
    def __init__(self, name):
        self.__name = name

s = Student("Diksha")

print(s._Student__name)

#4. Getter Method
class Student:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
    
s = Student("Diksha")

print(s.get_name())


#5.Setter Method
class Student:
    def __init__(self, name):
        self.__name = name

    def set_name(self, new_name):
        self.__name = new_name

    def get_name(self):
        return self.__name
    
s = Student("Diksha")

s.set_name("Riya")

print(s.get_name())


#6. Mini Project: Bank Account
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


account = BankAccount(1000)

account.deposit(500)

print("Balance:", account.get_balance())