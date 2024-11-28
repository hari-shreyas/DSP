class bank:
    def __init__(self):
        self.balance = 0
        print ("the account is created")

    def deposit(self):
        amount = float(input("Enter the amount to be deposit: "))
        self.balance = self.balance + amount
        print ("deposit successful")
        print ('balance is: ',self.balance)

    def withdraw(self):
        amount = float(input("Enter the amount to withdraw: "))
        if (self.balance >= amount):
            self.balance = self.balance - amount
            print ("withdrawl successful")
        else:
            print ('insuficient balance')

    def enquiry(self):
        print ("balance in the account is:", self.balance)


acc = bank()
acc.deposit()
acc.withdraw()
acc.enquiry()