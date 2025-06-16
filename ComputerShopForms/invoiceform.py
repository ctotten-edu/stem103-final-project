# Collecting invoice information for invoice form

def collect_invoice_info(issue_type, description):
    print("\n--- Invoice Form ---")
    
    invoice = {}
    if issue_type in ['diagnostic', 'repair', 'maintenance']:
        urgency = input("Urgency Level (standard, priority, rush): ").strip().lower() # Have the user specify urgency level
        processing_costs = {
            'standard': (89.00, "5-6 business days"),
            'priority': (150.00, "1-2 business days"),
            'rush': (500.00, "within 24 hours")
        }

        base_cost, eta = processing_costs.get(urgency, (0, "unknown"))
        labor_cost = 0

        if "fix" in description.lower():
            labor_cost += 130  # 1 hour labor
        if "repair" in description.lower():
            labor_cost += 130 
        if "replace" in description.lower():
            labor_cost += 130
        total = base_cost + labor_cost

        invoice = {
            "Urgency": urgency,
            "Base Cost": f"${base_cost:.2f}",
            "Labor Cost": f"${labor_cost:.2f}",
            "Total Cost": f"${total:.2f}",
            "Turnaround Time": eta
        }

    else:
        detail = input("Enter one-line detail for invoice: ")
        invoice = {
            "Invoice Detail": detail
        }

    return invoice
