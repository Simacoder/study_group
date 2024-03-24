""" chapter 2
exercise 2.4 

R-2.4 Write a Python class, Flower, that has three instance variables of type str,
int, and float, that respectively represent the name of the flower, its number
of petals, and its price. Your class must include a constructor method
that initializes each variable to an appropriate value, and your class should
include methods for setting the value of each type, and retrieving the value
of each type.

"""

from ast import Num


class Flower:
    def __init__(self, name: str, n_petals: int, price: Num) -> None:
        self._name = name
        self._n_petals = n_petals
        self._price = price

    def get_name(self) -> str:
        '''get flower name'''
        return self._name

    def set_name(self, name: str) -> None:
        '''set flower name'''
        self._name = name

    def get_n_petals(self) -> int:
        '''get the num of flower'petrals'''
        return self._n_petals

    def set_n_petals(self, n_petals: int) -> None:
        '''set the num of flower'petrals'''
        self._n_petals = n_petals

    def get_price(self) -> Num:
        '''get flower price'''
        return self._price

    def set_price(self, price) -> None:
        '''set flower price'''
        self._price = price


    