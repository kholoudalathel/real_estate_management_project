
import unittest
from models.buyer import Buyer
from models.landlord import Landlord
from models.real_estate_property import Property
from services.real_estate_service import RealEstateService


class TestRealEstateService(unittest.TestCase):
    def setUp(self):
        self.buyer = Buyer("Abdullah", 100000)
        self.landlord = Landlord("Layan")
        self.property = Property("123 Hitten", 90000)
        self.landlord.add_property(self.property)

    def test_purchase_property_success(self):
        result = RealEstateService.purchase_property(self.buyer, self.landlord, self.property)
        self.assertEqual(result, "Abdullah bought 123 Hitten for $90000")

    def test_purchase_property_failure(self):
        self.buyer = Buyer("Abdullah", 50000)  # Lower budget
        result = RealEstateService.purchase_property(self.buyer, self.landlord, self.property)
        self.assertEqual(result, "Abdullah cannot afford 123 Hitten")


if __name__ == "__main__":
    unittest.main()
