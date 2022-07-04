#!/usr/bin/python3

class MyList(list):
    """ This class inherits from list"""

    def print_sorted(self):
        """the method prints a list in ascending order """
        print(sorted(self))
