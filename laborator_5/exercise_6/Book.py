from LibraryItem import LibraryItem


class Book(LibraryItem):
    def __init__(self, title, author, item_id, in_stock, check_out_number, pages):
        super().__init__(title, author, item_id, in_stock, check_out_number)
        self.pages = pages

    def display_info(self):
        super().show_information()
        print(f"Number of Pages: {self.pages}\n")
