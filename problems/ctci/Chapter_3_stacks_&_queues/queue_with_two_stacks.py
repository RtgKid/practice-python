class MyQueue:
    def __init__(self):
        self.s_new = []
        self.s_old = []

    def __str__(self) -> str:
        copy_s_old = self.s_old.copy()
        copy_s_old.reverse()
        return ' '.join(map(str, copy_s_old + self.s_new))

    def move_new_to_old_stack(self):
        while len(self.s_new) > 0:
            self.s_old.append(self.s_new.pop())

    def add(self, n : int) :
        self.s_new.append(n)

    def peek(self) -> int:
        if len(self.s_old) == 0:
            self.move_new_to_old_stack()
        return self.s_old[-1]

    def pop(self) -> int:
        if len(self.s_old) == 0:
            self.move_new_to_old_stack()
        return self.s_old.pop()


q = MyQueue()
q.add(1)
q.add(2)
q.add(3)
print(q)
print(q.peek())
print(q.pop())
print(q)
q.add(5)
print(q)