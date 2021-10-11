#!/usr/bin/python3
class MyInt(int):
    """ This class inherits from class int"""

    def __eq__(self, other):
        """ This method returns != check """
        return (int.__ne__(self, other))

    def __ne__(self, other):
        """ This method that returns == check """
        return (int.__eq__(self, other))
