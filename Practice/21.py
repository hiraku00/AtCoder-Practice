import threading

def fizzbuzz(start, end):
    for i in range(start, end+ 1 ):
        if i % 15 == 0:
            print(f"{threading.current_thread().name} : FizzBuzz")
        elif i % 3 == 0:
            print(f"{threading.current_thread().name} : Fizz")
        elif i % 5 == 0:
            print(f"{threading.current_thread().name} : Buzz")
        else:
            print(f"{threading.current_thread().name} : {i}")

if __name__ == "__main__":
    threads = []
    threads.append(threading.Thread(target=fizzbuzz, args=(1, 33), name="Thread1"))
    threads.append(threading.Thread(target=fizzbuzz, args=(36, 66), name="Thread2"))
    threads.append(threading.Thread(target=fizzbuzz, args=(67, 100), name="Thread3"))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
