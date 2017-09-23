# Let's just use the local mongod instance. Edit as needed.

# Please note that MONGO_HOST and MONGO_PORT could very well be left
# out as they already default to a bare bones local 'mongod' instance.
MONGO_HOST = 'localhost'
MONGO_PORT = 27017

# Skip these if your db has no auth. But it really should.
#MONGO_USERNAME = '<your username>'
#MONGO_PASSWORD = '<your password>'

MONGO_DBNAME = 'apitest'


# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']


# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']


schema = {
	# Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/nicolaiarocci/cerberus) for details.
    'firstname': {
    	'type': 'string',
    	'minlength': 1,
    	'maxlength': 10,
    	'required': True,
    },
    'lastname': {
    	'type': 'string',
    	'minlength': 1,
    	'maxlength': 15,
    	'required': True,
    },
    'username': {
       	'type': 'string',
       	'required': True,
       	# talk about hard constraints! For the purpose of the demo
       	# 'lastname' is an API entry-point, so we need it to be unique.
       	'unique': True,
    },
    #'password': {
    #	'type': 'string',
    #	'required': True,
    #},
    'start_date': {
       	'type': 'datetime'
    },
}

user = {
	# 'title' tag used in item links.
	'item_title': 'user_data',
	# by default the standard item entry point is defined as
    # '/user/<ObjectId>'. We leave it untouched, and we also enable an
    # additional read-only entry point. This way consumers can also perform
    # GET requests at '/user/<username>'.
    'additional_lookup': {        
       	'url': 'regex("[\w]+")',
       	'field': 'username',
	},
	# most global settings can be overridden at resource level
    'resource_methods': ['GET', 'POST'],

	'schema': schema
}


DOMAIN = { 
	'user': user,
}
