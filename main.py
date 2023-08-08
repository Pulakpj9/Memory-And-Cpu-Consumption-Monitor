import psutil
import os
import time

def get_process_info(process):
    try:
        process_name = process.name()
        process_cpu_percent = process.cpu_percent(interval=None)
        process_memory_info = process.memory_info()

        return {
            "Name": process_name,
            "CPU Usage (%)": process_cpu_percent,
            "Memory Usage (MB)": process_memory_info.rss / (1024 * 1024),
        }
    except psutil.AccessDenied:
        return None

def main():
    try:
        while True:
            processes = []
            for process in psutil.process_iter(attrs=['pid', 'name']):
                process_info = get_process_info(process)
                if process_info:
                    processes.append(process_info)

            sorted_processes_by_cpu = sorted(processes, key=lambda x: x["CPU Usage (%)"], reverse=True)
            sorted_processes_by_memory = sorted(processes, key=lambda x: x["Memory Usage (MB)"], reverse=True)

            os.system("cls" if os.name == "nt" else "clear")
            print("Processes sorted by CPU usage:")
            for process in sorted_processes_by_cpu:
                print(process)

            print("\nProcesses sorted by Memory usage:")
            for process in sorted_processes_by_memory:
                print(process)

            time.sleep(120)
            
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
