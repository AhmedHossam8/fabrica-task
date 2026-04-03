import frappe
from erpnext.selling.doctype.customer.customer import Customer


class CustomCustomer(Customer):
    def on_update(self):
        super().on_update()
        self.cancel_visits_on_territory_change()

    def cancel_visits_on_territory_change(self):
        # Check if territory actually changed
        before = self.get_doc_before_save()
        if not before:
            return
        if before.get("territory") == self.territory:
            return

        # Find all Draft or Approved visit requests for this customer
        visits = frappe.get_all(
            "Customer Visit Request",
            filters={
                "customer": self.name,
                "workflow_state": ["in", ["Draft", "Approved"]],
                "docstatus": ["!=", 2],
            },
            fields=["name", "docstatus"],
        )

        for visit in visits:
            doc = frappe.get_doc("Customer Visit Request", visit.name)
            if doc.docstatus == 1:
                # Already submitted — cancel it
                doc.cancel()
            else:
                # Still draft (docstatus 0) — delete or mark cancelled via workflow
                frappe.db.set_value(
                    "Customer Visit Request",
                    doc.name,
                    "workflow_state",
                    "Cancelled"
                )

        if visits:
            frappe.db.commit()
            frappe.msgprint(
                frappe._("{0} visit request(s) cancelled due to territory change.").format(len(visits)),
                alert=True
            )
