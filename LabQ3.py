class bankAccount:
    def __init__(self,accountNumber = 0, customerName = '', Balance=0) -> None:
        self.accountNumber = accountNumber
        self.customerName = customerName
        self.Balance = Balance
    def deposit(self,addBal):
        self.Balance += addBal
    def withdraw(self,withdrawBal):
        self.Balance -= withdrawBal
    def displayDetails(self):
        return "Account Number: {0}, \nCustomer Name: {1} \nBalance: {2}".format(self.accountNumber,self.customerName,self.Balance)


#Create Objects Example
SameesBank = bankAccount(28006001, "Samee Khan", 0)
SameesBank.deposit(2500)
SameesBank.withdraw(2000)
print(SameesBank.displayDetails())