class Animal:
    def __init__(self, name, environment, legs):
        self.name = name
        self.environment = environment
        self.legs = legs

    def show_information(self):
        print(f"Name: {self.name}\nEnvironment: {self.environment}\nNumber of legs:{self.legs}")
