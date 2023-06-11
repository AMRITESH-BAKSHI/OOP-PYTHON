# polymorphism
# 1. method overriding
# 2. method overloading
# 3. operator overloading

############## METHOD OVERLOADING
class Geometry:
      def area(self,a,b=0):
            if b==0:
                  print("area of circle is ",3.14*a**2)
            else:
                  print("area of rectangle is",a*b)
            
ob=Geometry()
ob.area(4)
ob.area(4,5)

############### operator overloading --> magic method
print(2+1)
print("hello"+"world")
