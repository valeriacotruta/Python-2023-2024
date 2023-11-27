import csv
from .Rules import *

class CSVValidator:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = []
        self.header = []

    def read_csv(self):
        try:
            csv_file = open(self.file_path, 'r', newline='')
            reader = csv.reader(csv_file)
            self.header = next(reader)
            self.data = [row for row in reader]
            print(self.data)
            return True
        except FileNotFoundError:
            print("File " + self.file_path + " not found.")
        except Exception as e:
            print(str(e))

    def validate(self, rules):
        try:
            for index, row in enumerate(self.data, start=1):
                for column_index, text in enumerate(row):
                    if "is_empty" in rules or "is_integer" in rules:
                        if self.header[column_index] in 'Name, Email' and not is_empty(text):
                            raise TypeError(f"Row {index}, Column {self.header[column_index]}: Invalid value '{text}'")
                        if self.header[column_index] == 'Age' and not is_integer(text):
                            raise TypeError(f"Row {index}, Column {self.header[column_index]}: Invalid value '{text}'")
            return "Everything is fine!"
        except (TypeError, Exception) as e:
            return e
