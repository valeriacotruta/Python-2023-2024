class FoundStateResponse:
    """
           A class to represent a state from all of the states found in the database.

           Attributes
           ----------
           state_id : int
               the id of the state from the database
           name : str
               name of the state

           Methods
           -------
           __dict__():
               Returns a dictionary representation of the FoundStateResponse object.
        """

    def __init__(self, state_id, name):
        """

        :param state_id:the id of the state from the database
        :param name: name of the state
        """
        self.state_id = state_id
        self.name = name

    def __dict__(self):
        """
        Returns a dictionary representation of the FoundStateResponse object.

        :return: dict
        """
        return {"Id": self.state_id, "Nume": self.name}
