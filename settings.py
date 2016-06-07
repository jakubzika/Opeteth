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
            'id':1,
            'api':['getNotes'],
            'call':pageProcess.notes,
        },
        {
            'uri':'text',
            'path':'text',
            'id':2,
            'api':[],
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
            'name':'Preview',
            'link-to':0,
        },
        {
            'name':'Notes',
            'link-to':1,
        },
        {
            'name':'Text',
            'link-to':2,
        }
    ]
}
