from rental import Rental
from movie import Movie
from typing import List
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
        self.rentals: List(Rental) = []

    def add_rental(self, rental: Rental):
        """Add a rental for this customer"""
        if rental not in self.rentals:
            self.rentals.append(rental)
    
    def get_name(self):
        return self.name
    
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
            amount = rental.get_charge()
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