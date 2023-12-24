class State:
    def __init__(self, name, capital_name, population, density, surface, neighbours, spoken_languages, time_zones,
                 political_regime):
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
        return f"State(id: {self.id}, name:{self.name}, capital_name:{self.capital_name}, " \
               f"population:{self.population}, density:{self.density}, " \
               f"surface:{self.surface}, neighbours:{self.neighbours}, " \
               f"official_languages:{self.spoken_languages}, " \
               f"time zones:{self.time_zones}, " \
               f"political_regime:{self.political_regime})"
