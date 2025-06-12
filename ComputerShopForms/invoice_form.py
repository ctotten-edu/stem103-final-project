def generate_invoice(info):
    print("--- Invoice Form ---")
    issue_type = info['issue_description']
    cost = 0
    turnaround_time = ""
    
    if issue_type in ['diagnostic', 'repair', 'maintenance']:
        urgency = ""
        while urgency.lower() not in ['standard', 'priority', 'rush']:
            urgency = input("Enter urgency level (Standard, Priority, Rush): ")
        urgency = urgency.lower()

        if urgency == 'standard':
            cost = 89
            turnaround_time = "5-6 business days"
        elif urgency == 'priority':
            cost = 150
            turnaround_time = "1-2 business days"
        elif urgency == 'rush':
            cost = 500
            turnaround_time = "within 24 hours"
        
        labor_hours = 1  # default most common
        labor_cost = 130 * labor_hours
        cost += labor_cost

    else:
        # Sales or Other
        urgency = input("Enter one-line detail for invoice: ")
        turnaround_time = "N/A"

    return {
        'urgency': urgency,
        'labor_cost': 130,
        'diagnostic_cost': cost,
        'turnaround_time': turnaround_time
    }
