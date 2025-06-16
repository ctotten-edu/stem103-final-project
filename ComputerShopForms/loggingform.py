# Module for collecting logging form information

def collect_logging_info(urgency):
    print("\n--- Logging Form ---")

    make = input("Device Make: ")
    model = input("Device Model: ")
    serial = input("Serial Number: ")
    notes = input("Notes for future fixes: ")
    partslist = input("Parts needed (comma-separated): ")
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
