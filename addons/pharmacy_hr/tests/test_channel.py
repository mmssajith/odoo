# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.addons.pharmacy_hr.tests.common import Testpharmacy_hrCommon
from odoo.tests.common import tagged


@tagged("post_install", "-at_install")
class TestChannel(Testpharmacy_hrCommon):

    @classmethod
    def setUpClass(cls):
        super(TestChannel, cls).setUpClass()

        cls.channel = cls.env['discuss.channel'].create({'name': 'Test'})

        emp0 = cls.env['pharmacy_hr.employee'].create({
            'user_id': cls.res_users_pharmacy_hr_officer.id,
        })
        cls.department = cls.env['pharmacy_hr.department'].create({
            'name': 'Test Department',
            'member_ids': [(4, emp0.id)],
        })

    def test_auto_subscribe_department(self):
        self.assertEqual(self.channel.channel_partner_ids, self.env['res.partner'])

        self.channel.write({
            'subscription_department_ids': [(4, self.department.id)]
        })

        self.assertEqual(self.channel.channel_partner_ids, self.department.mapped('member_ids.user_id.partner_id'))
