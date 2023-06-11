"""inhertance
single level | multiple level |   hierarchical    |  Multiple       
parent       |   grand parent |     parent        | papa   mother
   ^         |        ^       |     /    \        |  \        /
   |         |        |       |    /      \       |   \      /
   |         |       parent   | child 1    child2 |    child
child        |        |       |                   |
             |        child   |                   |


"""
########### example of multilevel inheritance ###########
class Warrenty:
      def warrent(self):
            print("warrenty")

class Computer(Warrenty):
      def __init__(self,price,brand,windows):
            self.price=price
            self.__brand=brand
            self.windows=windows
            
      
class Laptop(Computer):
      def lap(self,batterylife):    
            self.batter=batterylife
            print("from laptop class")

model=Laptop(50000,"asus","windows 11")
print(model.warrent())
model.lap("2 days")
########### example multiple inheritance ###########

class Warrenty:
      def warrenty(self):
            print(" only warrenty")

class Computer():
      def __init__(self,price,brand,windows):
            self.price=price
            self.__brand=brand
            self.windows=windows
      def warrenty(self):
            print("computer warrent ")
              # 1st     2nd  # MRO--> method resolution order 
class Laptop(Computer,Warrenty):
      def lap(self,batterylife):    
            self.batter=batterylife
            print("from laptop class")

model=Laptop(50000,"asus","windows 11")
print(model.warrenty())
model.lap("2 days")

