class TopStateResponse:
    def __init__(self, name, argument, argument_value):
        self.name = name
        self.argument = argument
        self.argument_value = argument_value

    def __dict__(self):
        return {"Nume:": self.name, self.argument: self.argument_value}
