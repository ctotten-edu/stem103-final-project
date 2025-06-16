# Collecting diagnostic information for the diagnostic form
def get_nonempty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        else:
            print("This field cannot be empty. Please try again.")

def collect_diagnostic_info():
    print("\n--- Diagnostic Form ---")
    name = get_nonempty_input("Customer Name: ")
    phone = get_nonempty_input("Phone Number: ")
    
    issue_type = get_nonempty_input("Main Issue (diagnostic, repair, maintenance, sale, other): ").strip().lower() 
    description = "" 
    email = None
    #If the issue is diagnostic, repair, or maintenance, ask for a description
    if issue_type in ['diagnostic', 'repair', 'maintenance']:
        description = get_nonempty_input("Describe the issue (2-3 sentences): ")

    # Optional email
    email_prompt = get_nonempty_input("Would you like to provide an email? (yes/no): ").strip().lower()
    if email_prompt == "yes":
        email = get_nonempty_input("Email Address: ")

    return {
        "Customer Name": name,
        "Phone": phone,
        "Issue Type": issue_type,
        "Description": description,
        "Email": email or "Not Provided"
    }
