from API.scripts.services import CrawlerService as Cs
import re
from API.scripts.repositories import StatesOfTheWorldRepository
from API.scripts.views import State
from API.scripts.responses import TopStateResponse, FoundStateResponse


class StatesOfTheWorldService:
    """
          A class used to manage specific operations regarding the parsing of the states' details,
          insertion of specific information into the database or getting responses from the database.

          Attributes
          ----------
          crawler_service : CrawlerService
              an instance of the CrawlerService class
          states_dictionary : dict
              a dictionary where will be parsed all the information by the state's name
          states_of_the_world_repository : StatesOfTheWorldRepository
              an instance of the StatesOfTheWorldRepository class

          Methods
          -------
          __add_missing_information(self, current_details_list_length, default_information):
              Adds missing information about the states that are in the states_dictionary,
               but are not found on a specific table.
          __parse_capitals(self, capitals_table):
              Parses capitals from the capitals_table and adds them to the value-list of the key-state.
          __parse_population_values(self, population_table):
              Parses the numbers of the population from the population_table
              and adds them to the value-list of the key-state.
          __parse_density_values(self, density_table):
              Parses the density values from the density_table
              and adds them to the value-list of the key-state.
          __parse_surface_value(self, surface_table):
              Parses the surface values from the surface_table
              and adds them to the value-list of the key-state.
          __parse_neighbours(self, neighbours_table):
              Parses the neighbours' list from the neighbours_table
              and adds them to the value-list of the key-state.
          __parse_official_languages(self, official_languages_table):
              Parses the list of official languages from the official_languages_table
              and adds them to the value-list of the key-state.
          __parse_time_zones(self, time_zones_table):
              Parses the list of time zones from the time_zones_table
              and adds them to the value-list of the key-state.
          __parse_systems_of_government(self, systems_of_government_table):
              Parses the list of political regimes from the systems_of_government_table
              and adds them to the value-list of the key-state.
           create_records(self):
              Parses all the data to the states_dictionary based on specific websites and tables.
              Uses the functions above.
           __build_state(self, state_name):
               Creates an instance of the State class.
           insert_all_data(self):
               Inserts all data into the database.
           get_to_10_states_by(self, argument):
               Gets a response of top 10 states based on an argument.
           get_states_by(self, argument, argument_value):
               Gets a response about all the states, based on an argument and its value.
          """

    def __init__(self):
        """
        Constructs all the necessary attributes for the StatesOfTheWorldService object.

        Parameters
        __________
         crawler_service : CrawlerService
              an instance of the CrawlerService class
          states_dictionary : dict
              a dictionary where will be parsed all the information by the state's name
          states_of_the_world_repository : StatesOfTheWorldRepository
              an instance of the StatesOfTheWorldRepository class

        """
        self.crawler_service = Cs.CrawlerService()
        self.states_dictionary = dict()
        self.states_of_the_world_repository = StatesOfTheWorldRepository.StatesOfTheWorldRepository()

    def __add_missing_information(self, current_details_list_length, default_information):
        """
        Adds missing information about the states that are in the states_dictionary,
        but are not found on a specific table.

        :param current_details_list_length: the current length of the value list
        of the key-states from the states_dictionary
        :param default_information: the default value for the information like neighbours,
        political regime, etc. (0, 0.0, "" or []).

        :return: None
        """
        missing_population_states = [state for state in self.states_dictionary.keys() if
                                     len(self.states_dictionary.get(state)) < current_details_list_length]
        for state in missing_population_states:
            state_details = self.states_dictionary.get(state)
            state_details.append(default_information)
            self.states_dictionary.setdefault(state, state_details)

    def __parse_capitals(self, capitals_table):
        """
        Parses capitals from the capitals_table and adds them to the value-list(states_information)
        of the key-state(state_name) of the states_dictionary.

        :param capitals_table: the table where are parsed the rows for each state where we search for the capital name;
            row[0] is the state name, row[1] is the capital of the state
        :return: None
        """
        for row in capitals_table:
            states_information = list()
            state_name = row[0].replace("\u202f*", "")
            capital_name = row[1]
            states_information.append(capital_name)
            self.states_dictionary.setdefault(state_name, states_information)
        print("Capitals parsed!")

    def __parse_population_values(self, population_table):
        """
        Parses the numbers of the population from the population_table and adds them to the
        value-list(states_information) of the key-state(state_name) of the states_dictionary.

        :param population_table:the table where are parsed the rows for each state where we search for the population number;
            row[0] is the state name, row[1] is the population number of the state
        :return: None
        """
        for row in population_table:
            state_name = row[0]
            population_value = row[1].replace(",", "")
            state_information = self.states_dictionary.get(state_name)
            if state_information:
                state_information.append(int(population_value))
                self.states_dictionary[state_name] = state_information
            else:
                self.states_dictionary.setdefault(state_name, ["", int(population_value)])
        self.__add_missing_information(2, 0)
        print("Population values parsed!")

    def __parse_density_values(self, density_table):
        """
        Parses the values of the density from the density_table and adds them to the
        value-list(states_information) of the key-state(state_name) of the states_dictionary.

        :param density_table:the table where are parsed the rows for each state where we search for the density value;
            row[0] is the state name, row[1] is the density value of the state
        :return: None
        """
        for row in density_table:
            state_name = row[0]
            density_value = row[1].replace(",", "")
            state_information = self.states_dictionary.get(state_name)
            if state_information:
                state_information.append(float(density_value))
                self.states_dictionary[state_name] = state_information
            else:
                self.states_dictionary.setdefault(state_name, ["", 0, float(density_value)])
        self.__add_missing_information(3, 0.0)
        print("Density values parsed!")

    def __parse_surface_value(self, surface_table):
        """
        Parses the values of the surface from the surface_table and adds them to the
        value-list(states_information) of the key-state(state_name) of the states_dictionary.

        :param surface_table:the table where are parsed the rows for each state where we search for the surface value;
            row[0] is the state name, row[2] is the surface of the state
        :return:None
        """
        for row in surface_table:
            state_name = row[1]
            surface_value = row[2].replace(",", "").split("(")[0]
            state_information = self.states_dictionary.get(state_name)
            if state_information:
                state_information.append(float(surface_value))
                self.states_dictionary[state_name] = state_information
            else:
                self.states_dictionary.setdefault(state_name, ["", 0, 0.0, float(surface_value)])
        self.__add_missing_information(4, 0.0)
        print("Surface values parsed!")

    def __parse_neighbours(self, neighbours_table):
        """
        Parses the list of the neighbours from the neighbours_table and adds them to the
        value-list(states_information) of the key-state(state_name) of the states_dictionary.

        :param neighbours_table: the table where are parsed the rows for each state where we search for the neighbours;
            row[0] is the state name, row[5] is the list of the state's neighbours
        :return: None
        """
        for row in neighbours_table:
            pattern = r"(?:[A-Z][a-z\' ]+)+:"
            neighbours_list = [state[:-1] for state in re.findall(pattern, row[5])]
            state_name = row[0].split("[")[0]
            exceptions = ["China", "Netherlands", "United Kingdom"]
            is_exception = [name for name in exceptions if name in state_name]
            if is_exception:
                state_name = is_exception[0]
            state_information = self.states_dictionary.get(state_name)
            if state_information:
                state_information.append(neighbours_list)
                self.states_dictionary[state_name] = state_information
            else:
                self.states_dictionary.setdefault(state_name, ["", 0, 0.0, 0.0, neighbours_list])
        self.__add_missing_information(5, [])
        print("Neighbours parsed!")

    def __parse_official_languages(self, official_languages_table):
        """
        Parses the official languages of the states from the official_languages_table and adds them to the
        value-list(states_information) of the key-state(state_name) of the states_dictionary.

        :param official_languages_table: the table where are parsed the rows for each state where we search for the
            official languages of the state; row[0] is the state name, row[1] is the list of the official languages of the state
        :return: None
        """
        for row in official_languages_table:
            pattern = r"([A-Za-z]+\s?)"
            state_name = "".join(re.findall(pattern, row[0]))
            languages = [language.split("[")[0] if "[" in language else language for language in row[1].split("\n")]
            state_information = self.states_dictionary.get(state_name)
            if state_information:
                state_information.append(languages)
                self.states_dictionary[state_name] = state_information
            else:
                self.states_dictionary.setdefault(state_name, ["", 0, 0.0, 0.0, [], languages])
        self.__add_missing_information(6, [])
        print("Languages parsed!")

    def __parse_time_zones(self, time_zones_table):
        """
        Parses the list of the time zones from the time_zones_table and adds them to the
        value-list(states_information) of the key-state(state_name) of the states_dictionary.

        :param time_zones_table:the table where are parsed the rows for each state where we search for the time zones;
            row[0] is the state name, row[2] is the list of the time zones for each state found
        :return: None
        """
        for row in time_zones_table:
            state_name_pattern = r"([A-Za-z]+\s?)"
            time_zone_pattern = r"UTC\S+.*?(?=UTC|$)"

            state_name = "".join(re.findall(state_name_pattern, row[0]))
            time_zones = re.findall(time_zone_pattern, row[2])
            state_information = self.states_dictionary.get(state_name)
            if state_information:
                state_information.append(time_zones)
                self.states_dictionary[state_name] = state_information
            else:
                self.states_dictionary.setdefault(state_name, ["", 0, 0.0, 0.0, [], [], time_zones])
        self.__add_missing_information(7, [])
        print("Time zones parsed!")

    def __parse_systems_of_government(self, systems_of_government_table):
        """
        Parses the political regime from the systems_of_government_table and adds them to the
        value-list(states_information) of the key-state(state_name) of the states_dictionary.

        :param systems_of_government_table:the table where are parsed the rows for each state where we search for the political regime;
            row[0] is the state name, row[1] is the political regime of each state

        :return: None
        """
        for row in systems_of_government_table:
            state_name = row[0]
            political_regime = row[1].replace("\xa0", " ")
            state_information = self.states_dictionary.get(state_name)
            if state_information:
                state_information.append(political_regime)
                self.states_dictionary[state_name] = state_information
            else:
                self.states_dictionary.setdefault(state_name, ["", 0, 0.0, 0.0, [], [], [], political_regime])
        self.__add_missing_information(8, "")
        print("Political regimes parsed!")
        print(self.states_dictionary)

    def create_records(self):
        """
        Parses all the data to the states_dictionary based on specific websites and tables.

        :return: None
        """
        capitals_table = self.crawler_service.parse_states_by_capitals(
            "https://en.wikipedia.org/wiki/List_of_national_capitals_by_population", "wikitable")
        self.__parse_capitals(capitals_table)

        population_table = self.crawler_service.parse_information(
            "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population",
            "wikitable")
        population_table = [row for row in population_table if row != population_table[0]]
        self.__parse_population_values(population_table)

        density_table = self.crawler_service.parse_information(
            "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population_density",
            "wikitable")
        self.__parse_density_values(density_table)

        surface_table = self.crawler_service.parse_information(
            "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_area", "wikitable")
        surface_table = [row for row in surface_table if row != surface_table[0]]
        self.__parse_surface_value(surface_table)

        neighbours_table = self.crawler_service.parse_information(
            "https://en.wikipedia.org/wiki/List_of_countries_and_territories_by_number_of_land_borders", 'wikitable')
        self.__parse_neighbours(neighbours_table)

        official_languages_table = self.crawler_service.parse_information(
            "https://en.wikipedia.org/wiki/List_of_official_languages_by_country_and_territory",
            "wikitable")
        self.__parse_official_languages(official_languages_table)

        time_zones_table = self.crawler_service.parse_information(
            "https://en.wikipedia.org/wiki/List_of_time_zones_by_country", "wikitable")
        self.__parse_time_zones(time_zones_table)

        systems_of_government_table = self.crawler_service.parse_information(
            "https://en.m.wikipedia.org/wiki/List_of_countries_by_system_of_government", "wikitable")
        self.__parse_systems_of_government(systems_of_government_table)

    def __build_state(self, state_name):
        """
        Creates and returns a State object based on the name of a state. Gets all the information of the state from
        the states_dictionary by its name.

        :param state_name: the name of a state
        :return: State
        """
        state_details = self.states_dictionary.get(state_name)
        capital_name = state_details[0]
        population = state_details[1]
        density = state_details[2]
        surface = state_details[3]
        neighbours = state_details[4]
        spoken_languages = state_details[5]
        time_zones = state_details[6]
        political_regime = state_details[7]
        return State.State(state_name, capital_name, population, density, surface, neighbours,
                           spoken_languages, time_zones, political_regime)

    def insert_all_data(self):
        """
        Inserts all the information into several tables of the database.

        :return: Union[bool, Exception]
        """
        try:
            for state_name in self.states_dictionary.keys():
                new_state = self.__build_state(state_name)
                self.states_of_the_world_repository.insert_new_state(new_state)
                new_state.id = self.states_of_the_world_repository.get_state_id(state_name)
                print(new_state)
                self.states_of_the_world_repository.insert_state_neighbours(new_state)
                self.states_of_the_world_repository.insert_state_official_languages(new_state)
                self.states_of_the_world_repository.insert_state_time_zones(new_state)
            return True
        except Exception as exception:
            return exception

    def get_to_10_states_by(self, argument):
        """
         Gets a response of top 10 states from the database based on an argument.

        :param argument: a string that represents the argument based on what do we get the states;
        Its value can be: "population", "density" or "surface".

        :return: list
        """
        top_10_states = self.states_of_the_world_repository.get_top_10_states_by(argument)
        top_10_states_list = list()
        current_state = None
        for state in top_10_states:
            name = state[1]
            if argument == "population":
                current_state = TopStateResponse.TopStateResponse(name, "Populatie", state[3])
            elif argument == "density":
                current_state = TopStateResponse.TopStateResponse(name, "Densitate", state[4])
            elif argument == "surface":
                current_state = TopStateResponse.TopStateResponse(name, "Suprafata", state[5])
            top_10_states_list.append(current_state.__dict__())
        return top_10_states_list

    def get_states_by(self, argument, argument_value):
        """
        Gets a response about all the states, based on an argument and its value, from teh database.

        :param argument: a string that represents the argument based on what do we get the states;
        Its value can be: "language", "time_zone" or "political_regime".

        :param argument_value: the value of the argument

        :return:list
        """
        found_states = None
        if argument == "language":
            found_states = self.states_of_the_world_repository.get_states_by_language(argument_value)
        elif argument == "time_zone":
            found_states = self.states_of_the_world_repository.get_states_by_time_zone(argument_value)
        elif argument == "neighbour":
            found_states = self.states_of_the_world_repository.get_states_by_neighbour(argument_value)
        if argument == "political_regime":
            states_found_by_id = self.states_of_the_world_repository.get_states_by_political_regime(argument_value)
        else:
            states_found_by_id = list(
                map(lambda state_id: self.states_of_the_world_repository.get_state_by_id(state_id),
                    found_states))
        found_states_list = list()
        for state in states_found_by_id:
            current_state = FoundStateResponse.FoundStateResponse(state[0], state[1])
            found_states_list.append(current_state.__dict__())
        return found_states_list
