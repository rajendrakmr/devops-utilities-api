
def analyze_logs(logs: list):

    result = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    for log in logs: 
        if "ERROR" in log:
            result["ERROR"] += 1 
        elif "WARNING" in log:
            result["WARNING"] += 1 
        else:
            result["INFO"] += 1

    return result