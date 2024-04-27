import frappe


def update_invoice(doc, method=None):
	frappe.db.set_value("Sales Invoice", doc.sales_invoice, "custom_ack_no", doc.acknowledgement_number)
	frappe.db.set_value("Sales Invoice", doc.sales_invoice, "custom_ack_date", doc.acknowledged_on)
