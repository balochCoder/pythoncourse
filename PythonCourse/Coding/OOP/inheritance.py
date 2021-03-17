class User():
    def sign_in(self):
        print("logged in")

class Wizard(User):
    def __init__(self,name,power):
        self.name = name
        self.power = power
    def attack(self):
        print(f'attacking power {self.power}')

class Archer(User):
    def __init__(self,name,no_of_arrows):
        self.name = name
        self.no_of_arrows = no_of_arrows
    
    def attack(self):
        print(f'number of arrows left: {self.no_of_arrows}')
    
wizard1 = Wizard('Merlin',50)
archer1 = Archer('Robin',100)

archer1.attack()