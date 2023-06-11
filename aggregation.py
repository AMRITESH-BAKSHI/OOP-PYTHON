class Customer:
      def __init__(self,name,gender,address):
            self.name=name
            self.gender=gender
            self.address=address
      def editProfile(self,newname,newcity,newpin,newstate):
            self.name=newname
            self.address.change_address(newcity,newpin,newstate)
class Address:
      def __init__(self,city,pincode,state):
            self.city=city
            self.pincode=pincode
            self.state=state
      def change_address(self,new_city,new_pin,new_state):
            self.city=new_city
            self.pin=new_pin
            self.state=new_state
addre=Address("Gorakhpur",273016,"uttar pradesh")
cust=Customer("amritesh","male",addre)
print(cust.editProfile("himanshu","lucknow",345345,"up"))
print(cust.name)
