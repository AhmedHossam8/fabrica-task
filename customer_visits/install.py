import frappe


def ensure_workflow_actions():
	"""Workflow transitions use these actions; create if missing (idempotent)."""
	for title in ("Complete", "Cancel"):
		if not frappe.db.exists("Workflow Action Master", title):
			frappe.get_doc(
				{"doctype": "Workflow Action Master", "workflow_action_name": title}
			).insert(ignore_permissions=True)
