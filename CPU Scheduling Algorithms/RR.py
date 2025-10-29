def round_robin(processes, burst_time, quantum):
    """
    Simulate Round Robin CPU Scheduling.
    :param processes: List of process IDs.
    :param burst_time: List of burst times for each process.
    :param quantum: Time quantum for Round Robin.
    :return: Average waiting time and turnaround time.
    """
    n = len(processes)
    remaining_time = burst_time[:]
    waiting_time = [0] * n
    turnaround_time = [0] * n
    current_time = 0  # Track the current time

    # Process the queue using the time quantum
    while True:
        done = True
        for i in range(n):
            if remaining_time[i] > 0:
                done = False  # There's still at least one process left
                if remaining_time[i] > quantum:
                    # Process can only execute for 'quantum' time
                    current_time += quantum
                    remaining_time[i] -= quantum
                else:
                    # Process completes within remaining time
                    current_time += remaining_time[i]
                    waiting_time[i] = current_time - burst_time[i]
                    remaining_time[i] = 0

        if done:
            break

    # Calculate Turnaround Time
    for i in range(n):
        turnaround_time[i] = burst_time[i] + waiting_time[i]

    # Calculate average waiting time and turnaround time
    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n

    return avg_waiting_time, avg_turnaround_time, waiting_time, turnaround_time


processes = [1, 2, 3, 4]
burst_time = [10, 5, 8, 6]  # Burst times for each process
quantum = 3  # Time quantum

avg_wait, avg_turnaround, wait_times, turnarounds = round_robin(processes, burst_time, quantum)

print("Processes:", processes)
print("Burst Times:", burst_time)
print("Time Quantum:", quantum)
print("Waiting Times:", wait_times)
print("Turnaround Times:", turnarounds)
print(f"Average Waiting Time: {avg_wait:.2f}")
print(f"Average Turnaround Time: {avg_turnaround:.2f}")
