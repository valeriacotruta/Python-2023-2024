class FoundStateResponse:
    def __init__(self, state_id, name):
        self.state_id = state_id
        self.name = name

    def __dict__(self):
        return {"Id": self.state_id, "Nume": self.name}
