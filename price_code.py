from enum import Enum

class PriceCode(Enum):
    """An enumeration for different kinds of movies and their behavior"""
    new_release = { 
        "price_code": 1,
        "price": lambda days: 3.0*days, 
        "frp": lambda days: 2 if days > 1 else 1
    }
    regular = {
        "price_code": 0,
        "price": lambda days: 2.0 + 1.5*(days-2) if days > 2 else 2.0,
        "frp": lambda days: 1
    }
    childrens = {
        "price_code": 2,
        "price": lambda days: 1.5 + 1.5*(days-3) if days > 3 else 1.5,
        "frp": lambda days: 1
    }

    def get_price_code(self) -> int:
        """returns the price code of the movie enum"""
        return self.value["price_code"]

    def get_price(self, days: int) -> float:
        """Return the rental price for a given number of days"""
        pricing = self.value["price"]    # the enum member's price formula
        return pricing(days)

    def get_frequent_renter_points(self, days: int) -> int:
        """returns the renter points"""
        points = self.value["frp"]
        return int(points(days))