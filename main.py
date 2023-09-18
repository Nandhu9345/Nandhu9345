class bankaccount:                               
 def __init__(self, account_number, account_holder_name,initial_balance=0.0):
   self.__account_number=   account_number
   self.__account_holder_name= account_holder_name
   self.__account_balance= initial_balance
 def deposit(self, amount):
  if amount>0:

   self.__account_balance+= amount  
  #self.__account_balance=self.__account_balance+amount 
   print("deposit${}.new balance:${}".format(amount,self.__account_balance))
  else:
   print("invalid deposit amount please deposit a positive amount.")      
 def withdraw(self,amount):
  if amount>0 and amount<= self.__account_balance:
   self.__account_balance-=amount
   #self.__account_balance=self.__account_balance-amount
   print("withdraw ${}.newbalance:${}".format(amount,self.__account_balance))  
  else:
    print("invalid withdraw amount or insufficient balance.")
 def display_balance(self):
    print("account balance for{}(account{}):${}".format(self.__account_holder_name,self.__account_number,self.__account_balance))
  #create a instance of the bank account class 
account = bankaccount(account_number="123",
account_holder_name="nandhini", 
  initial_balance=500.00)
# test deposit and withdrawal functionally 
account.display_balance()
account.deposit(300.00)
account.withdraw(200.00)
account.display_balance()
