frappe.ui.form.on('Customer', {
    refresh: function(frm) {
        if (frm.is_new()) return;

        frappe.call({
            method: 'frappe.client.get_list',
            args: {
                doctype: 'Customer Visit Request',
                filters: [
                    ['customer', '=', frm.doc.name],
                    ['workflow_state', 'in', ['Draft', 'Approved']]
                ],
                fields: ['name'],
                limit: 1
            },
            callback: function(r) {
                if (r.message && r.message.length > 0) {
                    var visit_name = r.message[0].name;
                    frm.add_custom_button('View Scheduled Visit Request', function() {
                        frappe.set_route('Form', 'Customer Visit Request', visit_name);
                    });
                } else {
                    frm.add_custom_button('Create Visit Request', function() {
                        frappe.new_doc('Customer Visit Request', {
                            customer: frm.doc.name
                        });
                    });
                }
            }
        });
    }
});
