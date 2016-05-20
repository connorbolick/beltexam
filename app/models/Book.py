""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model
import re

class Book(Model):
    def __init__(self):
        super(Book, self).__init__()
    
    def display_authors(self):
        query_all_authors="SELECT * FROM authors"
       
        authors_all=self.db.query_db(query_all_authors)
        print authors_all
        return authors_all

    def create_book(self, book_info):
        if not book_info['author_exists']:
            query_insert="INSERT INTO authors (author_name) VALUES (:author)"
            data={'author':book_info['author']}
            author_id = self.db.query_db(query_insert, data)
        else:
            get_author_query = "SELECT * FROM authors WHERE author_name=:author"
            data={'author':book_info['author']}
            print data
            author= self.db.query_db(get_author_query, data)
            author_id=author[0]['id']

        query_insert_book="INSERT INTO books (author_id, title, user_id)  VALUES (:author_id, :title, :user_id)"
        data2={
                'author_id':author_id,
                'title':book_info['title'],
                'user_id':book_info['user_id']
           
              
        }
        book_id=self.db.query_db(query_insert_book, data2)
        print "this is book_id", book_id
        
        query_insert_review="INSERT INTO reviews(ratings, review, created_at, updated_at, book_id, user_id) VALUES(:ratings, :review, NOW(), NOW(), :book_id, :user_id)"
        data4={
                'ratings':book_info['ratings'],
                'review':book_info['review'],
                'book_id':book_id,
                'user_id':book_info['user_id']
         
        }
        record = self.db.query_db(query_insert_review,data4)
        print "This is after inserting review: ", record
        return book_id

    def get_book_title(self, book_id):
        query="SELECT books.title, authors.author_name FROM books JOIN authors ON books.author_id=authors.id WHERE books.id=:book_id"
        data={'book_id': book_id}
        return self.db.query_db(query, data)

    def get_book_reviews(self, book_id):

        query= "SELECT * FROM reviews WHERE book_id=:book_id ORDER BY created_at Desc"
        data= {'book_id': book_id}
        three_reviews = self.db.query_db(query, data)
        return three_reviews

    def get_all_books(self):
        query="SELECT * FROM books"
        return self.db.query_db(query)

    def get_most_recent_books(self):
        query="select books.title, reviews.ratings, reviews.review, users.name, books.id, reviews.created_at FROM reviews JOIN books ON books.id=reviews.book_id JOIN users ON users.id=reviews.user_id ORDER BY created_at DESC LIMIT 3"
        return self.db.query_db(query)

    def insert_new_review(self, data):
        query = "INSERT INTO reviews (user_id, review, book_id, ratings, created_at) VALUES (:user_id, :review, :book_id, :ratings, NOW())"
        

        data = {
                'user_id': data['user_id'],
                'review' : data['review'],
                'book_id': data['book_id'],
                'ratings': data['ratings']
        }
        return self.db.query_db(query, data)
        
    # def show_books(self, id):
    #     query="select books.title from books JOIN users ON books.user_id=users.id"
    #     data = {'id':id}
    #     return self.db.query_db(query, data)


    """
    Below is an example of a model method that queries the database for all users in a fictitious application
    
    Every model has access to the "self.db.query_db" method which allows you to interact with the database

    def get_users(self):
        query = "SELECT * from users"
        return self.db.query_db(query)

    def get_user(self):
        query = "SELECT * from users where id = :id"
        data = {'id': 1}
        return self.db.get_one(query, data)

    def add_message(self):
        sql = "INSERT into messages (message, created_at, users_id) values(:message, NOW(), :users_id)"
        data = {'message': 'awesome bro', 'users_id': 1}
        self.db.query_db(sql, data)
        return True
    
    def grab_messages(self):
        query = "SELECT * from messages where users_id = :user_id"
        data = {'user_id':1}
        return self.db.query_db(query, data)

    """