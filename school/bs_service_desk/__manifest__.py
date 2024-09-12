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
    'category': 'Services',
    'license': 'LGPL-3',
    'version': '16.0.1.0.0',

    'depends': [
        'base',
        'mail', 
        'portal',
        'utm',
        'product',
        'hr'
    ],

    'data': [
        'data/ir_sequence_data.xml',
        'views/service_desk_request_type_views.xml',
        'views/service_desk_stage_views.xml',
        'views/service_desk_request_priority_views.xml',
        'security/ir.model.access.csv',
        'views/service_desk_menu.xml',        
        'views/service_desk_request_views.xml'
    ],

    'demo': [
        'demo/stage_demo.xml',
    ],

    'images': [
        'static/description/icon.png'    
    ],
}
