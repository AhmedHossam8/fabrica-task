import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import getdate


class CustomerVisitRequest(Document):
	def validate(self):
		self.validate_single_active_visit()

	def on_update(self):
		if self.has_value_changed("workflow_state"):
			self.update_customer_last_visit_date()

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

	def update_customer_last_visit_date(self):
		"""Update customer's last visit date when request is completed."""
		if not (self.workflow_state == "Completed" and self.customer and self.visit_date):
			return

		current_last_visit = frappe.db.get_value(
			"Customer",
			self.customer,
			"custom_last_visit_date"
		)

		if not current_last_visit or getdate(self.visit_date) > getdate(current_last_visit):
			frappe.db.set_value(
				"Customer",
				self.customer,
				"custom_last_visit_date",
				self.visit_date
			)