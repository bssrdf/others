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
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'self'):
            cls.self = object.__new__(cls)
        return cls.self

class Restaurant(Singleton):
    def __init__(self, s):
        self.s = s

if __name__ == '__main__':
    for pizza_type in ('HamMushroom', 'Deluxe', 'Hawaiian'):
        print 'Price of {0} is {1}'.format(pizza_type, PizzaFactory.create_pizza(pizza_type).get_price())
    #Usage
    mySingleton1 = Restaurant('Inka Mama')
    mySingleton2 = Restaurant('Thai')
 
    print mySingleton1 is mySingleton2
    print mySingleton1.s
    print mySingleton2.s
    #mySingleton1 and  mySingleton2 are the same instance.
