# Factory Method
#
# Pizza
#
class Pizza(object):
    def __init__(self):
        self._price = None
    def get_price(self):
        return self._price
class HamAndMushroomPizza(Pizza):
    def __init__(self):
        self._price = 8.5
class DeluxePizza(Pizza):
    def __init__(self):
        self._price = 10.5
class HawaiianPizza(Pizza):
    def __init__(self):
        self._price = 11.5
#
# PizzaFactory
#
class PizzaFactory(object):
    @staticmethod
    def create_pizza(pizza_type):
        if pizza_type == 'HamMushroom':
            return HamAndMushroomPizza()
        elif pizza_type == 'Deluxe':
            return DeluxePizza()
        elif pizza_type == 'Hawaiian':
            return HawaiianPizza()


# Singleton
class Singleton(object):
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            cls.__instance.__initialized = False
        return cls.__instance

    def __init__(self, s):
        if (self.__initialized): return
        self.__initialized = True
        self.s = s

if __name__ == '__main__':
    for pizza_type in ('HamMushroom', 'Deluxe', 'Hawaiian'):
        print 'Price of {0} is {1}'.format(pizza_type, PizzaFactory.create_pizza(pizza_type).get_price())
    #Usage
    mySingleton1 = Singleton('Inka Mama')
    mySingleton2 = Singleton('Thai')
 
    print mySingleton1 is mySingleton2
    print mySingleton1.s
    print mySingleton2.s
    #mySingleton1 and  mySingleton2 are the same instance.
