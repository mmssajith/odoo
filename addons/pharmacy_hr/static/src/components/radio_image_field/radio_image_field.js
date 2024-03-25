/** @odoo-module */

import { registry } from "@web/core/registry";
import { RadioField, preloadRadio, radioField } from "@web/views/fields/radio/radio_field";

class RadioImageField extends RadioField {}
RadioImageField.template = "pharmacy_hr_homeworking.RadioImageField";

registry.category("fields").add("pharmacy_hr_homeworking_radio_image", {
    ...radioField,
    component: RadioImageField,
});

registry.category("preloadedData").add("pharmacy_hr_homeworking_radio_image", {
    loadOnTypes: ["many2one"],
    preload: preloadRadio,
});
