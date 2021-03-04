import datetime
import pytz
class Accounts:
    "simple account with deposit and withdraw methods"

    @staticmethod
    def _current_time():
        time=datetime.datetime.utcnow()
        return pytz.utc.localize(time)

    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance
        self.transeciton_list=[(Accounts._current_time(),balance)]
        print("Account created for ",name)
        self.showbalance()
        self.showbalance()

    def deposit(self,amount):
        if amount > 0:
            self.__balance+=amount
        self.showbalance()
        self.transeciton_list.append((Accounts._current_time(),amount))

    def withdraw(self,amount):
        if 0 < amount <= self.__balance:
            self.__balance-=amount
            self.transeciton_list.append((Accounts._current_time(), -amount))
        else:
            print("The amount must be greater than zero and the existing amount.")
        self.showbalance()


    def showbalance(self):
        print("The total balance is {}".format(self.__balance))

    def show_transection(self):
        for date, amount in self.transeciton_list:
            if amount>0:
                tran_type="deposited"
            else:
                tran_type="withdrawn"
                amount*=-1
            print("{:6} , {}, on {} (local time was {})".format(amount,tran_type,date,date.astimezone()))

if __name__=='__main__':
    account=Accounts("Umair",0)
    # account.showbalance()
    account.deposit(1000)
    # account.showbalance()
    account.withdraw(500)
    # account.showbalance()
    account.show_transection()

    account1=Accounts("Kamran",1000)
    account1.__balance=5
    account1.showbalance()
    account1.deposit(100)
    account1.withdraw(200)
    account1.show_transection()

# Name Mangling: In this concept we write double underscore (__) before a vriable name and when we access that, python will not provide access to that
# python will internally change its name to _classname__variablename I have done nothing new here just checking the procedure