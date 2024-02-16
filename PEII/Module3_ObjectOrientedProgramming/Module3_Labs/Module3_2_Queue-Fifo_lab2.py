# extension of queue FIFO material
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


# new SuperQueue subclass that can say if empty or not
# easy if queue property is public, not so if private
class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)
        self.q_length = 0

    def is_empty(self):
        return self.q_length == 0

    def put(self, elem):
        self.q_length += 1
        Queue.put(self, elem)

    def get(self):
        self.q_length -= 1
        got = Queue.get(self)
        return got


# test data
que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.is_empty():
        print(que.get())
    else:
        print("Queue empty")
        