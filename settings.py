DOMAIN = {
    'cat': {
        'resource_methods': ['GET', 'POST'],
        'schema': {
            'cat_name': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 10,
                'required': True,
            },
            'cat_description': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 5000,
                'default': 'No description for this cat :('
            },
            'cat_age': {
                'type': 'integer',
                'required': True,
            }
        }
    }
}
JSON = True
XML = False
# Config mongo
MONGO_HOST = "127.0.0.1"
MONGO_PORT = "27017"
MONGO_DBNAME = "cat_social_api"