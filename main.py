from models.buyer import Buyer
from models.landlord import Landlord
from models.real_estate_property import Property
from services.real_estate_service import RealEstateService

def main():
    # Create instances
    buyer = Buyer("Yara", 120000)
    landlord = Landlord("Leena")
    property1 = Property("222 Malqa", 100000)
    property2 = Property("555 Olaya", 150000)

    # Add properties to landlord
    landlord.add_property(property1)
    landlord.add_property(property2)

    # Show initial state
    print(landlord)
    print(buyer)

    # Attempt to purchase properties
    result1 = RealEstateService.purchase_property(buyer, landlord, property1)
    print(result1)
    print(landlord)
    print(buyer)

    result2 = RealEstateService.purchase_property(buyer, landlord, property2)
    print(result2)

if __name__ == "__main__":
    main()