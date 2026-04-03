import frappe


def cancel_visits_on_territory_change(doc, method=None):
	frappe.db.sql(
		"""
		UPDATE `tabCustomer Visit Request`
		SET workflow_state='Cancelled'
		WHERE customer=%s AND workflow_state IN ('Draft','Approved')
		""",
		(doc.name,),
	)
