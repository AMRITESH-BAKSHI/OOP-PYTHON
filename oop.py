class Atm:
       # function->just function len()
       # method -> function written inside class example list.append()
       # __init__ -> constructor automatically execute inside class
       # constructor we use configuration work inside it
       # special/magic/dunder methods


       # self ->       
       def __init__(self):
             self.__pin=""    # __pin means __ will make it private
             self.__balance=0  # __pin means actually python read it as _Atm__pin
                                  #_Atm__pin is true variable
             print(id(self))      # nothing in python is Truly private
             self.__menu()
                  
       def __menu(self):
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

       def createPin(self):
             self.__pin=input("enter your pin")
             print("pin set !!")
       def deposit(self):
             temp=input("enter pin")
             if temp==self.__pin:
                   depo=int(input("enter the ammount"))
                   self.__balance+=depo
                   print("success")

             else:
                   print("give valid pin")
       def withdraw(self):
             temp=input("enter pin")
             if temp==self.__pin:
                   amout=int(input("enter the amount to withdraw"))
                   if amout<=self.__balance:
                         print("amount withdraw is ",amout)
                         self.__balance-=amout
                   else:
                         print("insufficient in funds",self.__balance)
             else:
                   print("invalid pin")
       def checkBalance(self):
             temp=input("enter pin")
             if temp==self.__pin:
                   print(self.__balance)
             else:
                   print("invalid pin")
       def set_pin(self,newpin):
              p=input("enter the old pin")
              if p==self.__pin:
                     if type(newpin)==str:
                            self.__pin=newpin
                            print("pin changed")
                     else:
                            print("give valid input")
              else:
                     print("not allowed")

       
             
                  
             
      
       
       
      
            
             
      
