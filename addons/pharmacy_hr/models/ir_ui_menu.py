# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, api, tools


class IrUiMenu(models.Model):
    _inherit = 'ir.ui.menu'

    def _load_menus_blacklist(self):
        res = super()._load_menus_blacklist()
        if self.env.user.has_group('pharmacy_hr.group_pharmacy_hr_user'):
            res.append(self.env.ref('pharmacy_hr.menu_pharmacy_hr_employee').id)
        return res
