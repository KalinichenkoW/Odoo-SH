{
    'name': "BS Service Desk",

    'summary': """
        Modules lists 
        Service Desk""",

    'description': """
        Module Service Desk
    """,

    'author': "Volodymyr Kalinichenko",
    'website': "https://www.bettaservice.com.ua",
    'category': 'Uncategorized',
    'license': 'LGPL-3',
    'version': '16.0.1.0.0',

    'depends': ['base'],

    'data': [
        'data/ir_sequence_data.xml',
        'security/ir.model.access.csv',
        'views/service_desk_menu.xml',
        'views/service_desk_request_views.xml',
        'views/service_desk_stage_views.xml',                
        # 'views/.xml',
    ],

    'demo': [
        'demo/stage_demo.xml',
        #'demo/request_demo.xml',
    ],

    'installable': True,
    'auto_install': False,

    'images': [
        'static/description/icon.png',
        
        
    ],
}
