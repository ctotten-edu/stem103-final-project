from datetime import datetime
from diagnostic_form import collect_diagnostic_info
from invoice_form import generate_invoice
from logging_form import log_repair_details

def save_repair_ticket(diagnostic_info, invoice_info, log_info):
    try:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        file_name = f"Repair_Ticket_{timestamp}.txt"
        with open(file_name, "w") as file:
            file.write("--- Repair Ticket ---\n")
            file.write(f"Check-in Time: {diagnostic_info['check_in_time']}\n")
            file.write(f"Customer: {diagnostic_info['customer_name']}\n")
            file.write(f"Phone: {diagnostic_info['customer_phone']}\n")
            file.write(f"Email: {diagnostic_info['customer_email']}\n")
            file.write(f"Item: {diagnostic_info['item_name']}\n")
            file.write(f"Issue Type: {diagnostic_info['issue_description']}\n")
            file.write(f"Urgency/Details: {invoice_info['urgency']}\n")
            file.write(f"Labor Cost: ${invoice_info['labor_cost']}\n")
            file.write(f"Total Diagnostic + Labor Cost: ${invoice_info['diagnostic_cost']}\n")
            file.write(f"Turnaround Time: {invoice_info['turnaround_time']}\n")
            file.write(f"Make/Model: {log_info['make_model']}\n")
            file.write(f"Serial Number: {log_info['serial_number']}\n")
            file.write(f"Task Notes: {log_info['task_notes']}\n")
            file.write("-----------------------\n")
        print(f"Repair Ticket saved successfully as '{file_name}'.")
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")

def main():
    diagnostic_info = collect_diagnostic_info()
    invoice_info = generate_invoice(diagnostic_info)
    log_info = log_repair_details(diagnostic_info)
    save_repair_ticket(diagnostic_info, invoice_info, log_info)

if __name__ == '__main__':
    main()