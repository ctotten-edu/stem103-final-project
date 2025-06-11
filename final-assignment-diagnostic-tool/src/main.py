# filepath: /final-assignment-diagnostic-tool/final-assignment-diagnostic-tool/src/main.py

def greet_user():
    print("Welcome to the Diagnostic Reporting Tool!")
    print("Please provide the following information to generate your report.")

def collect_information():
    customer_name = input("Enter customer name: ")
    item_name = input("Enter item name: ")
    priority_level = input("Enter priority level (low, medium, high): ")
    issue_description = input("Describe the issue: ")
    return customer_name, item_name, priority_level, issue_description

def save_report(report):
    try:
        with open('src/data/reports.txt', 'a') as file:
            file.write(report + '\n')
        print("Report saved successfully.")
    except Exception as e:
        print(f"Error saving report: {e}")

def main():
    greet_user()
    customer_name, item_name, priority_level, issue_description = collect_information()
    
    from diagnostic_tool import create_diagnostic_form, create_invoice_form
    
    diagnostic_form = create_diagnostic_form(customer_name, item_name, priority_level, issue_description)
    invoice_form = create_invoice_form(customer_name, item_name, priority_level, issue_description)
    
    print("\nDiagnostic Form:")
    print(diagnostic_form)
    
    print("\nInvoice Form:")
    print(invoice_form)
    
    save_report(diagnostic_form)
    save_report(invoice_form)

if __name__ == "__main__":
    main()