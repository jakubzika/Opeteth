import pageProcess

settings = {
    'pages': [

        {
            'name': 'index',
            'uri': 'index',
            'path': 'index',
            'id': 0,
            'permission': 20,
            'scope':['super-admin','admin','user','guest'],
        },
        {
            'name': 'preview',
            'uri': 'preview',
            'path': 'preview',
            'id': 4,
            'permission': 20,
            'scope':['super-admin','admin','user','guest'],

        },
        {
            'name': 'notes',
            'uri': 'notes',
            'path': 'notes',
            'id': 1,
            'permission': 10,
            'module': True,
            'module-name': 'notes',
            'scope':['super-admin','admin','user','guest'],
        },
        {
            'name': 'text',
            'uri': 'text',
            'path': 'text',
            'id': 2,
            'permission': 20,
            'scope':['super-admin','admin','user','guest'],

        },
        {
            'name': 'admin',
            'uri': 'admin',
            'path': 'admin',
            'id': 3,
            'permission': 1,
            'scope':['super-admin','admin'],

        },
        {
            'name': 'register',
            'uri': 'register',
            'path': 'register',
            'id': 5,
            'permission': 20,
            'scope':['super-admin','admin','guest'],

        },
        {
            'name':'management',
            'uri':'management',
            'path':'management',
            'permission':1,
            'scope':['super-admin','admin'],

        }

    ],
    'paths': {
        'templates': 'templates',
        'pages': 'pages/',
        'static': 'static/',
        'modules': 'modules',
        'blueprint-name': 'module'
    },
    'menu': [
        {
            'name': 'Home',
            'link-to': 'index',
            'permission': 20,
            'scope': ['super-admin', 'admin', 'user', 'guest'],

        },
        {
            'name': 'Notes',
            'link-to': 'notes',
            'permission': 10,
            'scope':['super-admin','admin','user','guest'],

        },
        {
            'name': 'Text',
            'link-to': 'text',
            'permission': 20,
            'scope':['super-admin','admin','user','guest'],

        },
        {
            'name': 'Admin tools',
            'link-to': 'admin',
            'permission': 1,
            'scope':['super-admin','admin','user','guest'],

        },
        {
            'name': 'Preview',
            'link-to': 'preview',
            'permission': 20,
            'scope':['super-admin','admin','user','guest'],

        },
        {
            'name':'Management',
            'link-to':'management',
            'permission':1,
            'scope':['super-admin','admin','user','guest'],

        }

    ],
    'modules': [
        {
            'name': 'notes',
            'api-path': 'note',
            'url-path': 'note',
            'package-path': 'Notes',
            'permission': 10,
            'templates-path': 'templates',
        },
        {
            'name': 'admin-tools',
            'api-path': 'admin',
            'url-path': 'admin',
            'package-path': 'AdminTools',
            'permission': 1,
            'templates-path': 'templates',
        },
        {
            'name': 'user-tools',
            'api-path': 'user',
            'url-path':'user',
            'package-path': 'User',
            'permission': 20,
            'templates-path': 'templates',
        },
        {
            'name':'management',
            'api-path':'manage',
            'url-path':'manage',
            'package-path':'Management',
            'permission':1,
            'template-path':'templates'
        }

    ],
    'scopes':[
        {
            'name':'super-admin'
        },
        {
            'name':'admin'
        },
        {
            'name':'user'
        },
        {
            'name':'guest'
        }
    ]
}
