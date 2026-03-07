import psutil


def get_system_metrics():
    """
        This API get the system metrics (cpu disk and health check)
    """
    
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_percent = psutil.virtual_memory().percent
    total_memory = psutil.virtual_memory().total
    disk_usage = psutil.disk_usage("/").percent
    threshold = 40
    status ="High cpu" if cpu_percent>threshold else "Healthy"

    return {
        "total_memory":total_memory,
        "cpu_percent":cpu_percent,
        "memory_percent":memory_percent,
        "disk_usage":disk_usage,
        "cpu_threshold":threshold,
        "system_health": status,
    }