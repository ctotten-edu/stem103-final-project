# Collecting diagnostic information for the diagnostic form

def collect_diagnostic_info():
    print("\n--- Diagnostic Form ---")
    name = input("Customer Name: ")
    phone = input("Phone Number: ")
    
    issue_type = input("Main Issue (diagnostic, repair, maintenance, sale, other): ").strip().lower() 
    description = "" 
    email = None
    #If the issue is diagnostic, repair, or maintenance, ask for a description
    if issue_type in ['diagnostic', 'repair', 'maintenance']:
        description = input("Describe the issue (2-3 sentences): ")

    # Optional email
    email_prompt = input("Would you like to provide an email? (yes/no): ").strip().lower()
    if email_prompt == "yes":
        email = input("Email Address: ")

    return {
        "Customer Name": name,
        "Phone": phone,
        "Issue Type": issue_type,
        "Description": description,
        "Email": email or "Not Provided"
    }
