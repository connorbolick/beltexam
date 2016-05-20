"""
    Routes Configuration File

    Put Routing rules here
"""
from system.core.router import routes

"""
    This is where you define routes

    Start by defining the default controller
    Pylot will look for the index method in the default controller to handle the base route

    Pylot will also automatically generate routes that resemble: '/controller/method/parameters'
    For example if you had a products controller with an add method that took one parameter
    named id the automatically generated url would be '/products/add/<id>'
    The automatically generated routes respond to all of the http verbs (GET, POST, PUT, PATCH, DELETE)
"""
routes['default_controller'] = 'Users'
routes['POST']['/create']='Users#create'
routes['POST']['/login']='Users#login'
# routes['GET']['/quotes']='Quotes#index'
# routes['GET']['/quotes/add']='Quotes#add'
# routes['POST']['/add_book_review']='Books#create_book'
# routes['POST']['/add_review']='Books#create_new_review'
# routes['GET']['/books/<book_id>']='Books#add_review'
# routes['GET']['/users/<id>']='Users#user_show'
# routes['GET']['/logout']='Users#log_out'
# routes['GET']['/users/<id>']='Books#show_books'
