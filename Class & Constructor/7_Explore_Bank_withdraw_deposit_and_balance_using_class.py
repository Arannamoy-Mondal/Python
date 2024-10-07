class bank:
    def __init__(self,balance):
        self.balance=balance
        self.min_balance=100
        self.max_balance=100000
    
    def withdraw(self,balance):
        if(self.balance>balance and balance>self.min_balance and balance<=self.max_balance):
            print('Withdrawl successful',balance)
            self.balance-=balance
        elif(self.balance<balance):
            print('Insufficient balance')
        elif(balance<=self.min_balance):
            print('Less than minimum balance')
        elif(balance>self.max_balance):
            print('Reached maximum balance')

bracBank=bank(100000000)
bracBank.withdraw(500)
ibbl=bank(5000)
ibbl.withdraw(100)
dbbl=bank(1000000)
dbbl.withdraw(500000)