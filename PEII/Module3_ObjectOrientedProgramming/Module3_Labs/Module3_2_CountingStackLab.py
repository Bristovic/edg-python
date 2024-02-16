# base stack class
class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


# subclass that counts number of pushes and pops
class CountStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__push_count = 0
        self.__pop_count = 0

    # new method to get push count
    def get_push_count(self):
        return self.__push_count

    # new method to get pop count
    def get_pop_count(self):
        return self.__pop_count

    # new method to get element count
    def get_el_count(self):
        return self.__push_count - self.__pop_count

    def push(self, val):
        self.__push_count += 1
        Stack.push(self, val)

    def pop(self):
        self.__pop_count += 1
        val = Stack.pop(self)
        return val


# test data
stk = CountStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_pop_count())
print(stk.get_push_count())
print(stk.get_el_count())
