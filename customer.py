class Customer:
      def __init__(self,name,gender):
            self.name=name
            self.gender=gender

def greet(customer):
      if customer.gender=="male":
            print("hello sir",customer.name,"how can i help you")
      else:
            print("hello mam",customer.name,"how can i help you")

                  
      cust2=Customer("sumita","female")
      return cust2
      
cust=Customer("amritesh","male")
greet(cust)
new_cust=greet(cust)
print(new_cust.name)
