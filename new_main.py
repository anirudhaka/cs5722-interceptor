from framework import Framework
from movie import Movie
from rental import Rental
from customer import Customer
from logging_interceptor import LoggingInterceptor
from statement_interceptor import SaveStatementInterceptor

def main():
    # create framework obj
    framework = Framework()

    # create a dispatcher
    dispatcher = framework.create_dispatcher()

    # applicaion creates interceptors
    logging_intrcptr = LoggingInterceptor()
    statement_intrcptr = SaveStatementInterceptor()

    # register interceptors with dispatcher
    dispatcher.register_interceptor(logging_intrcptr)
    dispatcher.register_interceptor(statement_intrcptr)

    # event occurs
    # the event is creating a new customer and adding rentals
    customer_one = Customer("Morpheus")
    customer_one.add_rental(Rental(Movie("The Matrix", Movie.REGULAR), 8))

    # create a context object for the interceptors
    ctx_obj_one = framework.create_customer_context(customer_one)

    # pass the context object to the dispatcher through the notify() method
    dispatcher.notify(ctx_obj_one)

    # event 2 occurs
    customer_two = Customer("Neo")
    customer_two.add_rental(Rental(Movie("The Matrix Reloaded", Movie.NEW_RELEASE), 3))

    # follow same steps as above
    ctx_obj_two = framework.create_customer_context(customer_two)
    dispatcher.notify(ctx_obj_two)



if __name__ == "__main__":
    main()