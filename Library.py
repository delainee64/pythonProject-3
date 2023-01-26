# Author: Delainee Lenss
# GitHub username: delainee64
# Date: 01/22/2023
# Description: You will be writing a Library simulator involving multiple classes.
# You will write the LibraryItem, Patron and Library classes, and the three classes that
# inherit from LibraryItem (Book, Album and Movie).

class LibraryItem:
    """Represents a library item a patron can check out."""
    def __init__(self, library_item_id, title):
        self._library_item_id = library_item_id
        self._title = title
        self._location = "ON_SHELF"
        self._checked_out_by = None
        self._requested_by = None
        self._date_checked_out = 0

    def get_library_item_id(self):
        """Returns a library item's id number."""
        return self._library_item_id

    def get_title(self):
        """Returns a title."""
        return self._title

    def get_location(self):
        """Returns a location of a library item."""
        return self._location

    def set_location(self, location):
        """Sets the location of the library item."""
        self._location = location

    def get_checked_out_by(self):
        """Returns who the item is checked out by."""
        return self._checked_out_by

    def set_checked_out_by(self, patron):
        """Sets all items checked out by a patron."""
        self._checked_out_by = patron

    def get_requested_by(self):
        """Returns the patron an item is requested by."""
        return self._requested_by

    def set_requested_by(self, patron):
        """Sets the patron who requested an item."""
        self._requested_by = patron

    def get_date_checked_out(self):
        """Returns the date an item was checked out."""
        return self._date_checked_out

    def set_date_checked_out(self, current_date):
        """Sets the current date to when an item was checked out."""
        self._date_checked_out = current_date


class Book(LibraryItem):
    """Represents a book in the library and inherits information from LibraryItem."""

    def __init__(self, library_item_id, title, author):
        super().__init__(library_item_id, title)
        self._author = author

    def get_author(self):
        """Returns the name of the author."""
        return self._author

    def get_check_out_length(self):
        """Returns the max number of days a book can be checked out."""
        return 21


class Album(LibraryItem):
    """Represents an album in the library and inherits information from LibraryItem."""

    def __init__(self, library_item_id, title, artist):
        super().__init__(library_item_id, title)
        self._artist = artist

    def get_artist(self):
        """Returns the name of the artist."""
        return self._artist

    def get_check_out_length(self):
        """Returns the max number of days an album can be checked out."""
        return 14


class Movie(LibraryItem):
    """Represents a movie in the library and inherits information from LibraryItem."""

    def __init__(self, library_item_id, title, director):
        super().__init__(library_item_id, title)
        self._director = director

    def get_director(self):
        """Returns the name of the director."""
        return self._director

    def get_check_out_length(self):
        """Returns the max number of days a movie can be checked out."""
        return 7


class Patron:
    """Represents a member of the library."""

    def __init__(self, patron_id, name):
        self._patron_id = patron_id
        self._name = name
        self._checked_out_items = []
        self._fine_amount = 0.0

    def get_patron_id(self):
        """Returns the patron's id number."""
        return self._patron_id

    def get_name(self):
        """Returns the patron's name."""
        return self._name

    def get_checked_out_items(self):
        """Returns the items checked out by a patron."""
        return self._checked_out_items

    def get_fine_amount(self):
        """Returns the patron's fine amount."""
        return self._fine_amount

    def add_library_item(self, item):
        """Adds a library item to a patron's account they have checked out."""
        self._checked_out_items.append(item)

    def remove_library_item(self, item):
        """Removes a library item from a patron's account once they return it."""
        self._checked_out_items.remove(item)

    def amend_fine(self, amount):
        """Calculates a new fine amount once a payment is made."""
        self._fine_amount += amount


class Library:
    """Represents a library that contains various library items."""

    def __init__(self):
        self._holdings = []
        self._members = []
        self._current_date = 0

    def get_holdings(self):
        """Returns a collection of library items."""
        return self._holdings

    def get_members(self):
        """Returns a collection of library members."""
        return self._members

    def get_current_date(self):
        """Returns the current date."""
        return self._current_date

    def add_library_item(self, item):
        """Adds a new library item to holdings."""
        self._holdings.append(item)

    def remove_library_item(self, item):
        """Removes a library item from holdings."""
        self._holdings.remove(item)

    def add_patron(self, patron):
        """Adds a new member to the library."""
        self._members.append(patron)

    def lookup_library_item_from_id(self, library_item_id):
        """Returns whether the library item is in the holdings."""
        for library_item_id in self._holdings:
            if library_item_id.get_library_id_code() == library_item_id:
                return library_item_id
        return None

    def lookup_patron_from_id(self, patron_id):
        """Returns the patron associated with a patron id."""
        for patron in self._members:
            if patron.get_patron_id() == patron_id:
                return patron_id
        return None

    def check_out_library_item(self, patron_id, library_item_id):
        """Allows a library item to be checked out and the data stored properly."""
        for patron in self._members:
            if patron.get_patron_id() == patron_id:
                for item in self._holdings:
                    if item.get_library_item_id() == library_item_id:
                        if item.get_location() == "CHECKED_OUT":
                            print("item already checked out")
                            break
                        elif item.get_location() == "ON_HOLD_SHELF":
                            print("item on hold by other patron")
                            break
                        else:
                            item.set_checked_out_by(patron)
                            item.set_date_checked_out(self._current_date)
                            item.set_location("CHECKED_OUT")
                            if item.get_requested_by() == patron:
                                item.set_requested_by(None)
                            patron.add_library_item(item)
                            print("check out successful")
                            break
                else:
                    print("item not found")
                break
        else:
            print("patron not found")

    def return_library_item(self, library_item_id):
        """Returns a library item to the library."""
        for item in self._holdings:
            if item.get_check_out_length() == library_item_id:
                if item.get_location() != "CHECKED_OUT":
                    print("item already in library")
                    break
                elif item.get_location() == "CHECKED_OUT":
                    item.get_checked_out_by().remove_library_item(item)
                    if item.get_check_out_length() != None:
                        item.set_location("ON_HOLD_SHELF")
                    else:
                        item.set_location("ON_SHELF")
                        item.set_checked_out_by(None)
                        print("return successful")
                        break
                break
        else:
            print("item not found")

    def request_library_item(self, patron_id, library_item_id):
        """Places items on hold for members of the library."""
        for patron in self._members:
            if patron.get_patron_id() == patron_id:
                for item in self._holdings:
                    if item.get_library_item_id() == library_item_id:
                        if item.get_location() == "CHECKED_OUT":
                            print("item already checked out")
                        elif item.get_location() == "ON_HOLD_SHELF":
                            print("item already on hold")
                            break
                        else:
                            item.set_requested_by(patron)
                            item.set_location("ON_HOLD_SHELF")
                            print("request successful")
                        break
                else:
                    print("item not found")
                break
        else:
            print("patron not found")

    def pay_fine(self, patron_id, amount):
        """Allows a patron to pay their fine."""
        for patron in self._members:
            if patron.get_patron_id() == patron_id:
                patron.amend_fine(-amount)
                print("payment successful")
                break
        else:
            print("patron not found")

    def increment_current_date(self):
        """Adds the correct fine for every day an item is past due."""
        self._current_date = self._current_date + 1
        for item in self._holdings:
            if self._current_date - item.get_date_checked_out() > item.get_check_out_length():
                for patron in self._members:
                    for item_of_patron in patron.get_checked_out_items():
                        if item_of_patron == item:
                            patron.amend_fine(0.10)


# def main():

    # b1 = Book("345", "Phantom Tollbooth", "Juster")
    # a1 = Album("456", "...And His Orchestra", "The Fastbacks")
    # m1 = Movie("567", "Laputa", "Miyazaki")
    # print(b1.get_author())
    # print(a1.get_artist())
    # print(m1.get_director())

    # p1 = Patron("abc", "Felicity")
    # p2 = Patron("bcd", "Waldo")

    # lib = Library()
    # lib.add_library_item(b1)
    # lib.add_library_item(a1)
    # lib.add_patron(p1)
    # lib.add_patron(p2)

    # lib.check_out_library_item("bcd", "456")
    # for _ in range(7):
        # lib.increment_current_date()  # 7 days pass
    # lib.check_out_library_item("abc", "567")
    # loc = a1.get_location()
    # lib.request_library_item("abc", "456")
    # for _ in range(57):
        # lib.increment_current_date()  # 57 days pass
    # p2_fine = p2.get_fine_amount()
    # lib.pay_fine("bcd", p2_fine)
    # lib.return_library_item("456")


# if __name__ == '__main__':
    # main()