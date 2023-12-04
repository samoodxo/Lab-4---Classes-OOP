class Student:
    def __init__(self,name = '',id = 0,address = '') -> None:
        self.name = name
        self.id = id
        self.address = address
    #Setters
    def set_name(self,newname):
        self.name = newname
    def set_id(self,newid):
        self.id = newid
    def set_address(self,newaddress):
        self.address = newaddress
    #getters
    def get_name(self):
        return self.name
    def get_id(self):
        return self.id
    def get_address(self):
        return self.address
    def __str__(self):
        return "The students name is {0}, \nThe students id is {1},\nThe students address is {2}".format(self.name,self.id,self.address)
    
#Create Objects Example
s1 = Student()
s1.set_name("Samee")
s1.set_id(28006001)
s1.set_address("1301 16 Ave NW")

print(s1.__str__())