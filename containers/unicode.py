import unicodedata


class NormalizedStr:
    '''
    By default, Python's str type stores any valid unicode string.
    This can result in unintuitive behavior.
    For example:

    >>> 'César' in 'César Chávez'
    True
    >>> 'César' in 'César Chávez'
    False

    The two strings to the right of the in keyword above are equal *semantically*,
    but not equal *representationally*.
    In particular, the first is in NFC form, and the second is in NFD form.
    The purpose of this class is to automatically normalize our strings for us,
    making foreign languages "just work" a little bit easier.
    '''

    def __init__(self, text, normal_form='NFC'):
        pass

    def __repr__(self):
        '''
        The string returned by the __repr__ function should be valid python code
        that can be substituted directly into the python interpreter to reproduce an equivalent object.
        '''

    def __str__(self):
        '''
        This functions converts the NormalizedStr into a regular string object.
        The output is similar, but not exactly the same, as the __repr__ function.
        '''

    def __len__(self):
        pass

    def __contains__(self, elem):
        pass

    def __getitem__(self, index):
        pass

    def lower(self):
        '''
        Returns a copy in the same normalized form, but lower case.
        '''

    def upper(self):
        '''
        Returns a copy in the same normalized form, but upper case.
        '''

    def __add__(self, b):
        '''
        HINT:
        The addition of two normalized strings is not guaranteed to stay normalized.
        Therefore, you must renormalize the strings after adding them together.
        '''

    def __iter__(self):
        '''
        HINT:
        Recall that the __iter__ method returns a class, which is the iterator object.
        You'll need to define your own iterator class with the appropriate magic methods to get returned here.
        '''
