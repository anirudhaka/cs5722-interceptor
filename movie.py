import logging

class Movie:
    """
    A movie available for rent.
    """
    # The types of movies (price_code). 
    REGULAR = 0
    NEW_RELEASE = 1
    CHILDRENS = 2
    
    def __init__(self, title, price_code):
        # Initialize a new movie. 
        self.title = title
        self.price_code = price_code

    def get_price_code(self):
        # get the price code
        return self.price_code
    
    def get_title(self):
        return self.title
    
    def __str__(self):
        return self.title

    def get_charge(self, days_rented: int) -> float:
        result = 0
        if self.get_price_code() == Movie.REGULAR:
            # Two days for $2, additional days 1.50 each.
            result = 2.0
            if days_rented > 2:
                result += 1.5*(days_rented-2)
        elif self.get_price_code() == Movie.CHILDRENS:
            # Three days for $1.50, additional days 1.50 each.
            result = 1.5
            if days_rented > 3:
                result += 1.5*(days_rented-3)
        elif self.get_price_code() == Movie.NEW_RELEASE:
            # Straight per day charge
            result = 3*days_rented
        else:
            log = logging.getLogger()
            log.error(f"Movie {self} has unrecognized priceCode {self.get_price_code()}")
        
        return result

    def get_frequent_renter_points(self, days_rented: int) -> int:
        if (self.get_price_code() == Movie.NEW_RELEASE) and (days_rented > 1):
            return 2
        else:
            return 1
