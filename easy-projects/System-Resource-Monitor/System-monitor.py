import psutil # type: ignore
import time
import os

def clear_terminal():
    """Clear terminal screen for better readability"""
    os.system('clear' if os.name == 'posix' else 'cls')

def display_system_stats():
    """Display system stats in a clean format"""
    while True:
        clear_terminal()
        print("="*40)
        print("   SYSTEM RESOURCE MONITOR")
        print("="*40)

        # CPU Usage
        print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")

        # Memory Usage
        mem = psutil.virtual_memory()
        print(f"Memory Usage: {mem.percent}% ({mem.used / 1e9:.2f}GB/{mem.total / 1e9:.2f}GB)")

        # Disk Usage
        disk = psutil.disk_usage('/')
        print(f"Disk Usage: {disk.percent}% ({disk.used / 1e9:.2f}GB/{disk.total / 1e9:.2f}GB)")

        # Refresh every second
        time.sleep(3)

if __name__ == "__main__":
    display_system_stats()
