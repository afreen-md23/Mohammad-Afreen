class Bank:
   def __init__(self, balance=0):

       self.balance = balance

   def viewOptions(self):
       while True:
           print("1. Deposit")
           print("2. Withdraw")
           print("3. Balance Inquiry")
           print("0. Exit")
           case = int(input("Enter your choice: "))
           if case == 1:
               self.deposite()
           elif case == 2:
               self.withdraw()
           elif case == 3:
               self.balenquiry()
           elif case == 0:
               print("Exiting... Thank you!")
               break
           else:
               print("Invalid choice. Please try again.")



   def validation(self):
       count = 1
       while count <= 3:
           pin = int(input("Enter the pin number: "))
           if pin == 1234:
               print("PIN verified successfully.")
               self.viewOptions()
               break
           else:
               if count < 3:
                   print("Invalid pin number. Try again.")
               else:
                   print("Too many failed attempts. Please wait for 30 seconds.")

                   import time
                   time.sleep(30)
           count += 1



   def deposite(self):
       amount = int(input("enter the deposit money"))

       if amount>=100 and amount %100==0  and amount<=50000:
           self.balance += amount
           print(f"Total balance : {self.balance}")
       else:
           print("the min amount of the balance is 100")


   def withdraw(self):
       withdraw_amt = int(input("Enter the with draw amount"))

       if withdraw_amt >=100 and withdraw_amt %100==0 and withdraw_amt < self.balance and withdraw_amt <=20000:
           self.balance -= withdraw_amt
           print(f"You have successfully withdrawn {withdraw_amt}.")
           print(f"Remaining balance: {self.balance}")

       else :
           print("the  min amount  of the balance should be transaction is 500")

   def balenquiry(self):
       print(f"the balance amount....:{self.balance}")


obj=Bank()
obj.validation()
