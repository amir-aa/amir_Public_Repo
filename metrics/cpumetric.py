import psutil
import time

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def monitor_cpu_usage():
    while True:
        cpu_percent = get_cpu_usage()
        yield cpu_percent
        time.sleep(5)
for item in monitor_cpu_usage():

    print(f"CPU Usage: {item}%")

