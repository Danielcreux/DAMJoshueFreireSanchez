import psutil

def get_system_load():
    # Get CPU load as a percentage
    cpu_load = psutil.cpu_percent(interval=1)

    # Get RAM usage
    memory = psutil.virtual_memory()
    total_ram = memory.total / (1024 ** 3)  # Convert bytes to GB
    used_ram = memory.used / (1024 ** 3)   # Convert bytes to GB
    ram_usage_percentage = memory.percent

    return [int(time.time()),cpu_load,ram_usage_percentage]

if __name__ == "__main__":
    while True:
        print(get_system_load())
        time.sleep(1)
