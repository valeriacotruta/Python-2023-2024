from LibraryItem import LibraryItem


class DVD(LibraryItem):
    def __init__(self, title, director, item_id, in_stock, check_out_number, duration):
        super().__init__(title, director, item_id, in_stock, check_out_number)
        self.duration = duration

    def display_info(self):
        super().show_information()
        print(f"Duration: {self.duration} minutes\n")


