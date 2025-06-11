from datetime import datetime

try:
    customer_info = collect_customer_info()
    item_info = collect_item_info()
    priority = collect_priority()
    issue = collect_issue()
    if not issue:
        return
except Exception as e:
    print(f"Unexpected error: {e}")
    return