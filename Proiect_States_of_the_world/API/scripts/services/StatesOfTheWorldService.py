import CrawlerService as Cs
import re
from API.scripts.repositories import StatesOfTheWorldRepository
from API.scripts.views import State


class StatesOfTheWorldService:
    def __init__(self):
        self.crawler_service = Cs.CrawlerService()
        self.states_dictionary = dict()

    def __add_missing_information(self, current_details_list_length, default_information):
        missing_population_states = [state for state in self.states_dictionary.keys() if
                                     len(self.states_dictionary.get(state)) < current_details_list_length]
        for state in missing_population_states:
            state_details = self.states_dictionary.get(state)
            state_details.append(default_information)
            self.states_dictionary.setdefault(state, state_details)

    def __parse_capitals(self, capitals_table):
        for row in capitals_table:
            states_information = list()
            state_name = row[0].replace("\u202f*", "")
            capital_name = row[1]
            states_information.append(capital_name)
            self.states_dictionary.setdefault(state_name, states_information)
        print("Capitals parsed!")

    def __parse_population_values(self, population_table):
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
        state_details = self.states_dictionary.get(state_name)
        if len(state_details) < 8:
            return (state_name, state_details)
        else:
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

    def insertAllData(self):
        states_of_the_world_repository = StatesOfTheWorldRepository.StatesOfTheWorldRepository()
        for state_name in self.states_dictionary.keys():
            new_state = self.__build_state(state_name)
            states_of_the_world_repository.insert_new_state(new_state)
            new_state.id = states_of_the_world_repository.get_state_id(state_name)
            print(new_state)
            states_of_the_world_repository.insert_state_neighbours(new_state)
            states_of_the_world_repository.insert_state_official_languages(new_state)
            states_of_the_world_repository.insert_state_time_zones(new_state)


x = StatesOfTheWorldService()
x.create_records()
x.insertAllData()
