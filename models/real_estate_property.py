class Property:
    def __init__(self, address: str, price: float):
        self.address = address
        self.price = price

    def __str__(self):
        return f"Property at {self.address}, Price: ${self.price}"
