import modules

userState = 0

settings = {
    'dependencies': {
        'head': ['css/main.css', ],
        'body': ['js/main.js', ],
    },
    'menu': [
        {
            'name': 'Lorem ipsum',
            'visibility': 1,
            'index': 0,

        },
        {
            'name': 'Management',
            'visibility': 1,
            'index': 2,
        },
        {
            'name': 'Notes',
            'visibility': 6,
            'index': 3,
        }
    ],
    'modules': [
        {
            'name': 'user info',
            'path': '',
            #'callable': modules.user_info()
        },
        {
            'name': 'notifications',
            'path':'',
            #'callable': modules.notifications()
        },

    ]

}
