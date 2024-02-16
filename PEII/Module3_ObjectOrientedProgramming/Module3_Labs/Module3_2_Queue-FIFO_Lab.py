# Queue AKA FIFO lab

# new queue error class
class QueueError(IndexError):
    pass


# new queue class (first in - first out)
class Queue:
    def __init__(self):
        self.__q_list = []

    def put(self, elem):
        self.__q_list.append(elem)

    def get(self):
        if len(self.__q_list) > 0:
            got = self.__q_list[0]
            del self.__q_list[0]
            return got
        else:
            raise QueueError

# test data
que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")
