class LibraryItem:
    def __init__(self, title, author, item_id, in_stock=0, check_out_number=0):
        self.title = title
        self.author = author
        self.item_id = item_id
        self.in_stock = in_stock
        self.is_available = bool(in_stock)
        self.check_out_number = check_out_number

    def show_information(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nItem id: {self.item_id}\n"
              f"Available: {self.is_available}")

    def check_out(self, check_out_number=1):
        if check_out_number <= self.in_stock and self.is_available:
            self.in_stock -= check_out_number
            self.check_out_number += check_out_number
            print(f"Checked out {check_out_number} of {self.title}. Remaining copies: {self.in_stock}")
        if check_out_number > self.in_stock and self.is_available:
            print(f"Current in the stock:{self.in_stock}.")
        if self.in_stock == 0:
            self.is_available = False
            print(f"{self.title} availability: {self.is_available}.")

    def return_item(self, number):
        if self.check_out_number != 0:
            if self.check_out_number < number:
                print(f"Number of copies currently checked out:{self.check_out_number}.")
            else:
                self.check_out_number -= number
                self.in_stock += number
                self.is_available = True
                print(f"Returned {self.title}. Remaining copies: {self.in_stock}")
        else:
            print(f"No copies of {self.title} are currently checked out.")
