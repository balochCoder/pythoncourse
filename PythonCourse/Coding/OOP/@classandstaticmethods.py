class PlayerCharacter:
    membership=True
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    @classmethod
    def addingthings(cls,num1,num2):
        return num1+num2
        # return cls("Raheel",2,3) we instanciated the class in this method
    
    @staticmethod
    def addingthings1(num1,num2): # same as classmethod but we do not have access to cls
        return num1+num2

# player3 = PlayerCharacter.addingthings(2,3) we already instanciated the class in method so it means it go to constructor and name will be Raheel and age 5
# print(player3.age)
print(PlayerCharacter.addingthings(2,3))