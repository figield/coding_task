from threading import Thread


class CustomThread(Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.result = None

    def run(self):
        print(f"run thread {self.name}")
        self.result = self.name


def func(argu1, return_value):
    result = f"{argu1}"
    print(f"In thread: {result}")
    return return_value.append(result)


if __name__ == "__main__":
    results = []
    thread1 = CustomThread(name="1")
    thread2 = CustomThread(name="2")

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    results.append(thread1.result)
    results.append(thread2.result)
    print(results)
