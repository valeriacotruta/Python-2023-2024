# Design a library catalog system with a base class LibraryItem and subclasses for
# different types of items like Book, DVD, and Magazine.
# Include methods to check out, return, and display information about each item.

import exercise_6 as ex_6

book = ex_6.Book("The Great Gatsby", "F. Scott Fitzgerald", "100", 5, 0, 180)
book.show_information()
book.check_out(2)
book.return_item(3)

print()
dvd = ex_6.DVD("Inception", "Christopher Nolan", "102", 100, 2, 148)
dvd.show_information()
dvd.check_out(1)
dvd.return_item(3)

print()
magazine = ex_6.Magazine("National Geographic", "National Geographic Society", "101", 0, 3, "12/12/2022")
magazine.show_information()
magazine.check_out(4)
magazine.return_item(5)
