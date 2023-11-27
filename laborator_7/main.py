from exercise_1.CSVValidator import CSVValidator

csv_validator = CSVValidator(
    'G:\Facultate\An3Sem1\python_laboratoare\pregatire_partial\laborator_7\exercise_1\csv_file.csv')

if csv_validator.read_csv():
    rules = ['is_empty', 'is_integer']
    print(csv_validator.validate(rules))

print()

from exercise_2.ArithmeticOperations import add, subtract, multiply, divide

print("Integer results:")
print("Addition:", add(5, 3))
print("Subtraction:", subtract(10, 4))
print("Multiplication:", multiply(6, 7))
print("Division:", divide(15, 3))

print("\nFloating-point results:")
print("Addition:", add(5.5, 3.2))
print("Subtraction:", subtract(10.7, 4.3))
print("Multiplication:", multiply(6.5, 7.2))
print("Division:", divide(15.6, 0.0))

from exercise_3.MergeFiles import merge_files

file_list = ['laborator_7/exercise_3/file1.txt', 'laborator_7/exercise_3/file2.txt']
print(merge_files(file_list, 'laborator_7/exercise_3/result.txt'))

from exercise_4.GeneratePasswords import generate_password

password = generate_password(10, False, True, True)
print("Generated Password:", password)
