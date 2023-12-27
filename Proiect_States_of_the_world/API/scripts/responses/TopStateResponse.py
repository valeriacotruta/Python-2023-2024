class TopStateResponse:
    """
       A class to represent a state from the top 10 states response.

       Attributes
       ----------
       name : str
           name of the state
       argument : str
           the argument that expresses the top; its value can be: "Populatie", "Suprafata" or "Densitate"
       argument_value : int or double
           value of the argument parameter

       Methods
       -------
       __dict__():
           Returns a dictionary representation of the TopStatesResponse object.
    """
    def __init__(self, name, argument, argument_value):
        """
        Constructs all the necessary attributes for the TopStatesResponse object.

        :param name:name of the state
        :param argument:the argument that expresses the top; its value can be: "Populatie", "Suprafata" or "Densitate"
        :param argument_value: value of the argument parameter
        """
        self.name = name
        self.argument = argument
        self.argument_value = argument_value

    def __dict__(self):
        """
        Returns a dictionary representation of the TopStatesResponse object.

        :return: dict
        """
        return {"Nume:": self.name, self.argument: self.argument_value}
