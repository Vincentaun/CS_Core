class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

def fcfs_scheduling(processes):
    # Sort processes by arrival time
    processes.sort(key=lambda p: p.arrival_time)

    current_time = 0
    for process in processes:
        if current_time < process.arrival_time:
            current_time = process.arrival_time
        
        # Calculate completion time
        process.completion_time = current_time + process.burst_time
        current_time = process.completion_time
        
        # Calculate turnaround time
        process.turnaround_time = process.completion_time - process.arrival_time
        
        # Calculate waiting time
        process.waiting_time = process.turnaround_time - process.burst_time

def print_schedule(processes):
    print(f"{'PID':<5} {'AT':<5} {'BT':<5} {'CT':<5} {'TAT':<5} {'WT':<5}")
    for process in processes:
        print(f"{process.pid:<5} {process.arrival_time:<5} {process.burst_time:<5} "
              f"{process.completion_time:<5} {process.turnaround_time:<5} {process.waiting_time:<5}")

# Example usage
if __name__ == "__main__":
    processes = [
        Process(pid=1, arrival_time=0, burst_time=5),
        Process(pid=2, arrival_time=1, burst_time=3),
        Process(pid=3, arrival_time=2, burst_time=8),
        Process(pid=4, arrival_time=3, burst_time=6)
    ]

    fcfs_scheduling(processes)
    print_schedule(processes)
