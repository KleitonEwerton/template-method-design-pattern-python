from abc import ABC, abstractmethod
class BeverageMaker(ABC):
    # Template method defining the overall process
    def make_beverage(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    # Common methods
    def boil_water(self):
        print("Boiling water")

    def pour_in_cup(self):
        print("Pouring into cup")

    # Abstract methods to be implemented by subclasses
    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def add_condiments(self):
        pass