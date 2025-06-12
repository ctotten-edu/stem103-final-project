import re
from datetime import datetime

def collect_diagnostic_info():
    # Get current time for the record
    check_in_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    file_timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    file_name = f"diagnostic_{file_timestamp}.txt"
    print("--- Diagnostic Form ---")

    customer_name = input("Enter customer name: ")
    item_name = input("Enter item name (e.g., Desktop, Laptop, etc.): ")
    
    # Present choices for issue description
    issue_description = ""
    while issue_description.lower() not in ['diagnostic', 'repair', 'maintenance', 'sale', 'other']:
        issue_description = input("Enter issue type (Diagnostic, Repair, Maintenance, Sale, Other): ")

    # Phone number with error handling
    while True:
        customer_phone = input("Enter customer phone number (e.g., 123-456-7890): ")
        if re.match(r"^\d{3}-\d{3}-\d{4}$", customer_phone):
            break
        else:
            print("Invalid phone format. Please use 123-456-7890 format.")

    customer_email = input("Enter customer email (or type 'skip'): ")
    if customer_email.lower() == 'skip':
        customer_email = 'N/A'

    return {
        'check_in_time': check_in_time,
        'customer_name': customer_name,
        'item_name': item_name,
        'issue_description': issue_description.lower(),
        'customer_phone': customer_phone,
        'customer_email': customer_email
    }