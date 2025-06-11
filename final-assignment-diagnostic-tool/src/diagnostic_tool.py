def create_diagnostic_form(customer_name, item_name, priority_level, issue_description):
    form = f"Diagnostic Repair Form\n"
    form += f"Customer Name: {customer_name}\n"
    form += f"Item Name: {item_name}\n"
    form += f"Priority Level: {priority_level}\n"
    form += f"Issue Description: {issue_description}\n"
    form += "-----------------------------------\n"
    return form

def create_invoice_form(customer_name, item_name, priority_level, issue_description, cost):
    invoice = f"Invoice\n"
    invoice += f"Customer Name: {customer_name}\n"
    invoice += f"Item Name: {item_name}\n"
    invoice += f"Priority Level: {priority_level}\n"
    invoice += f"Issue Description: {issue_description}\n"
    invoice += f"Total Cost: ${cost:.2f}\n"
    invoice += "-----------------------------------\n"
    return invoice