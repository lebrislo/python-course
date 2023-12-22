from multiprocessing import Process, Value, Array, Lock, Pool
import os
import time

def add_100(number, lock):
    for _ in range(100):
        time.sleep(0.01)
        with lock:
            number.value += 1

def add_100_array(numbers, lock):
    for _ in range(100):
        time.sleep(0.01)
        for i in range(len(numbers)):
            with lock:
                numbers[i] += 1

def cube(number):
    return number**3

if __name__ == '__main__':

    lock = Lock()
    shared_number = Value('i', 0)
    print("Value at begginning", shared_number.value)

    p1 = Process(target=add_100, args=(shared_number,lock))
    p2 = Process(target=add_100, args=(shared_number,lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Value at end", shared_number.value)

    shared_array = Array('d', [0.0, 100.0, 200.0])
    print("Array at begginning", shared_array[:])

    p3 = Process(target=add_100_array, args=(shared_array,lock))
    p4 = Process(target=add_100_array, args=(shared_array,lock))

    p3.start()
    p4.start()

    p3.join()
    p4.join()

    print("Array at end", shared_array[:])

    pool = Pool()

    result = pool.map(cube, range(1,7))

    pool.close()
    pool.join()

    print(result)