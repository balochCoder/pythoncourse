class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')

    def speak(self):
        print(f'my name is {self.name}, my age is {self.age}')


player = PlayerCharacter("Raj", 30)

player.speak()
