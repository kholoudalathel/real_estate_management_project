from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name: str):
        self._name = name  #protected attribute to represent encapsulation

    @abstractmethod  #added an abstract method to force subclasses to implement their own (abstraction)
    def __str__(self):
        pass
