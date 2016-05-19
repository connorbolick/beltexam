"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
from flask import url_for 

class Books(Controller):
    def __init__(self, action):
        super(Books, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """

           
        self.load_model('Book')
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
        books=self.models['Book'].get_all_books()
        reviews=self.models['Book'].get_most_recent_books()
        return self.load_view('books.html', books=books, reviews=reviews)
        
    def add(self):
        authors_all=self.models['Book'].display_authors()
        print "authors_all returned: " + str(authors_all)
        return self.load_view('add_book.html', authors=authors_all)

    def add_review(self, book_id):

        print "we are in add_review", book_id
        #run a query to get 3 most recent reviews of that book
        three_reviews = self.models['Book'].get_book_reviews(book_id)
        title_author= self.models['Book'].get_book_title(book_id)
        return self.load_view('add_book_review.html', three_reviews=three_reviews, title_author=title_author[0])

    

    def create_book(self):
        # print "Connor said this is"+ request.form['author_alt']
        print "we are in create_book"
        if request.form['author_alt']:
            author=request.form['author_alt']
            author_exists=False 
        else:
            author=request.form['author']
            author_exists = True
       
 

        book_info = {
             "title" : request.form['title'],
             "author":author,
             "review":request.form['review'],
             "ratings":request.form['ratings'],
             "user_id":session['id'],
             "author_exists": author_exists
                }
        # print book_info['author']
        book_id=self.models['Book'].create_book(book_info)
        # print "this is book_id", book_id
        url = "/books/"+str(book_id)
        return redirect(url)
        # return redirect("/books/", book_id)
        # return redirect(url_for('/books', book_id=book_id))
    def create_new_review(self):

        print "we are create_new_review"
        data={
            'review':request.form['review'],
            'ratings':request.form['ratings'],
            'book_id':request.form['book_id'],
            'user_id':session['id']
        }
        self.models['Book'].insert_new_review(data)
        url = "/books/"+str(data['book_id'])
        return redirect(url)
    
    def show_books(self, id):
        books=self.models['Book'].show_books(id)
        book_info=books[0]
        print book_info
        return self.load_view('user_reviews.html', book_info=book_info)
    