from AptUrl.Helpers import _

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class EmployeeLevel(models.Model):

    _name = 'employee.level'
    _rec_name = 'level'

    level = fields.Char(string='Level')
    salary = fields.Float(string='Salary')

class EmployeeRelatedLevel(models.Model):

    _inherit = 'hr.employee'
    def default_level(self):
        search = self.env['employee.level'].search([],order='level desc')
        value = list(search)
        # print(max(value))
        vals = max(value)
        return vals

    employee_level_id = fields.Many2one('employee.level',string='Employee Level',default=default_level)
    salary = fields.Char(string='Salary')

    def promote_level(self):
        print('gh')

        search = self.env['employee.level'].search([], order='level desc')
        value=list(search)
        print(max(value))

        for i in value:
            if i:
                value.remove(max(value))
                print(value,'llllllllll')
                print(max(value),'farrrrrrrrr')
                self.employee_level_id = max(value)
                self.salary = self.employee_level_id.salary

    @api.onchange('employee_level_id')
    def onchange_employee_level_id(self):
        self.salary = self.employee_level_id.salary

