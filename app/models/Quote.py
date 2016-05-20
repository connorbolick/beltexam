"""
    Sample Model File

    A Model should be in charge of communicating with the Database.
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model
import re

class Quote(Model):
    def __init__(self):
        super(Quote, self).__init__()

    def display_quotes(self):
        query_all_quotes="SELECT * FROM quotes"

        authors_all=self.db.query_db(query_all_quotes)
        print quotes_all
        return quotes_all

    # def create_quote(self, quote_info):
    #     if not book_info['quoter_exists']:
    #         query_insert="INSERT INTO quoter (quoter_name) VALUES (:quoter)"
    #         data={'quoter':quote_info['quoter']}
    #         quoter_id = self.db.query_db(query_insert, data)
    #     else:
    #         get_quoter_query = "SELECT * FROM quoters WHERE quoter_name=:quoter"
    #         data={'quoter':quote_info['quoter']}
    #         print data
    #         quoter = self.db.query_db(get_quoter_query, data)
    #         quoter_id=quoter[0]['id']
    #
    #     query_insert_quote="INSERT INTO quotes (quoter_id, user_id)  VALUES (:author_id, :user_id)"
    #     data2={
    #             'quoter_id':quoter_id,
    #             'user_id':quote_info['user_id']
    #
    #
    #     }
    #     quote_id=self.db.query_db(query_insert_quote, data2)
    #     print "this is quote_id", book_id
    #     return book_id

    # def get_book_title(self, book_id):
    #     query="SELECT books.title, authors.author_name FROM books JOIN authors ON books.author_id=authors.id WHERE books.id=:book_id"
    #     data={'book_id': book_id}
    #     return self.db.query_db(query, data)

    # def get_book_reviews(self, book_id):
    #
    #     query= "SELECT * FROM reviews WHERE book_id=:book_id ORDER BY created_at Desc"
    #     data= {'book_id': book_id}
    #     three_reviews = self.db.query_db(query, data)
    #     return three_reviews

    # def get_all_books(self):
    #     query="SELECT * FROM books"
    #     return self.db.query_db(query)

    # def get_most_recent_quotes(self):
    #     query="select quotes.quoter_name, users.quote_poster, quotes.id FROM reviews JOIN quotes ON quotes.id=quoters.quote_id JOIN users ON users.id=quotes.user_id ORDER BY created_at DESC LIMIT 4"
    #     return self.db.query_db(query)

    # def insert_new_review(self, data):
    #     query = "INSERT INTO reviews (user_id, review, book_id, ratings, created_at) VALUES (:user_id, :review, :book_id, :ratings, NOW())"
    #
    #
    #     data = {
    #             'user_id': data['user_id'],
    #             'review' : data['review'],
    #             'book_id': data['book_id'],
    #             'ratings': data['ratings']
    #     }
    #     return self.db.query_db(query, data)

    # def show_books(self, id):
    #     query="select books.title from books JOIN users ON books.user_id=users.id"
    #     data = {'id':id}
    #     return self.db.query_db(query, data)
