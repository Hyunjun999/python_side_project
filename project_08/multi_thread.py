import threading, time


def thread_name(t_name):
    for _ in range(10):
        print(t_name)
        time.sleep(0.2)


def sum(name, value):
    for e in list(map(lambda x: f"{name} : {x}", range(value))):
        print(e)


t1 = threading.Thread(target=sum, args=("thread #1", 10))
t2 = threading.Thread(target=sum, args=("thread #2", 10))
t3 = threading.Thread(target=thread_name, args=("Custom thread",))
# Since we have to pass the tuple type for the args parameter, even if it requires a single argument,
# we have to add a comma to make it tuple to create a singleton tuple
t1.start()
t2.start()
print("main thread")
t3.start()
