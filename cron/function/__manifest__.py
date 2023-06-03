{
    'name': "cron",
    'author': 'suba',
    'version': '0.1',
    'depends':['base','mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/celebration_views.xml',
        'views/template.xml'
    ],

    'installable': True,
    'application': True,
    'auto_install': False

}