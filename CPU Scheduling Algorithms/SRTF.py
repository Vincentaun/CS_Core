def srtf(processes, arrival_time, burst_time):
    """
    Simulate Shortest Remaining Time First (SRTF) Scheduling.
    :param processes: List of process IDs.
    :param arrival_time: List of arrival times for each process.
    :param burst_time: List of burst times for each process.
    :return: Average waiting time and turnaround time.
    """
    n = len(processes)
    remaining_time = burst_time[:]
    waiting_time = [0] * n
    turnaround_time = [0] * n
    completed = 0  # Number of completed processes
    current_time = 0  # Track the current time
    min_remaining_time = float("inf")
    shortest = 0
    check = False

    while completed != n:
        # Find process with the shortest remaining time at the current time
        for i in range(n):
            if (arrival_time[i] <= current_time and
                remaining_time[i] < min_remaining_time and
                remaining_time[i] > 0):
                min_remaining_time = remaining_time[i]
                shortest = i
                check = True

        if not check:  # If no process is ready, move time forward
            current_time += 1
            continue

        # Execute the shortest process
        remaining_time[shortest] -= 1
        min_remaining_time = remaining_time[shortest]
        if min_remaining_time == 0:
            min_remaining_time = float("inf")

        # If a process is completed
        if remaining_time[shortest] == 0:
            completed += 1
            check = False
            finish_time = current_time + 1

            # Calculate waiting time
            waiting_time[shortest] = (finish_time - burst_time[shortest] -
                                      arrival_time[shortest])

            if waiting_time[shortest] < 0:
                waiting_time[shortest] = 0

        current_time += 1

    # Calculate Turnaround Time
    for i in range(n):
        turnaround_time[i] = burst_time[i] + waiting_time[i]

    # Calculate average waiting time and turnaround time
    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n

    return avg_waiting_time, avg_turnaround_time, waiting_time, turnaround_time


# Example usage
processes = [1, 2, 3, 4]
arrival_time = [0, 1, 2, 3]  # Arrival times for each process
burst_time = [8, 4, 9, 5]  # Burst times for each process

avg_wait, avg_turnaround, wait_times, turnarounds = srtf(processes, arrival_time, burst_time)

print("Processes:", processes)
print("Arrival Times:", arrival_time)
print("Burst Times:", burst_time)
print("Waiting Times:", wait_times)
print("Turnaround Times:", turnarounds)
print(f"Average Waiting Time: {avg_wait:.2f}")
print(f"Average Turnaround Time: {avg_turnaround:.2f}")
