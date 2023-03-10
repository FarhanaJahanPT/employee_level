{
    'name': 'Employee Level',
    'sequence': 1,
    'version': '16.0.1.0.0',
    'depends': ['base', 'hr'],

    'data':  [
              'security/ir.model.access.csv',
              'views/employee_level.xml',
              'views/employee_level_menu.xml',
              ],

    'installable': True,
    'application': True,
    'auto_install': False,

}
