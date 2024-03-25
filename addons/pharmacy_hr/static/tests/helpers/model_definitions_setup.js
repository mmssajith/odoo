/** @odoo-module **/

import { addFakeModel, addModelNamesToFetch } from '@bus/../tests/helpers/model_definitions_helpers';

addModelNamesToFetch(['pharmacy_hr.employee', 'pharmacy_hr.employee.public', 'pharmacy_hr.department']);

addFakeModel('m2x.avatar.employee', {
    employee_id: { string: "Employee", type: 'many2one', relation: 'pharmacy_hr.employee.public' },
    employee_ids: { string: "Employees", type: "many2many", relation: 'pharmacy_hr.employee.public' },
});
