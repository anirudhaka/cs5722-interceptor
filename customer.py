from rental import Rental
from movie import Movie
import logging

class Customer:
    """A customer who rents movies.

    The customer object holds information about the
    movies rented for the current billing period,
    and can print a statement of his rentals.
    """

    def __init__(self, name: str):
        """Initialize a new customer."""
        self.name = name
        self.rentals = []

    def add_rental(self, rental: Rental):
        """Add a rental for this customer"""
        if rental not in self.rentals:
            self.rentals.append(rental)
    
    def get_name(self):
        return self.name
    
    @staticmethod
    def amount_for(a_rental: Rental):
        """
        returns the amount for a given rental type
        """
        result = 0
        if a_rental.get_movie().get_price_code() == Movie.REGULAR:
            # Two days for $2, additional days 1.50 each.
            result = 2.0
            if a_rental.get_days_rented() > 2:
                result += 1.5*(a_rental.get_days_rented()-2)
        elif a_rental.get_movie().get_price_code() == Movie.CHILDRENS:
            # Three days for $1.50, additional days 1.50 each.
            result = 1.5
            if a_rental.get_days_rented() > 3:
                result += 1.5*(a_rental.get_days_rented()-3)
        elif a_rental.get_movie().get_price_code() == Movie.NEW_RELEASE:
            # Straight per day charge
            result = 3*a_rental.get_days_rented()
        else:
            log = logging.getLogger()
            log.error(f"Movie {a_rental.get_movie()} has unrecognized priceCode {a_rental.get_movie().get_price_code()}")
        
        return result

    
    def statement(self):
        """Create a statement of rentals for the current period.

        Print all the rentals in current period, 
        along with total charges and reward points.
        
        Returns:
                the statement as a String
        """
        total_amount = 0 # total charges
        frequent_renter_points = 0 
        statement = f"Rental Report for {self.name}\n\n"
        fmt = "{:40s}    {:4s} {:6s}\n"
        statement += fmt.format("Movie Title", "Days", "Price")
        fmt = "{:40s}   {:4d} {:6.2f}\n"
        
        for rental in self.rentals:
            # compute rental change
            amount = self.amount_for(rental)
            # award renter points
            if rental.get_movie().get_price_code() == Movie.NEW_RELEASE:
                frequent_renter_points += rental.get_days_rented()
            else:
                frequent_renter_points += 1
            #  add detail line to statement
            statement += fmt.format(rental.get_movie().get_title(), rental.get_days_rented(), amount)
            # and accumulate activity
            total_amount += amount

        # footer: summary of charges
        statement += "\n"
        statement += "{:40s} {:6s} {:6.2f}\n".format(
                       "Total Charges", "", total_amount)
        statement += "Frequent Renter Points earned: {}\n".format(frequent_renter_points)

        return statement