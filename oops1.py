#1.initiate class
class employee:
    #special method/magic method/dunder method - constructor
    def __init__(self):
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
    
    def travel(self, destination):
        print(f"Employee is now moving to {destination}")

#creating an obj/instance of the class
sam = employee()
#printing attributes
print(sam.id)
#calling a method
sam.travel("OHIO")
print(type(sam))

#2.everything in python is an pbject (data structure/data type) - so it is called oops

#3. Advantages of oops:
        # you can create own datatype
        # code reusability
        #debugging
        #easy to collab
        
