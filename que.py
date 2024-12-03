class Que:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enque(self, item):
        self.items.insert(0, item)

    def deque(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


que = Que()
print(que.is_empty())
que.enque("действие 1")
que.enque("действие 2")
que.enque("действие 3")
que.enque("действие 4")

print(que.is_empty())
print(que.size())
print(que.deque())

print(que.size())
