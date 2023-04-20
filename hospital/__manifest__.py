{
    'name': "Hospital",
    'author': "iti",
    'depends': ['base', 'crm'],
    'data': ['views/patient_view.xml', 
             'views/department_view.xml',
               'views/doctor_view.xml',
                 'views/crm_customer_inherit.xml',
                   'security/security.xml',
                     'security/ir.model.access.csv',
                        'reports/report_form.xml',
                        'reports/report.xml']
}