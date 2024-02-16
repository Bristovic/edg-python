# a procedural approach to a v. simple stack
stack = []


# function to "push" to stack
def push(val):
    stack.append(val)


# function to "pop" from stack
def pop():
    val = stack[-1]
    del stack[-1]
    return val


# examples
push(3)  # add 3 as 1st stack element
print(stack)  # print stack: [3]

push(2)  # add element: 2
push(1)  # add element: 1
print(stack)  # print stack: [3, 2, 1]

print(pop())  # pop "top" element and print value
print(stack)  # print stack ([3, 2]) to demonstrate stack change


# an object-oriented approach to the stack
# creating a new Stack class
class Stack:
    # constructor function, invoked on instantiation
    def __init__(self):
        # constructor initiates empty stack_list
        # __ before name makes the property private
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]  # could just use .pop() method
        return val


little_stack = Stack()
another_stack = Stack()
fun_stack = Stack()

little_stack.push(1)
another_stack.push(little_stack.pop())
fun_stack.push(another_stack.pop())

print(fun_stack.pop())


# creating a subclass
# name in brackets points to superclass for new subclass
class AddingStack(Stack):
    # constructor
    def __init__(self):
        # explicitly invoke superclass constructor
        # to provide its init properties
        Stack.__init__(self)
        # initiate new sum variable
        self.__sum = 0

    # new method, to get sum
    def get_sum(self):
        # simply returns value of sum property
        # allowing reading but not editing of sum
        # except via methods
        return self.__sum

    # redefine push method from superclass
    def push(self, val):
        # add the val value to the sum variable
        self.__sum += val
        # explicitly invoke the superclass and its attendant method
        # passing self as target, and val as val
        Stack.push(self, val)

    # redefine the pop method from superclass
    def pop(self):
        # use superclass pop, explicitly invoked, to pop value
        val = Stack.pop(self)
        # subtract returned val from sum property
        self.__sum -= val
        # return val as result
        return val


# testing data
stack_object = AddingStack()

for i in range(5):
    stack_object.push(i)
print(stack_object.get_sum())

for i in range(5):
    print(stack_object.pop())
