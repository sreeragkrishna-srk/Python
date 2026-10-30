import time
from typing import Callable

# Decorators
def log_activity(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        print(f"[LOG] Executing function '{func.__name__}'...")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"[LOG] Finished '{func.__name__}' in {end_time - start_time:.4f}s")
        return result
    return wrapper

@log_activity
def run_data_pipeline(records: list) -> int:
    time.sleep(0.3)
    return len(records)

total_records = run_data_pipeline([100, 200, 300, 400, 500])

# Context Manager
with open("system_audit.txt", "w") as audit_file:
    audit_file.write("Audit Entry: Pipeline processed successfully.\n")

print("Audit file created and closed successfully.")