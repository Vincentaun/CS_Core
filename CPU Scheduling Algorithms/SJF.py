# Function to perform Shortest Job First Scheduling
def sjf_scheduling(processes):
    # Sort processes based on their burst time (execution time)
    processes.sort(key=lambda x: x['burst_time'])
    
    # Initialize variables
    total_wait_time = 0
    total_turnaround_time = 0
    current_time = 0
    schedule = []
    
    print("\nProcess Execution Order:")
    print("Process\tBurst Time\tWaiting Time\tTurnaround Time")
    
    for process in processes:
        # Calculate waiting time for the current process
        waiting_time = current_time - process['arrival_time']
        waiting_time = max(waiting_time, 0)  # Ensure it's not negative
        
        # Calculate turnaround time
        turnaround_time = current_time + process['burst_time']
        
        # Update total times
        total_wait_time += waiting_time
        total_turnaround_time += turnaround_time
        
        # Update the current time to reflect the execution of the process
        current_time = turnaround_time
        
        # Add the process to the schedule
        schedule.append({
            'Process': process['name'],
            'Burst Time': process['burst_time'],
            'Waiting Time': waiting_time,
            'Turnaround Time': turnaround_time
        })
        
        # Print the process details
        print(f"{process['name']}\t{process['burst_time']}\t\t{waiting_time}\t\t{turnaround_time}")
    
    # Calculate average waiting time and turnaround time
    avg_wait_time = total_wait_time / len(processes)
    avg_turnaround_time = total_turnaround_time / len(processes)
    
    print(f"\nAverage Waiting Time: {avg_wait_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")
    
    return schedule


# Example: Define the processes
processes = [
    {'name': 'P1', 'arrival_time': 0, 'burst_time': 6},
    {'name': 'P2', 'arrival_time': 1, 'burst_time': 8},
    {'name': 'P3', 'arrival_time': 2, 'burst_time': 7},
    {'name': 'P4', 'arrival_time': 3, 'burst_time': 3},
]

# Perform SJF Scheduling
schedule = sjf_scheduling(processes)
