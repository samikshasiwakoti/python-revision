# the process of hiding data and controlling acess is encapsulation
# in encapsulation we mostly used privatevaribale

class BankAccount :
    def __init__(self,owner,balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self,amount) :
        self.__balance += amount
        print("The amount is:",amount)  

    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdraw:",amount)  
        else:
            print("Insufficient baalnces")
    def check_balance(self):
        return self.__balance 
a = BankAccount("Samiksha",1000)
a.deposit(5000)  
a.withdraw(500)         