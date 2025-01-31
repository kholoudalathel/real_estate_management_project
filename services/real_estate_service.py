from models.buyer import Buyer
from models.landlord import Landlord
from models.real_estate_property import Property

class RealEstateService:
    @staticmethod
    def purchase_property(buyer: Buyer, landlord: Landlord, property_obj: Property):
        if buyer.purchase(property_obj.price):  #this represents polymorphism cz its the buyer's method
            landlord.remove_property(property_obj)
            return f"{buyer._name} bought {property_obj.address} for ${property_obj.price}"
        return f"{buyer._name} cannot afford {property_obj.address}"
