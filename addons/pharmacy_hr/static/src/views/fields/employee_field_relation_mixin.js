/** @odoo-module **/

import { onWillStart } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

/**
 * Mixin that handles public/private access of employee records in many2X fields
 * @param { Class } fieldClass
 * @returns Class
 */
export function EmployeeFieldRelationMixin(fieldClass) {
    return class extends fieldClass {
        static props = {
            ...fieldClass.props,
            relation: { type: String, optional: true },
        };

        setup() {
            super.setup();
            this.user = useService("user");
            onWillStart(async () => {
                this.ispharmacy_hrUser = await this.user.hasGroup("pharmacy_hr.group_pharmacy_hr_user");
            });
        }

        get relation() {
            if (this.props.relation) {
                return this.props.relation;
            }
            return this.ispharmacy_hrUser ? "pharmacy_hr.employee" : "pharmacy_hr.employee.public";
        }
    };
}
