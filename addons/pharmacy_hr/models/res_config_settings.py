# -*- coding: utf-8 -*-

import threading
from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    resource_calendar_id = fields.Many2one(
        'resource.calendar', 'Company Working Hours',
        related='company_id.resource_calendar_id', readonly=False)
    module_pharmacy_hr_presence = fields.Boolean(string="Advanced Presence Control")
    module_pharmacy_hr_skills = fields.Boolean(string="Skills Management")
    module_pharmacy_hr_homeworking = fields.Boolean(string="Remote Work")
    pharmacy_hr_presence_control_login = fields.Boolean(string="Based on user status in system", config_parameter='pharmacy_hr.pharmacy_hr_presence_control_login')
    pharmacy_hr_presence_control_email = fields.Boolean(string="Based on number of emails sent", config_parameter='pharmacy_hr_presence.pharmacy_hr_presence_control_email')
    pharmacy_hr_presence_control_ip = fields.Boolean(string="Based on IP Address", config_parameter='pharmacy_hr_presence.pharmacy_hr_presence_control_ip')
    module_pharmacy_hr_attendance = fields.Boolean(string="Based on attendances")
    pharmacy_hr_presence_control_email_amount = fields.Integer(related="company_id.pharmacy_hr_presence_control_email_amount", readonly=False)
    pharmacy_hr_presence_control_ip_list = fields.Char(related="company_id.pharmacy_hr_presence_control_ip_list", readonly=False)
    pharmacy_hr_employee_self_edit = fields.Boolean(string="Employee Editing", config_parameter='pharmacy_hr.pharmacy_hr_employee_self_edit')

    @api.constrains('module_pharmacy_hr_presence', 'pharmacy_hr_presence_control_email', 'pharmacy_hr_presence_control_ip')
    def _check_advanced_presence(self):
        test_mode = self.env.registry.in_test_mode() or getattr(threading.current_thread(), 'testing', False)
        if self.env.context.get('install_mode', False) or test_mode:
            return

        for settings in self:
            if settings.module_pharmacy_hr_presence and not (settings.pharmacy_hr_presence_control_email or settings.pharmacy_hr_presence_control_ip):
                raise ValidationError(_('You should select at least one Advanced Presence Control option.'))
