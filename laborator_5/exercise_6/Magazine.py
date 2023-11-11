from LibraryItem import LibraryItem

class Magazine(LibraryItem):
    def __init__(self, title, author, item_id, in_stock, check_out_number, date):
        super().__init__(title, author, item_id, in_stock, check_out_number)
        self.date = date

    def display_info(self):
        super().show_information()
        print(f"Issue Date: {self.date}\n")
