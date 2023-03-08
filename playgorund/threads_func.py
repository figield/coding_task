from threading import Thread


def func(argu1, return_value):
    result = f"{argu1}"
    print(f"In thread: {result}")
    return return_value.append(result)

if __name__ == "__main__":
    results = []
    thread1 = Thread(target=func, args=(1, results))
    thread2 = Thread(target=func, args=(2, results))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(results)