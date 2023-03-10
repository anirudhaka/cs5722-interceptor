import unittest
from customer import Customer
from rental import Rental
from movie import Movie


class RentalTest(unittest.TestCase):
    
	def setUp(self):
		self.new_movie = Movie("Mulan", Movie.NEW_RELEASE)
		self.regular_movie = Movie("CitizenFour", Movie.REGULAR)
		self.childrens_movie = Movie("Frozen", Movie.CHILDRENS)

	def test_movie_attributes(self):
		"""trivial test to catch refactoring errors or change in API of Movie"""
		m = Movie("CitizenFour", Movie.REGULAR)
		self.assertEqual("CitizenFour", m.get_title())
		self.assertEqual(Movie.REGULAR, m.get_price_code())

	# @unittest.skip("TODO add this test when you refactor rental price")
	def test_rental_price(self):
		rental = Rental(self.new_movie, 1)
		self.assertEqual(rental.get_charge(), 3.0)
		rental = Rental(self.new_movie, 5)
		self.assertEqual(rental.get_charge(), 15.0)
		rental = Rental(self.regular_movie, 3)
		self.assertEqual(rental.get_charge(), 3.5)
		rental = Rental(self.childrens_movie, 7)
		self.assertEqual(rental.get_charge(), 7.5)
		# self.fail("TODO add more tests for other movie categories")

	# @unittest.skip("TODO add test of frequent renter points when you add it to Rental")
	def test_rental_points(self):
		rental = Rental(self.new_movie, 2)
		self.assertEqual(rental.get_frequent_renter_points(), 2)
		rental = Rental(self.new_movie, 1)
		self.assertEqual(rental.get_frequent_renter_points(), 1)
		rental = Rental(self.childrens_movie, 10)
		self.assertEqual(rental.get_frequent_renter_points(), 1)
		# self.fail("TODO add  test of frequent renter points")
