import time
from queue import Empty, Queue
from random import randint
from threading import Thread


def producer(queue):
    for i in range(1, 21):
        print(f'Inserting item {i} into the queue')
        time.sleep(0.1)
        queue.put(i)


def consumer(name, queue, speed = 1):
    while True:
        try:
            item = queue.get()
        except Empty:
            continue
        else:
            print(f'{name} processes item {item}')
            time.sleep(randint(1,10) / speed)
            queue.task_done()


def main():
    queue = Queue()

    # create a producer thread and start it
    producer_thread = Thread(
        target=producer,
        args=(queue,)
    )
    producer_thread.start()

    # create a consumer thread and start it
    consumer1_thread = Thread(
        target=consumer,
        args=("A", queue),
        daemon=True
    )
    consumer1_thread.start()

    consumer2_thread = Thread(
        target=consumer,
        args=("B", queue, 3),
        daemon=True
    )
    consumer2_thread.start()

    # wait for all tasks to be added to the queue
    producer_thread.join()

    # wait for all tasks on the queue to be completed
    queue.join()


if __name__ == '__main__':
    main()