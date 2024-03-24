
"""
Write a Python class, Flower, that has three instance variables of type str,
int, and float, that respectively represent the name of the flower, its number
of petals, and its price. Your class must include a constructor method
that initializes each variable to an appropriate value, and your class should
include methods for setting the value of each type, and retrieving the value
of each type.
"""

class Flower():
    def __init__(self, name = None, petals = None, price = None):
        self._name = self._petals = self._price = None

        self.set_name(name)
        self.set_petals(petals)
        self.set_price(price)

    def set_name(self, name):
        try:
            self._name = str(name)
        except:
            print("Invalid input for a name")
    
    def set_petals(self, petals):
        try:
            self._petals = petals
        except:
            print("invalid input petals")

    def set_price(self, price):
        if price is not None:
            try:
                self._price = float(price)
            except:
                print("Invalid price")
    
    def get_name(self):
        if self._name is None: 
            return ('Attributes has not been set')
        else:
            return self._name
    
    def get_price(self):
        if self._price is  None:
            return ('attributes has not been set')
        else:
            return self._price
        
    def get_petals(self):
        if self._petals is None:
            return ('Attributes has not been set')
        else:
            return self._petals



palesa = Flower('Dandelion', 5, 'R20.34')
print(palesa.get_name(), palesa.get_petals(), palesa.get_price())

print('\n')

rose = Flower()
print(rose.get_name(), rose.get_petals(), rose.get_price())

rose.set_name("Palesa")
rose.set_price(30)
rose.set_petals(20)
print(rose.get_name(), rose.get_petals(), rose.get_price())