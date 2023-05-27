class Atm:
       # function->just function len()
       # method -> function written inside class example list.append()
       # __init__ -> constructor automatically execute inside class
       # constructor we use configuration work inside it
       # special/magic/dunder methods


       # self ->       
       def __init__(self):
             self.pin=""
             self.balance=0
             print(id(self))
             self.menu()
                  
       def menu(self):
             user_input=input("""
            hello how would u like to proceed
            choose option
            1->create pin
            2-> to deposit
            3-> to withdraw cash
            4->check balance
            5->exit
            choose option here#  """)
             if user_input=="1":
                   print("create pin")
                   self.createPin()
             elif user_input=="2":
                   self.deposit()
             elif user_input=="3":
                   self.withdraw()
             elif user_input=="4":
                  self.checkBalance()
             elif user_input=="5":
                   exit()
             else:
                   print("give valid input")

       def createPin():
             self.pin=input("enter your pin")
             print("pin set !!")
       def deposit(self):
             temp=input("enter pin")
             if temp==self.pin:
                   depo=int(input("enter the ammount"))
                   self.balance+=depo
                   print("success")

             else:
                   print("give valid pin")
       def withdraw(self):
             temp=input("enter pin")
             if temp==self.pin:
                   amout=int(input("enter the amount to withdraw"))
                   if amout<=self.balance:
                         print("amount withdraw is ",amout)
                         self.balance-=amout
                   else:
                         print("insufficient in funds",self.balance)
             else:
                   print("invalid pin")
       def checkBalance(self):
             temp=input("enter pin")
             if temp==self.pin:
                   print(self.balance)
             else:
                   print("invalid pin") 
             
                  
             
      
       
       
      
            
             
      
