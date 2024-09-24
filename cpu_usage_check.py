import psutil

# Get the number of logical CPUs (including hyper-threaded ones)
total_logical_cpus = psutil.cpu_count()

# Get the CPU usage percentage for each logical CPU
cpu_usage = psutil.cpu_percent(interval=1, percpu=True)

# Find out how many logical CPUs are actively used
active_cpus = sum(1 for usage in cpu_usage if usage > 0)

print(f"Total number of logical CPUs: {total_logical_cpus}")
print(f"Number of actively used logical CPUs: {active_cpus}")