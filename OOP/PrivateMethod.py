# Private Attribute
class Account:
    def __init__(self, account_number, account_password):
        self.account_number = account_number # __ private
        self.__account_password = account_password

    def recover_pass(self):
        return self.__account_password
a1 = Account(1234,'xyz')
print(a1.recover_pass()) # Output: xyz

class Account:
    def __init__(self, account_number, account_password):
        self.account_number = account_number # __ private
        self.account_password = account_password

    def recover_pass(self):
        return self.__account_password
a1 = Account(1234,'xyz')
del a1
print(a1.recover_pass()) # Output: xyz

class Person:
    __name = 'xyz'

    def __hello(self):
        print('hello person')

    def welcome(self):
        return self.__hello()
p1 = Person()
print(p1.welcome()) # Output: hello person

class Person:
    name = 'xyz'

    def __hello(self):
        print('hello person')

    def welcome(self):
        return self.__hello()
p1 = Person()
print(p1.welcome()) # Output: hello person
print(Person.name)