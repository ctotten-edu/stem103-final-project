def validate_priority(priority):
    valid_priorities = ['low', 'medium', 'high']
    if priority.lower() in valid_priorities:
        return True
    else:
        return False

def format_report(customer_name, item_name, priority, issue_description):
    report = (
        f"Customer Name: {customer_name}\n"
        f"Item Name: {item_name}\n"
        f"Priority Level: {priority}\n"
        f"Issue Description: {issue_description}\n"
        "----------------------------------------\n"
    )
    return report