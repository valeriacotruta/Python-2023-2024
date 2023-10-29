def ex_1(a, b):
    # Write a function that receives as parameters two lists a and b and returns a list
    # of sets containing: (a intersected with b, a reunited with b, a - b, b - a)
    return [set(filter(lambda element: element in a and element in b, a)), set(a + b),
            set(filter(lambda element: element in a and element not in b, a)),
            set(filter(lambda element: element not in a and element in b, b))]


# print(ex_1([1, 2, 3], [3, 4, 1]))


def ex_2(string):
    # Write a function that receives a string as a parameter and returns a dictionary in which
    # the keys are the characters in the character string and the values are the number of
    # occurrences of that character in the given text.
    return dict(zip([character for character in string], [string.count(character) for character in string]))


# print(ex_2('hello'))
# print(ex_2('Ana has apples.'))

def ex_3(dictionary1, dictionary2):
    # Compare two dictionaries without using the operator "==" returning True or False.
    # (Attention, dictionaries must be recursively covered because they can contain other containers,
    # such as dictionaries, lists, sets, etc.)
    if not isinstance(dictionary1, dict) or not isinstance(dictionary2, dict) or set(dictionary1.keys()) != set(
            dictionary2.keys()):
        return False

    for key in dictionary1:
        if isinstance(dictionary1[key], dict) and isinstance(dictionary2[key], dict):
            if not ex_3(dictionary1[key], dictionary2[key]):
                return False

        elif isinstance(dictionary1[key], (list, set)) and isinstance(dictionary1[key], (list, set)):
            if not compare_lists_sets(dictionary1[key], dictionary1[key]):
                return False
        elif dictionary1[key] != dictionary2[key]:
            return False

    return True


def compare_lists_sets(container1, container2):
    sorted_container1 = sorted(container1)
    sorted_container2 = sorted(container2)

    for element1, element2 in zip(sorted_container1, sorted_container2):
        if isinstance(element1, dict) and isinstance(element2, dict):
            if not ex_3(element1, element2):
                return False
        elif isinstance(element1, (list, set)) and isinstance(element2, (list, set)):
            if not compare_lists_sets(element1, element2):
                return False
        elif element1 != element2:
            return False
    return True


dictionary1 = {
    "Dacia": 120,
    "BMW": 160,
    "Toyota": 140
}
dictionary2 = {
    "BMW": 160,
    "Toyota": 140,
    "Dacia": 120
}
print(ex_3(dictionary1, dictionary2))

dictionary3 = {
    "BMW": 160,
    "Toyota": 140,
    "Dacia": 120,
    "Ford": 120,
}
print(ex_3(dictionary1, dictionary3))

dictionary4 = {
    "BMW": 160,
    "Toyota": 140,
    "Dacia": 120,
    "Ford": 120,
    "key1": dictionary1
}
print(ex_3(dictionary1, dictionary4))


def ex_4(tag, content, **keys_values):
    # The build_xml_element function receives the following parameters:
    # tag, content, and key-value elements given as name-parameters.
    # Build and return a string that represents the corresponding XML element.
    # Example: build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid ")
    # returns  the string = "<a href=\"http://python.org \ "_class = \" my-link \ "id = \" someid \ "> Hello there </a>"
    open_tag = f"<{tag} "
    close_tag = f"</{tag}>"
    for key in keys_values.keys():
        open_tag += f'{key} = \\" {keys_values[key]} \\ "'
    return open_tag + ">" + content + close_tag


# print(ex_4("a", "Hello there", href=" http://python.org ", _class=" my-link ", id=" someid "))

def ex_5(*set_tuples, **dictionary):
    # The validate_dict function that receives as a parameter a set of tuples
    # ( that represents validation rules for a dictionary that has strings as keys and values) and a dictionary.
    # A rule is defined as follows: (key, "prefix", "middle", "suffix").
    # A value is considered valid if it starts with "prefix", "middle" is inside the value (not at the beginning or end)
    # and ends with "suffix". The function will return True if the given dictionary matches all the rules, False otherwise.
    # Example: the rules  s={("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
    # and d= {"key1": "come inside, it's too cold out", "key3": "this is not valid"} => False
    # because although the rules are respected for "key1" and "key2" "key3" that does not appear in the rules.

    for key in dictionary.keys():
        if key not in [element[0] for element in set_tuples[0]]:
            return False
        for element in set_tuples[0]:
            if element[0] == key:
                split_value = dictionary[key].replace(",", "").split(" ")
                split_length = len(split_value)
                if element[1] == "" or split_value[0] == element[1]:
                    if element[2] == "" or (split_value[0] != element[2] and element[2] in split_value) or (
                            split_value[0] == element[2] and element[2] in split_value):
                        if element[3] == "" or split_value[split_length - 1] - element[3]:
                            continue
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
    return True


# print(ex_5({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}, key1="come inside, it's too cold out",
#            key3="this is not valid"))


def ex_6(param_list):
    # Write a function that receives as a parameter a list and returns a tuple (a, b),
    # representing the number of unique elements in the list, and b representing the number
    # of duplicate elements in the list (use sets to achieve this objective).
    a = list(filter(lambda element: param_list.count(element) == 1, param_list))
    b = set(filter(lambda element: param_list.count(element) > 1, param_list))
    return len(a), len(b)


# print(ex_6(['Ana', 'are', 'Ana', 'Ana', 'are', 'pere']))

def set_item(element1, element2, dictionary):
    if element1 != element2 and (str(element2) + '|' + str(element1)) not in dictionary.keys():
        dictionary.setdefault(str(element1) + '|' + str(element2), element1 | element2)
        dictionary.setdefault(str(element1) + '&' + str(element2), element1 & element2)
        dictionary.setdefault(str(element1) + '-' + str(element2), element1 - element2)
    return dictionary


def ex_7(*sets):
    # Write a function that receives a variable number of sets and returns a dictionary with the
    # following operations from all sets two by two: reunion, intersection, a-b, b-a. The key will
    # have the following form: "a op b", where a and b are two sets, and op is the applied operator: |, &, -.
    # Ex: {1,2}, {2, 3} =>
    # {
    # "{1, 2} | {2, 3}":  {1, 2, 3},
    # "{1, 2} & {2, 3}":  { 2 },
    #  "{1, 2} - {2, 3}":  { 1 },
    #  ...
    # }
    dictionary = dict()
    for element1 in sets:
        for element2 in sets:
            dictionary = set_item(element1, element2, dictionary).copy()
    return dictionary


# print(ex_7({1, 2}, {2, 3}))


def ex_8(loop):
    # Write a function that receives a single dict parameter named mapping.
    # This dictionary always contains a string key "start".
    # Starting with the value of this key you must obtain a list of objects by iterating
    # over mapping in the following way: the value of the current key is the key for the next value,
    # until you find a loop (a key that was visited before).
    # The function must return the list of objects obtained as previously described.
    # Ex: loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'})
    # will return ['a', '6', 'z', '2']
    result = []
    stop = False
    current_key = 'start'
    while not stop:
        if loop[current_key] in loop.keys() and loop[current_key] not in result:
            current_key = loop[current_key]
            result.append(current_key)
        elif loop[current_key] not in loop.keys() or loop[current_key] in result:
            stop = True
    return result


# print(ex_8({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))


def ex_9(*positional_args, **keyword_args):
    # Write a function that receives a variable number of positional arguments and a variable number
    # of keyword arguments adn will return the number of positional arguments whose values can be found
    # among keyword arguments values.
    # Ex: my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5) will return returna 3
    return [position for position in positional_args if position in keyword_args.values()].__len__()

# print(ex_9(1, 2, 3, 4, x=1, y=2, z=3, w=5))
