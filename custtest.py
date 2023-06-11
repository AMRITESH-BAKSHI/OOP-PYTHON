class Customer:
      # static / class variable
      __counter=1
      def __init__(self,name,age):
            # instance variable
            self.name=name
            self.age=age
            
            self.sno=Customer.__counter
            Customer.__counter+=1
      
      def intro(self):
            print("my name is ",self.name,"my age is ",self.age)
      @staticmethod
      def getcounter():
            return Customer.__counter
      
      @staticmethod
      def setcounter(newcounter):
            Customer.__counter=newcounter
            
c1=Customer("amritesh",18)
c2=Customer("himanshu",17)
c3=Customer("nilesh",18)
c4=Customer("anubhav",18)
c4=Customer("anubhav",18)

