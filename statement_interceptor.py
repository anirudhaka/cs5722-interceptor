"""
A interceptor which intercepts and saves the statement() call
"""

from interceptor import Interceptor

class SaveStatementInterceptor(Interceptor):

    def update(self, context):
        print("******* Inside the statement_interceptor *******")
        customer_name = context.customer_object.get_name()
        time_now = str(context.get_creation_time())
        print("The customer name: ", context.customer_object.get_name())
        print("The rentals: ", context.customer_object.get_rentals())
        print(f"Saving the statement as {customer_name +'_'+ time_now} ")
        # add save code