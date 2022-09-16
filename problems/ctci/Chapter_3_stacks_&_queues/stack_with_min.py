class Node:
    def __init__(self, val = 0, next = None) -> None:
        self.val = val
        self.min = val
        self.next = next

    def __str__(self):
        return "Val : " + str(self.val) + " Min : " + str(self.min)
        

class Stack:
    def __init__(self) -> None:
        self.head = None

    def __str__(self):
        p = self.head
        while p:
            print(p)
            p = p.next
        return ""    


    def pop(self) -> Node:
        if not self.head:
            return    
        else:
            p = self.head
            self.head = self.head.next
            return p
    
    def peek(self) -> Node:
        return self.head

    def push(self, n : Node):
        if not self.head:
            self.head = n
        else:
            n.next = self.head
            n.min = min(n.val, self.head.min)
            self.head = n

    def min(self):
        return self.head.min

s = Stack()

s.push(Node(5))
s.push(Node(4))
s.push(Node(6))
print(s.min())
print(s.peek())
print(s)
s.pop()
print(s)