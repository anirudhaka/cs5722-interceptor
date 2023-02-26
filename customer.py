from framework import Framework
from rental import Rental
from movie import Movie
from typing import List
import logging

class Customer(Framework):
    """A customer who rents movies.

    The customer object holds information about the
    movies rented for the current billing period,
    and can print a statement of his rentals.
    """
    APP_VERSION = "0.0.1"

    def __init__(self, name: str):
        """Initialize a new customer."""
        self.name = name
        self.rentals: List(Rental) = []
        self.context_object = None

    def add_rental(self, rental: Rental):
        """Add a rental for this customer"""
        if rental not in self.rentals:
            self.rentals.append(rental)

    def get_rentals(self):
        rentals = [rental.get_movie().get_title() for rental in self.rentals]
        return rentals
    
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
            # award renter points
            frequent_renter_points += rental.get_frequent_renter_points()
            #  add detail line to statement
            statement += fmt.format(rental.get_movie().get_title(), rental.get_days_rented(), rental.get_charge())
            # and accumulate activity
            total_amount += rental.get_charge()

        # footer: summary of charges
        statement += "\n"
        statement += "{:40s} {:6s} {:6.2f}\n".format(
                       "Total Charges", "", total_amount)
        statement += "Frequent Renter Points earned: {}\n".format(frequent_renter_points)

        return statement

    # def event(self, data):
    #     framework_obj = Framework()
    #     self.context_object = framework_obj.create_context
        