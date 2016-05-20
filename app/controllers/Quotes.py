"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
from flask import url_for

class Quotes(Controller):
    def __init__(self, action):
        super(Quotes, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """


        self.load_model('Quote')
        self.db = self._app.db

        """

        This is an example of a controller method that will load a view for the client

        """

    def index(self):
        """
        A loaded model is accessible through the models attribute
        self.models['WelcomeModel'].get_users()

        self.models['WelcomeModel'].add_message()
        # messages = self.models['WelcomeModel'].grab_messages()
        # user = self.models['WelcomeModel'].get_user()
        # to pass information on to a view it's the same as it was with Flask

        # return self.load_view('index.html', messages=messages, user=user)
        """
        quotes=self.models['Quote'].get_all_books()
        # reviews=self.models['Book'].get_most_recent_books()
        return self.load_view('quotes.html', quotes=quotes)

    def add(self):
        authors_all=self.models['Quote'].display_quoter()
        print "quoters_all returned: " + str(quoters_all)
        return self.load_view('add_quote.html', quoters=quoters_all)

    # def add_review(self, book_id):
    #
    #     print "we are in add_review", book_id
    #     #run a query to get 3 most recent reviews of that book
    #     three_reviews = self.models['Book'].get_book_reviews(book_id)
    #     title_author= self.models['Book'].get_book_title(book_id)
    #     return self.load_view('add_book_review.html', three_reviews=three_reviews, title_author=title_author[0])



    def create_quote(self):

        print "we are in create_quote"

        # quoter=request.form['quoter']
        # quoter_exists = True



        quote_info = {
             "quoter_name" : request.form['quoter_name'],
             "message":request.form['message'],
             "user_id":session['id'],
                }
        # print book_info['author']
        quote_id=self.models['Quote'].create_quote(quote_info)
        # print "this is book_id", book_id
        url = "/quotes/"+str(quote_id)
        return redirect(url)



    # def show_books(self, id):
    #     books=self.models['Book'].show_books(id)
    #     book_info=books[0]
    #     print book_info
    #     return self.load_view('user_reviews.html', book_info=book_info)
