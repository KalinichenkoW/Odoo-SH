{
    'name': "hr_hospital",
    'summary': "Hospital automation",
    'author': "Volodymyr Kalinichenko",
    'website': "http://ukr.net",
    'category': 'Uncategorized',
    'license': 'LGPL-3',
    'version': '15.0.1.0.0',

    'depends': [
        'base',
    ],

    'external_dependencies': {'python': [], },

    'data': [
        'security/ir.model.access.csv',
        'data/disease_data.xml',
        'views/hospital_menu.xml',
        'views/hospital_doctor_views.xml',
        'views/hospital_disease_views.xml',
        'views/hospital_patient_views.xml',
        'views/hospital_patient_visit_views.xml',
    ],

    'demo': [
        'demo/doctor_demo.xml',
        'demo/patient_demo.xml',
    ],

    'installable': True,
    'auto_install': False,

    'images': [
        'static/description/icon.png',
    ],

}
