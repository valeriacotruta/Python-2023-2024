import numpy as np
from itertools import product


def ex_0(number):
    # scrieti un algoritm care calculeaza suma primelor n numere naturale
    return sum(range(1, number + 1))


# print(ex_0(int(input())))

def ex_1(start_char, num_elements):
    # generati codurile ascii in format hex string pentru un range de litere successive
    #    range-ul este dat de primul caracter, si numarul de elemente care incepe cu primul caracter
    #    ex: pentru {'0'....'9'} se va afisa '30 31 32 33 34 35 36 37 38 39'
    #    ex: pentru {'a'....'z'} se va afisa '61 62 63 64 65 66 67 68 69 6a 6b 6c 6d 6e 6f 70 71 72 73 74 75 76 77 78 79 7a'
    #    ex: pentru {'A'....'Z'} se va afisa '41 42 43 44 45 46 47 48 49 4a 4b 4c 4d 4e 4f 50 51 52 53 54 55 56 57 58 59 5a'
    result = ''
    result += ' '.join(hex(index)[2:] for index in range(ord(start_char), ord(start_char) + num_elements - 1))
    return result


# print(ex_1('0', 10))

def ex_2(set_of_numbers):
    # generati secventa de 8 biti pentru a reprezenta o succesiune de numere, si afisati si numarul de caractere 0 si 1
    #    ex: pentru {0,1,2,3,4} se va afisa '00000000 00000001 00000010 00000011 00000100', 35, 5
    result = ''
    for index in set_of_numbers:
        result += ''.join(add_zero(bin(index)[2:]))
    return result, result.count('0'), result.count('1')


def add_zero(number):
    length = number.__len__()
    result = ' '
    for index in range(8 - length):
        result += '0'
    return result + ''.join(number)


# print(ex_2({0, 1, 2, 3, 4}))

def ex_3(first_number, second_number):
    # scrieti un algoritm care calculeaza rezultatul unei impartiri cu virgula, folosind doar numere intregi
    #    rezultatul se va afisa cu 100 de zecimale
    result = first_number * 10 ** 100
    result //= second_number  # //= --> (floor division)
    return str(result)[:-100] + "." + str(result)[-100:]


# print(ex_3(2,3))

def ex_4(matrix, results):
    # scrieti un program care calculeaza solutiile unui sistem de ecuatii de grad 1 cu cel mult 4 necunoscute
    return np.linalg.solve(matrix, results)


matrix = np.array([[2, 3, 4, 5],
                   [1, -2, 2, -1],
                   [0, 1, -3, 2],
                   [4, 0, 6, -7]])
results = np.array([10, 3, 5, 12])


# print(ex_4(matrix, results))


def ex_5(n, number):
    # scrieti un algoritm care implementeaza radacina de ordin n dintr-un numar dat, cu 50 de zecimale,
    #  utilizand doar calcule cu numere intregi, dupa algorimtul prezentat aici: https://en.wikipedia.org/wiki/Nth_root
    result = number ** (1 / n)
    return


print(ex_5(2, 8))


def ex_6(length, alphabet):
    # Generati permutrea n pentru cuvinte cu p litre folosind un alfabet dat, n < len(alfabet)^p
    if length == 0:
        return None
    result = ''
    for permutation in product(alphabet, repeat=length):
        result += ''.join(permutation)
        result += ' '
    return result

alphabet = 'ABC'
length = 2
print(ex_6(length, alphabet))


def ex_7():
    #  Generati matrici de biti 0/1 compacte 8x16, pornind de la reprezentarea hex a unor numere
    #    matricile vor fi afisate unele sub altele
    matrix = [[0x00, 0x00, 0xFC, 0x66, 0x66, 0x66, 0x7C, 0x60, 0x60, 0x60, 0x60, 0xF0, 0x00, 0x00, 0x00, 0x00],
              [0x00, 0x00, 0x10, 0x30, 0x30, 0xFC, 0x30, 0x30, 0x30, 0x30, 0x36, 0x1C, 0x00, 0x00, 0x00, 0x00],
              [0x00, 0x00, 0x00, 0x00, 0x00, 0xC6, 0xC6, 0xC6, 0xC6, 0xC6, 0xC6, 0x7E, 0x06, 0x0C, 0xF8, 0x00],
              [0x00, 0x00, 0xE0, 0x60, 0x60, 0x6C, 0x76, 0x66, 0x66, 0x66, 0x66, 0xE6, 0x00, 0x00, 0x00, 0x00],
              [0x00, 0x00, 0x00, 0x00, 0x00, 0x7C, 0xC6, 0xC6, 0xC6, 0xC6, 0xC6, 0x7C, 0x00, 0x00, 0x00, 0x00],
              [0x00, 0x00, 0x00, 0x00, 0x00, 0xDC, 0x66, 0x66, 0x66, 0x66, 0x66, 0x66, 0x00, 0x00, 0x00, 0x00]]
    for index in range(6):
        for index1 in range(16):
            print(add_zero(bin(matrix[index][index1])[2:]))
        print()

# ex_7()
