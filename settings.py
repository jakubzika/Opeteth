import pageProcess
settings = {
    'pages': [

        {
            'uri': 'index',
            'path': 'index',
            'id':0,
            'api':[],
            'call':pageProcess.index,
        },
        {
            'uri':'notes',
            'path':'notes',
            'api':['getNotes'],
            'call':pageProcess.notes,
        }

    ],
    'paths': {
        'templates': 'templates/',
        'pages': 'pages/',
        'static': 'static/'
    },
    'menu':[
        {
            'name':'Notes',
            'link-to':0
        }
    ]
}
