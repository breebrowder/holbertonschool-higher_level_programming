#!/usr/bin/python3
""" Writing class MyInt that inherits from Int """


class MyInt(int):
    """ Method to define the equality logic for comparing two objects(==) """
    def __eq__(self, int):
        """ if __eq__, return not equal """
        return super().__ne__(int)

    def __ne__(self, int):
        """ if __ne__, return equal """
        return super().__eq__(int)
