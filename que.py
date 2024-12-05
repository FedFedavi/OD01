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

    def all_que(self):
        if not self.is_empty():
            for item in reversed(self.items):
                print(item)


que = Que()
print(que.is_empty())
que.enque("действие 1")
que.enque("действие 2")
que.enque("действие 3")
que.enque("действие 4")
que.all_que()
print(que.is_empty())
print(que.size())
print(que.deque())

print(que.size())
que.all_que()
