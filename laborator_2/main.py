def fib(number):
    # Write a function to return a list of the first n numbers in the Fibonacci string.
    if number == 0 or number == 1:
        return number
    return fib(number - 1) + fib(number - 2)


def ex_1(n):
    return ','.join(str(fib(index)) for index in range(n))


# print(ex_1(8))


def ex_2(list):
    # Write a function that receives a list of numbers and returns a list of the prime numbers found in it.
    return ''.join(f'{str(index) + " " if index % 2 == 0 else ""}' for index in list)


# print(ex_2([4, 2, 3]))


def ex_3(a, b):
    # Write a function that receives as parameters two
    # lists a and b and returns: (a intersected with b, a reunited with b, a - b, b - a)
    return list(filter(lambda element: element in a and element in b, a)), list(a + b), \
           list(filter(lambda element: element in a and not element in b, a)), \
           list(filter(lambda element: not element in a and element in b, b))


# print(ex_3([1, 2, 3], [3, 4, 1]))

def ex_4(notes, moves, start_position):
    # Write a function that receives as a parameters a list of musical notes (strings),
    # a list of moves (integers) and a start position (integer).
    # The function will return the song composed by going though the musical notes beginning with the start position
    # and following the moves given as parameter.
    # Example : compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2) will return ["mi", "fa", "do", "sol", "re"]
    list = [notes[start_position]]
    for index in range(moves.__len__()):
        start_position += moves[index]
        note = notes[start_position]
        list += [note]
    return list


# print(ex_4(["do", "re", "mi", "fa", "sol"], [1, -3, 4, -3], 2))


def ex_5(matrix):
    # Write a function that receives as parameter a matrix and will return
    # the matrix obtained by replacing all the elements under the main diagonal with 0 (zero).
    for row in range(matrix.__len__()):
        matrix[row][row] = 0
    print(matrix)


# ex_5([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


def ex_6(repeated, *lists):
    # Write a function that receives as a parameter a variable number of lists and a whole number x.
    # Return a list containing the items that appear exactly x times in the incoming lists.
    # Example: For the [1,2,3], [2,3,4],[4,5,6], [4,1, "test"]
    # and x = 2 lists [1,2,3 ] # 1 is in list 1 and 4, 2 is in list 1 and 2, 3 is in lists 1 and 2.
    all_the_elements = []
    for l in lists:
        all_the_elements += l
    print(list(set(filter(lambda element: all_the_elements.count(element) == repeated, all_the_elements))))


# ex_6(2, [1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"])


def ex_7(list_of_numbers):
    # Write a function that receives as parameter a list of numbers (integers)
    # and will return a tuple with 2 elements. The first element of the tuple will
    # be the number of palindrome numbers found in the list and the second element
    # will be the greatest palindrome number.
    palindrome_list = list(filter(lambda element: str(element)[::-1] == str(element), list_of_numbers))
    print("palindrome_list:", palindrome_list)
    return palindrome_list.__len__(), max(palindrome_list)


# print(ex_7([1, 12, 22, 344, 343, 32323]))

def ex_8(x=1, string_list=[], flag=True):
    # Write a function that receives a number x, default value equal to 1,
    # a list of strings, and a boolean flag set to True. For each string,
    # generate a list containing the characters that have the ASCII code
    # divisible by x if the flag is set to True, otherwise it should contain
    # characters that have the ASCII code not divisible by x.
    #  Example: x = 2, ["test", "hello", "lab002"],
    #  flag = False will return (["e", "s"], ["e" . Note: The function must return list of lists.
    strings = []
    for string in string_list:
        if flag:
            strings += [list(filter(lambda character: ord(character) % x == 0 and character in string, string))]
        else:
            strings += [list(filter(lambda character: ord(character) % x != 0 and character in string, string))]
    print(strings)


# ex_8(2, ["test", "hello", "lab002"], False)


def ex_9(matrix):
    # Write a function that receives as paramer a matrix which represents the heights of the spectators
    # in a stadium and will return a list of tuples (line, column) each one representing a seat of a
    # spectator which can't see the game. A spectator can't see the game if there is at least one taller
    # spectator standing in front of him. All the seats are occupied. All the seats are at the same level.
    # Row and column indexing starts from 0, beginning with the closest row from the field.
    # Example:
    # FIELD
    # [[1, 2, 3, 2, 1, 1],
    # [2, 4, 4, 3, 7, 2],
    # [5, 5, 2, 5, 6, 4],
    # [6, 6, 7, 6, 7, 5]]
    # Will return : [(2, 2), (3, 4), (2, 4)]
    cant_see_spectators_list = []
    rows = len(matrix)
    columns = len(matrix[0])

    for row in range(rows):
        for column in range(columns):
            spectator_height = matrix[row][column]

            for index in range(row + 1, rows):
                if matrix[index][column] >= spectator_height:
                    cant_see_spectators_list.append((row, column))
                    break

    return cant_see_spectators_list


stadium = [
    [1, 2, 3, 2, 1, 1],
    [2, 4, 4, 3, 7, 2],
    [5, 5, 2, 5, 6, 4],
    [6, 6, 7, 6, 7, 5]
]

# print(ex_9(stadium))


def ex_10(*input_lists):
    # Write a function that receives a variable number of lists and returns a list of tuples as follows:
    # the first tuple contains the first items in the lists, the second element contains the items on the position 2
    # in the lists, etc. Ex: for lists [1,2,3], [5,6,7], ["a", "b", "c"] return: [(1, 5, "a ") ,(2, 6, "b"), (3,7, "c")].
    # Note: If input lists do not have the same number of items, missing items will be replaced with None to be able to
    # generate max ([len(x) for x in input_lists]) tuples.
    max_input_lists_length = max([len(x) for x in input_lists])
    irregular_lists = list(filter(lambda element: element.__len__() != max_input_lists_length, input_lists))
    processed_lists = list(
        map(lambda element: [element.append(None) for index in range(max_input_lists_length - element.__len__())],
            irregular_lists))
    tuples = list(zip(*input_lists))
    print(tuples)


# ex_10([1, 2, 3], [5, 6, 7], ['a', 'b', 'c'])
# ex_10([1, 2, 3], [5, 6, 7, 8], ['a', 'b', 'c'])

def sortedByACharacter(tuple):
    first_element, second_element = tuple
    return second_element[2]


def ex_11(list_of_tuples):
    # Write a function that will order a list of string tuples based on the 3rd character
    # of the 2nd element in the tuple. Example: ('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]
    list_of_tuples.sort(key=sortedByACharacter)
    print("sorted:", list_of_tuples)


# ex_11([('abc', 'bcd'), ('abc', 'zza')])
# ex_11([('abc', 'bcd'), ('abc', 'zza'), ('abc', 'bcf')])

def isRepeated(el, list):
    if list.count(el) > 1:
        list.remove(el)
    return list


def ex_12(words_list):
    # Write a function that will receive a list of words  as parameter and will return a list of lists of words,
    # grouped by rhyme. Two words rhyme if both of them end with the same 2 letters.
    # 	Example:
    # group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']) will return [['ana', 'banana'], ['carte', 'parte'], ['arme']]
    returned_list = list(
        map(lambda word: list(filter(lambda element: element[-2:] == word[-2:], words_list)), words_list))
    print(list(map(lambda element: isRepeated(element, returned_list), returned_list))[0])

# ex_12(['ana', 'banana', 'carte', 'fata', 'baiat', 'arme', 'parte'])
