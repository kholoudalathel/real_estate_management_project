
from models.person import Person  # Importing the base class

class Buyer(Person):
    def __init__(self, name: str, budget: float):
        super().__init__(name)
        self.__budget = budget  #private attribute

    def can_afford(self, property_price: float) -> bool:
        return self.__budget >= property_price

    def purchase(self, amount: float):
        if self.can_afford(amount):
            self.__budget -= amount
            return True
        return False

    def get_budget(self): #add a getter cz its a private attribute
        return self.__budget

    def __str__(self):
        return f"Buyer: {self._name}, Budget: ${self.__budget}"