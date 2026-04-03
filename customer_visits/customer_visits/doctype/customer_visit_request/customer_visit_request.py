import frappe
from frappe import _
from frappe.model.document import Document


class CustomerVisitRequest(Document):
	def validate(self):
		self.validate_single_active_visit()

	def validate_single_active_visit(self):
		"""Only one visit request per customer may be in Draft or Approved at a time."""
		if not self.customer:
			return

		state = self.workflow_state or "Draft"
		if state not in ("Draft", "Approved"):
			return

		filters = {
			"customer": self.customer,
			"workflow_state": ["in", ["Draft", "Approved"]],
		}
		if self.name:
			filters["name"] = ["!=", self.name]

		if frappe.db.exists("Customer Visit Request", filters):
			frappe.throw(
				_("Customer {0} already has a scheduled visit request in Draft or Approved state.").format(
					self.customer
				)
			)

	def on_update_after_submit(self):
		if self.workflow_state == "Completed":
			frappe.db.set_value("Customer", self.customer, "custom_last_visit_date", self.visit_date)
