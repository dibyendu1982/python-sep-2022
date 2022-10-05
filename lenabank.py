class Transaction():
    def __init__(self, txnNo: int, description: str, amount: float, txnType: str):
        self.txnNo = txnNo
        self.description  = description
        self.amount = amount 
        self.txnType = txnType


class Account: 
    __last_account_number = 1 #* static, field attached to the class (ONE COPY)
    
    @staticmethod
    def get_last_account_number(): 
        return Account.__last_account_number
    
    def __init__(self, ac: int, hn: str, bal: float):
        self.account_number  = ac 
        self.holders_name = hn
        self.__balance = bal # 
        self.txnNo = 10000
        self.transactions : list[Transaction] = []
    
    def __str__(self):
       return f"""Checking Account Details 
                    Name: {self.holders_name} 
                    Account Number: {self.account_number} 
                    Balance: {self.balance()}"""
    
    def __eq__(self, rhs):
        return self.account_number == rhs.account_number 
    
    def __gt__(self, rhs):
        return self.__balance > rhs.__balance
    
    # May not be needed as eq and gt can cater to this 
    def __lt__(self, rhs):
        return self.__balance < rhs.__balance
    
    def __ge__(self, rhs):
        return self.__balance >= rhs.__balance
    
    def __le__(self, rhs):
        return self.__balance <= rhs.__balance
        
    def deposit(self, description: str, amount: float) -> float :
        self.__balance += amount
        self.txnNo += 1
        txn = Transaction(self.txnNo, description, amount, "CR")
        self.transactions.append(txn)
        return self.__balance 
    
    def withdraw(self, description: str, amount: float) -> float:
        self.__balance -= amount
        self.txnNo += 1
        txn = Transaction(self.txnNo, description, amount, "DR")
        self.transactions.append(txn)
        return self.__balance 
    
    def print(self) -> None:
        print(self.account_number, self.holders_name, self.__balance)
        header_format = "{0:<20} {1:<20} {2:<20} {3:<20}"
        print(header_format.format("Transaction No.", "Description", "Amount", "Type"))
        passbook_format: str = "{0:<20} {1:<20} {2:<20.2f} [{3:^20}]"
        for transaction in self.transactions:
            print(passbook_format.format (transaction.txnNo, transaction.description, transaction.amount, transaction.txnType))
    
    @property
    def balance(self): #* Getter 
        return self.__balance
    
    @balance.setter
    def balance(self, new_balance: float):
        print("setter called")
        self.__balance = new_balance
    
    ## this is a generator which returns an iterator 
    def get_transactions(self):
        for txn in self.transactions:
            yield txn
    

class SavingsAccount(Account):
    def __init__(self, an: int, hn: str, bal: float, min_bal: float):
        # self.account_number = an 
        # self.holders_name = hn
        # self.balance = bal
        super().__init__(an, hn, bal) #! Constructor chaining,  above 3 statements can be written as this. 
        self.minimum_balance = min_bal
        
    # ? Override the withdraw behavior 
    def withdraw(self, description: str, amount: float) -> float:
        if self.balance() - self.minimum_balance < 500 :
            raise Exception("Saving Accounts Insufficient Funds")
        super().withdraw(description, amount)
        return self.balance()
    
class CheckingAccount(Account):
    def __init__(self, an: int, hn: str, bal: float, cc_limit: float):
        super().__init__(an, hn, bal)
        self.credit_limit = cc_limit
        
    def __str__(self):
       return f"""Checking Account Details 
                    Name: {self.holders_name} 
                    Account Number: {self.account_number} 
                    Balance: {self.balance}"""
    
    def withdraw(self, description: str, amount: float) -> float:
        if amount >= self.balance + self.credit_limit :
            raise Exception("Checking account Insufficient funds")
        super().withdraw(description, amount) #~ * Data should be updated by the owner of the field in this case Balance. 
        return self.balance
            
# acct = Account(1001, "Dibyendu", 10000)
# # import dis 
# # dis.dis(Account)
# acct.deposit("Regular account deposit", 1000) 
# acct.print()
# acct.withdraw("Regular account deposit", 1000)
# acct.print()
# print("Dunder Balance", acct.__balance)

# savings_account = SavingsAccount(1002, "diby", 1000, 50)
# savings_account.withdraw("Savings withdraw", 800)
# savings_account.print()

print( "-" * 30, "Checking example", "-" * 30)
checking = CheckingAccount(1003, "diby1", 20000, 40000)
checking.withdraw("Loan Payment", 10000.00)
checking.deposit("salary", 40000.00)

checkingAdani = CheckingAccount(49589, "Gautam Adani", 398594854.34, 234902842)
checkingAdani1 = CheckingAccount(49589, "Gautam Adani", 398594854.34, 234902842)
print(checking)
checking.print()

print (checking > checkingAdani)
print (checking < checkingAdani)
print("id(checkingAdani)", id(checkingAdani), "id(checkingAdani1)", id(checkingAdani1))
print ("Operator overloading of == using __eq__", checkingAdani == checkingAdani1)

print("checkingAdani.balance", checkingAdani.balance)
print("Last account number", Account.get_last_account_number())
print(checking.get_transactions())

for txn in checking.get_transactions():
    print(txn.description, txn.amount)

