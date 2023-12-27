class State:
    """
       A class to represent a state.

       Attributes
       ----------
       id : int
           the id of the state from the database
       name : str
           name of the state
       capital_name : str
           capital of the state
       population : int
           population of the state
       density : double
           density of the state
       surface : double
           surface of the state
       neighbours : list
           neighbours of the state
       spoken_languages : list
           the official languages spoken in the state
       time_zones : list
           the time zones of the state
       political_regime : str
           the political regime of the state

       Methods
       -------
       __str__():
           Prints details about the state.
       """

    def __init__(self, name, capital_name="", population=0, density=0.0, surface=0.0, neighbours=[],
                 spoken_languages=[],
                 time_zones=[], political_regime=""):
        """
        Constructs all the necessary attributes for the State object.

        Parameters
        __________
        name : str
           name of the state
       capital_name : str
           capital of the state
       population : int
           population of the state
       density : double
           density of the state
       surface : double
           surface of the state
       neighbours : list
           neighbours of the state
       spoken_languages : list
           the official languages spoken in the state
       time_zones : list
           the time zones of the state
       political_regime : str
           the political regime of the state

        """
        self.id = 0
        self.name = name
        self.capital_name = capital_name
        self.population = population
        self.density = density
        self.surface = surface
        self.neighbours = neighbours
        self.spoken_languages = spoken_languages
        self.time_zones = time_zones
        self.political_regime = political_regime

    def __str__(self):
        """
         Returns a human-readable and informal string representation of an instance of the State class.

         Parameters
         __________
            None
        """
        return f"State(id: {self.id}, name:{self.name}, capital_name:{self.capital_name}, " \
               f"population:{self.population}, density:{self.density}, " \
               f"surface:{self.surface}, neighbours:{self.neighbours}, " \
               f"official_languages:{self.spoken_languages}, " \
               f"time zones:{self.time_zones}, " \
               f"political_regime:{self.political_regime})"
