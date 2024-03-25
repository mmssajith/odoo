# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.addons.mail.tests.common import mail_new_test_user
from odoo.tests import common


class Testpharmacy_hrCommon(common.TransactionCase):

    @classmethod
    def setUpClass(cls):
        super(Testpharmacy_hrCommon, cls).setUpClass()

        cls.res_users_pharmacy_hr_officer = mail_new_test_user(cls.env, login='pharmacy_hro', groups='base.group_user,pharmacy_hr.group_pharmacy_hr_user', name='pharmacy_hr Officer', email='pharmacy_hro@example.com')
