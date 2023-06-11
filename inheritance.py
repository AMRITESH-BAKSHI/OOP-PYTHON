class User():
      def login(self):
            print("login")
      def register(self):
            print("register")

class Student(User):
      def Enroll(self):
            print('enroll')
      def review(self):
            print("review")

stu1=Student()
stu1.Enroll()
stu1.login()

#user=User()
#user.Enroll()

########### inheriting construcuter ##############
class Computer:
      def __init__(self,price,brand,windows):
            self.price=price
            self.__brand=brand
            self.windows=windows
            
      
class Laptop(Computer):
      def lap(self,batterylife):    
            self.batter=batterylife
            print("from laptop class")

model=Laptop(50000,"asus","windows 11")
print(model.price)
model.lap("2 days")
#print(model.__brand) private cannot be read directly



# method overriding -> polymorphism
# method overloading --^
# operator overloading--^

######### polymorphism #########
class Computer:
      def __init__(self,price,brand,windows):
            self.price=price
            self.__brand=brand
            self.windows=windows
            #self.batter=batterylife
      def lap(self,batterylife):   # method overriding
            self.batter=batterylife
            print("from computer class ")
class Laptop(Computer):
      def lap(self,batterylife):    # method overriding
            self.batter=batterylife
            print("from laptop class")

model=Laptop(50000,"asus","windows 11")
print(model.price)
model.lap("2 days")

################## example ##############
class Parent:
      def __init__(self,num):
            self.__num=num
      def get_num(self):
            return self.__num
class Son(Parent):
      def show(self):
            print("this is child class ")
so=Son(23)
print(so.get_num()  )
############# example 2 #########
class Parent:
      def __init__(self,num,val):
            self.__val=val
      def get_num(self):
            return self.__val
class Son(Parent):
      def __init__(self,num,val):
            self.num=num
      def show(self):
            print("this is child class ")
so=Son(23,1)
#print(so.get_num())

########### example # ###########

class Computer:
      def __init__(self,price,brand,windows):
            self.price=price
            self.__brand=brand
            self.windows=windows
            #self.batter=batterylife
      def lap(self,batterylife):   # method overriding
            self.batter=batterylife
            print("from computer class ")
class Laptop(Computer):
      def lap(self,batterylife):    # method overriding
            self.batter=batterylife
            print("from laptop class")
            super().lap("4 days")  # super used to invoke parent class constructor and methods
            # can only be used inside class 
model=Laptop(50000,"asus","windows 11")
print(model.price)
model.lap("2 days")
########### super key words uses
class Computer:
      def __init__(self,price,brand,windows):
            self.price=price
            self.brand=brand
            self.windows=windows
          
class Laptop(Computer):
      def __init__(self,price,brand,windows,ram):
            super().__init__(price,brand,windows)
            self.ram=ram
            print("inside laptop")
            
model=Laptop(50000,"asus","windows 11",8)
print(model.brand)
print(model.ram)
print(model.price)














