/** @odoo-module */

import { registry } from "@web/core/registry";
import { standardWidgetProps } from "@web/views/widgets/standard_widget_props";

import { useOpenChat } from "@mail/core/web/open_chat_hook";
import { Component } from "@odoo/owl";

export class pharmacy_hrEmployeeChat extends Component {
    setup() {
        super.setup();
        this.openChat = useOpenChat(this.props.record.resModel);
    }
}
pharmacy_hrEmployeeChat.props = {
    ...standardWidgetProps,
};
pharmacy_hrEmployeeChat.template = "pharmacy_hr.OpenChat";

export const pharmacy_hrEmployeeChat = {
    component: pharmacy_hrEmployeeChat,
};
registry.category("view_widgets").add("pharmacy_hr_employee_chat", pharmacy_hrEmployeeChat);
