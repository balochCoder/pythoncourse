class PlayerCharacter:
    # Class Object Attribute or static method it will be same for all instances
    members = True

    def __init__(self, name, age):
        self.name = name  # Attributes
        self.age = age

    def check(self):
        print(f'my name is {self.name}')
        return True


player1 = PlayerCharacter("Raheel", 30)

player1.check()
