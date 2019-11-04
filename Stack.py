class A:
    pass


class B(A):
    pass


class Stack:
    stack_list = []

    def __init__(self, stack_type):
        self.stack_list = list()
        self.stack_type = stack_type

    def __str__(self):
        return str(self.stack_list)

    def push(self, *args):
        for arg in args:
            if not type(arg) is self.stack_type and not issubclass(type(arg), self.stack_type):
                raise TypeError()
            self.stack_list.append(arg)

    def pop(self):
        res = self.stack_list[len(self.stack_list) - 1]
        del self.stack_list[len(self.stack_list) - 1]
        return res

    def clear(self):
        self.stack_list = list()

    def is_empty(self):
        return True if len(self.stack_list) == 0 else False


# bad tests
'''test_stack = Stack(int)
print('start stack:', test_stack)
test_stack.push(1, 2, 3, 4, 5)
print('push: ', test_stack)
a = test_stack.pop()
print('pop:', test_stack, '   a =', a)

a = A()
b = B()
test_stack = Stack(A)
print('new stack:', test_stack)
test_stack.push(a)
test_stack.push(b)
print('От наследника:', test_stack)
print('Is Empty:', test_stack.is_empty())
test_stack.clear()
print('clear:', test_stack)
print('Is Empty:', test_stack.is_empty())'''
