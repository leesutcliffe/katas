from datetime import date

class Account:
    def __init__ (self):
       self.balance = 0
       self.transactions = []
    
    def deposit(self, amount):
        self.balance += float(amount)
        
        transaction = "+" + str(amount)
        balanceAtTime = self.balance
        
        self.transactions.append([self.getDate(), transaction, balanceAtTime])
        return self.balance

    def withdraw(self, amount):
        self.balance -= float(amount)
        
        transaction = "-" + str(amount)
        balanceAtTime = self.balance
        
        self.transactions.append([self.getDate(), transaction, balanceAtTime])
        return self.balance

    def printStatement(self):
        print(f'{"DATE":<15}{"AMOUNT":<10}{"BALANCE":<10}')
        for tx in self.transactions:
            print(f'{tx[0]:<15}{tx[1]:<10}{tx[2]:<10}')
        
    def getDate(self):
        now = date.today()
        return now.strftime("%d/%m/%Y")