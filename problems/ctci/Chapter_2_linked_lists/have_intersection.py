class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print(self):
        p = self
        while p.next:
            print(p.val)
            p = p.next
        print(p.val, "\n")  


p = ListNode(8, ListNode(2, None))
m = ListNode(7, ListNode(1, ListNode(6, ListNode(1, p))))
n = ListNode(5, ListNode(9, ListNode(5, p)))

m1 = ListNode(7, ListNode(1, ListNode(6, ListNode(1, None))))
n1 = ListNode(5, ListNode(9, ListNode(5, None)))

def have_intersection(m : ListNode, n : ListNode) -> ListNode:
    l = 0
    s = 1
    t = m
    k = n
    while t:
        l += 1
        t = t.next

    while n:
        p = n
        n = n.next
        p.next = None        

    while m.next:
        s += 1
        m = m.next

    if s != l:
        return m
    return None

print(have_intersection(n, m))
print(have_intersection(n1, m1))


