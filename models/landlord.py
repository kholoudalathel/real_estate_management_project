
from models.person import Person  # Importing the base class

class Landlord(Person):
    def __init__(self, name: str):
        super().__init__(name)
        self.properties = []  # Encapsulation (storing properties)

    def add_property(self, property_obj):
        self.properties.append(property_obj)

    def remove_property(self, property_obj):
        if property_obj in self.properties:
            self.properties.remove(property_obj)

    def __str__(self):
        return f"Landlord: {self._name}, Properties: {len(self.properties)}"