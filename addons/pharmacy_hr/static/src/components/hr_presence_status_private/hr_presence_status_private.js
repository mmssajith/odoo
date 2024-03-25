/** @odoo-module */

import { registry } from "@web/core/registry";
import { pharmacy_hrPresenceStatus, pharmacy_hrPresenceStatus } from "../pharmacy_hr_presence_status/pharmacy_hr_presence_status";

export class pharmacy_hrPresenceStatusPrivate extends pharmacy_hrPresenceStatus { }

export const pharmacy_hrPresenceStatusPrivate = {
    ...pharmacy_hrPresenceStatus,
    component: pharmacy_hrPresenceStatusPrivate,
};

registry.category("fields").add("pharmacy_hr_presence_status_private", pharmacy_hrPresenceStatusPrivate);
