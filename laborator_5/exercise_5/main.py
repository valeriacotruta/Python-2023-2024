# Create a class hierarchy for animals, starting with a base class Animal.
# Then, create subclasses like Mammal, Bird, and Fish.
# Add properties and methods to represent characteristics unique to each animal group.

import exercise_5 as ex_5

lion = ex_5.Mammal("Lion", "Grassland", 4, "Golden")
lion.show_information()

eagle = ex_5.Bird("Eagle", "Mountain", 2, True)
eagle.show_information()
eagle.build_nest()

clownfish = ex_5.Fish("Clownfish", "Coral Reef", 0, True)
clownfish.show_information()
