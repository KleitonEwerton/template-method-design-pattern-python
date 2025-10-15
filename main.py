# Abstract class defining the template method
from TeaMaker import CoffeeMaker, TeaMaker

if __name__ == '__main__':
    print('Making tea:')
    tea_maker = TeaMaker()
    tea_maker.make_beverage()

    print('\nMaking coffee:')
    coffee_maker = CoffeeMaker()
    coffee_maker.make_beverage()