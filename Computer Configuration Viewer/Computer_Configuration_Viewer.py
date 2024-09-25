import tkinter as tk
import platform
import psutil
import socket

# Function to gather system info
def get_system_info():
    uname = platform.uname()
    
    # CPU information
    cpu_info = f"Processor: {uname.processor}"
    cpu_cores = f"CPU Cores: {psutil.cpu_count(logical=False)} (Physical), {psutil.cpu_count(logical=True)} (Logical)"
    cpu_freq = f"CPU Frequency: {psutil.cpu_freq().current:.2f} MHz"
    cpu_usage = f"CPU Usage: {psutil.cpu_percent(interval=1)}%"
    
    # RAM and swap memory
    ram_info = f"RAM: {round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB"
    swap_info = f"Swap Memory: {round(psutil.swap_memory().total / (1024 ** 3), 2)} GB"
    
    # Disk information
    disk_info = ""
    partitions = psutil.disk_partitions()
    for partition in partitions:
        disk_usage = psutil.disk_usage(partition.mountpoint)
        disk_info += f"{partition.device}: {round(disk_usage.total / (1024 ** 3), 2)} GB, " \
                     f"Used: {round(disk_usage.used / (1024 ** 3), 2)} GB, Free: {round(disk_usage.free / (1024 ** 3), 2)} GB\n"
    
    # Network information
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    net_info = f"Hostname: {hostname}\nIP Address: {ip_address}"
    
    # System info
    sys_info = f"System: {uname.system} {uname.release} ({uname.version})"
    machine_info = f"Machine: {uname.machine}"
    
    return (cpu_info, cpu_cores, cpu_freq, cpu_usage, ram_info, swap_info, disk_info, net_info, sys_info, machine_info)

# Function to gather thread information
def get_thread_info():
    thread_info = ""
    processes = psutil.pids()
    for pid in processes[:10]:  # Displaying thread info for the first 10 processes
        try:
            process = psutil.Process(pid)
            threads = process.threads()
            thread_info += f"PID: {pid}, Name: {process.name()}, Threads: {len(threads)}\n"
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return thread_info

# Function to display system and thread info in the GUI
def display_system_info():
    cpu_info, cpu_cores, cpu_freq, cpu_usage, ram_info, swap_info, disk_info, net_info, sys_info, machine_info = get_system_info()
    thread_info = get_thread_info()
    
    # Update each section in the GUI
    cpu_label.config(text=f"{cpu_info}\n{cpu_cores}\n{cpu_freq}\n{cpu_usage}")
    memory_label.config(text=f"RAM: {ram_info}\nSwap: {swap_info}")
    disk_label.config(text=disk_info)
    network_label.config(text=net_info)
    system_label.config(text=f"{sys_info}\n{machine_info}")
    thread_label.config(text=thread_info)

# Set up GUI using Tkinter
root = tk.Tk()
root.title("Computer Configuration")
root.geometry("900x600")

# Create frames for system information (Left side)
left_frame = tk.Frame(root)
left_frame.pack(side="left", fill="both", expand=True, padx=20, pady=10)

# Create frames for each section on the left side
cpu_frame = tk.Frame(left_frame, bd=2, relief=tk.SUNKEN, padx=10, pady=10)
cpu_frame.pack(fill="both", pady=10)
cpu_title = tk.Label(cpu_frame, text="CPU Information", font=("Arial", 14, "bold"))
cpu_title.pack(anchor="w")
cpu_label = tk.Label(cpu_frame, text="", justify="left", font=("Arial", 12))
cpu_label.pack(anchor="w")

memory_frame = tk.Frame(left_frame, bd=2, relief=tk.SUNKEN, padx=10, pady=10)
memory_frame.pack(fill="both", pady=10)
memory_title = tk.Label(memory_frame, text="Memory Information", font=("Arial", 14, "bold"))
memory_title.pack(anchor="w")
memory_label = tk.Label(memory_frame, text="", justify="left", font=("Arial", 12))
memory_label.pack(anchor="w")

disk_frame = tk.Frame(left_frame, bd=2, relief=tk.SUNKEN, padx=10, pady=10)
disk_frame.pack(fill="both", pady=10)
disk_title = tk.Label(disk_frame, text="Disk Information", font=("Arial", 14, "bold"))
disk_title.pack(anchor="w")
disk_label = tk.Label(disk_frame, text="", justify="left", font=("Arial", 12))
disk_label.pack(anchor="w")

network_frame = tk.Frame(left_frame, bd=2, relief=tk.SUNKEN, padx=10, pady=10)
network_frame.pack(fill="both", pady=10)
network_title = tk.Label(network_frame, text="Network Information", font=("Arial", 14, "bold"))
network_title.pack(anchor="w")
network_label = tk.Label(network_frame, text="", justify="left", font=("Arial", 12))
network_label.pack(anchor="w")

system_frame = tk.Frame(left_frame, bd=2, relief=tk.SUNKEN, padx=10, pady=10)
system_frame.pack(fill="both", pady=10)
system_title = tk.Label(system_frame, text="System Information", font=("Arial", 14, "bold"))
system_title.pack(anchor="w")
system_label = tk.Label(system_frame, text="", justify="left", font=("Arial", 12))
system_label.pack(anchor="w")

# Create frames for thread information (Right side)
right_frame = tk.Frame(root)
right_frame.pack(side="right", fill="both", expand=True, padx=20, pady=10)

thread_frame = tk.Frame(right_frame, bd=2, relief=tk.SUNKEN, padx=10, pady=10)
thread_frame.pack(fill="both", pady=10)
thread_title = tk.Label(thread_frame, text="Thread Information", font=("Arial", 14, "bold"))
thread_title.pack(anchor="w")
thread_label = tk.Label(thread_frame, text="", justify="left", font=("Arial", 12))
thread_label.pack(anchor="w")

# Create a button to refresh and display system information
info_button = tk.Button(root, text="Show/Refresh Computer Configuration", command=display_system_info, font=("Arial", 14))
info_button.pack(pady=20)

# Start the main loop
root.mainloop()