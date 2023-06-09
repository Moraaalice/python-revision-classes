#Create a Python class called BankAccount which represents a bank account,
# having as  attributes: accountNumber (numeric type), name (name of the account owner as string type), balance.
#Create a constructor with parameters: accountNumber, name, balance.
#Create a Deposit() method which manages the deposit actions.
#Create a Withdrawal() method  which manages withdrawals actions.
#Create a bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
#Create a display() method to display account details.
class Bank:
    def __init__(self,account_number,name,balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance
        
    def deposit(self,amount):
        self.amount = amount
        return self.balance + self.amount
    
    def withdrawal(self,amount):
        self.amount = amount
        if self.balance > self.amount:
            return self.balance - self.amount  
        else:
            print(f"You do not have enough amount to withdraw {self.amount}")
    
    def display(self):
        print("Account Number:",self.account_number)    
        print("Account Name:",self.name)  
        print("Account Balance:",self.balance)
            
            
