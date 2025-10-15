# Concrete subclass for making tea
from main import BeverageMaker

class TeaMaker(BeverageMaker):
    # Implementing abstract methods
    def brew(self):
        print("Steeping the tea")

    def add_condiments(self):
        print("Adding lemon")

# Concrete subclass for making coffee
class CoffeeMaker(BeverageMaker):
    # Implementing abstract methods
    def brew(self):
        print("Dripping coffee through filter")

    def add_condiments(self):
        print("Adding sugar and milk")

