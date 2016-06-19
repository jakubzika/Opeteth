import pageProcess

settings = {
    'pages': [

        {
            'uri': 'index',
            'path': 'index',
            'id': 0,
            'api': [],
            'call': pageProcess.index,
            'permission': 20,
        },
        {
            'uri': 'notes',
            'path': 'notes',
            'id': 1,
            'api': ['getNotes'],
            'call': pageProcess.notes,
            'permission': 10,
        },
        {
            'uri': 'text',
            'path': 'text',
            'id': 2,
            'api': [],
            'call': pageProcess.notes,
            'permission': 20,
        },
        {
            'uri': 'admin',
            'path': 'admin',
            'id': 3,
            'api': [],
            'call': pageProcess.admin(),
            'permission':1,
        }

    ],
    'paths': {
        'templates': 'templates/',
        'pages': 'pages/',
        'static': 'static/',
    },
    'menu': [
        {
            'name': 'Preview',
            'link-to': 0,
            'permission': 20,

        },
        {
            'name': 'Notes',
            'link-to': 1,
            'permission': 10,
        },
        {
            'name': 'Text',
            'link-to': 2,
            'permission': 20,
        },
        {
            'name': 'Admin tools',
            'link-to': 3,
            'permission': 1
        }
    ]
}
