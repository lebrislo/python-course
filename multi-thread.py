from multiprocessing import Process
import os
import time

processes = []
num_processes = os.cpu_count()

print("Number of processes: " + str(num_processes))

def square(n):
    for i in range(n):
        i * i
        print("Process ID: " + str(os.getpid()))
        time.sleep(0.1)

# Create processes
for i in range(num_processes):
    p = Process(target=square, args=(num_processes,))
    processes.append(p)

# Start processes
for p in processes:
    p.start()

# Join processes: wait for all processes to finish
for p in processes:
    p.join()

print("End of processes")


#create Thread
from threading import Thread

threads = []

for i in range(num_processes):
    t = Thread(target=square, args=(num_processes,))
    threads.append(t)

# start Thread
for t in threads:
    t.start()

# join Thread: wait for all threads to finish
for t in threads:
    t.join()

print("End of threads")