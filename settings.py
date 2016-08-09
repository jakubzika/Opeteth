import pageProcess

settings = {
    'pages': [

        {
            'name': 'index',
            'uri': 'index',
            'path': 'index',
            'id': 0,
            'permission': 20,
        },
        {
            'name': 'preview',
            'uri': 'preview',
            'path': 'preview',
            'id': 4,
            'permission': 20,
        },
        {
            'name': 'notes',
            'uri': 'notes',
            'path': 'notes',
            'id': 1,
            'permission': 10,
            'module': True,
            'module-name': 'notes',
        },
        {
            'name': 'text',
            'uri': 'text',
            'path': 'text',
            'id': 2,
            'permission': 20,
        },
        {
            'name': 'admin',
            'uri': 'admin',
            'path': 'admin',
            'id': 3,
            'permission': 1,
        },
        {
            'name': 'register',
            'uri': 'register',
            'path': 'register',
            'id': 5,
            'permission': 20,
        },

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

        },
        {
            'name': 'Notes',
            'link-to': 'notes',
            'permission': 10,
        },
        {
            'name': 'Text',
            'link-to': 'text',
            'permission': 20,
        },
        {
            'name': 'Admin tools',
            'link-to': 'admin',
            'permission': 1
        },
        {
            'name': 'Preview',
            'link-to': 'preview',
            'permission': 20
        },

    ],
    'modules': [
        {
            'name': 'notes',
            'api-path': 'note',
            'package-path': 'Notes',
            'permission': 10,
            'templates-path': 'templates',
        },
        {
            'name': 'admin-tools',
            'api-path': 'admin',
            'package-path': 'AdminTools',
            'permission': 1,
            'templates-path': 'templates',
        },
        {
            'name': 'user-tools',
            'api-path': 'user',
            'package-path': 'User',
            'permission': 20,
            'templates-path': 'templates',
        },

    ]
}
