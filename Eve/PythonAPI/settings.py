MONGO_HOST = 'localhost'
MONGO_PORT = 27017

MONGO_DBNAME = 'eve'


RESOURCE_METHODS = ['GET', 'POST']

DOMAIN = {
	'user': {
		'additional_lookup': {
            'url': 'regex("[\w]+")',
            'field': 'username',
        },
    	'schema': {
            'firstname': {
    		      'type': 'string'
           	},
            'lastname': {
               	'type': 'string'
            },
            'username': {
               	'type': 'string',
               	'unique': True
            },
            'password': {
               	'type': 'string'
            },
            'phone': {
               	'type': 'string'
            }
        }
    },
	
    'item': {
        'schema': {
            'name':{
                'type': 'string'
            },
           	'username': {
               	'type': 'string'
            }
        }
    }
}
