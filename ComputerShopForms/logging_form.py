def log_repair_details(info):
    print("--- Logging Form ---")
    make_model = input("Enter make and model of the item: ")
    serial_number = input("Enter serial number: ")
    task_notes = input("Enter elaboration of task details: ")

    return {
        'make_model': make_model,
        'serial_number': serial_number,
        'task_notes': task_notes
    }