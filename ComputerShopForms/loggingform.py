# Module for collecting logging form information
def get_nonempty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        else:
            print("This field cannot be empty. Please try again.")

def collect_logging_info(urgency):
    print("\n--- Logging Form ---")

    make = get_nonempty_input("Device Make: ")
    model = get_nonempty_input("Device Model: ")
    serial = get_nonempty_input("Serial Number: ")
    notes = get_nonempty_input("Notes for future fixes: ")
    partslist = get_nonempty_input("Parts needed (comma-separated): ")
    callback_times = {
        'rush': "6 hours",
        'priority': "1 day",
        'standard': "2 days"
    }

    callback = callback_times.get(urgency, "unknown")

    return {
        "Make": make,
        "Model": model,
        "Serial": serial,
        "Future Notes": notes,
        "Parts Needed": partslist,
        "Proposed Callback Time": callback
    }
