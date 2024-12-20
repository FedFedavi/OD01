class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
            return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("стек пуст")

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


stack = Stack()

print(stack.is_empty())
print(stack.size())
try:
    print(stack.peek())
except IndexError as e:
    print(e)

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print(stack.is_empty())
print(stack.size())
print(stack.peek())
print(stack.__str__())
