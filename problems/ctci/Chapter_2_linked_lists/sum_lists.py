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


m = ListNode(7, ListNode(1, ListNode(6, ListNode(1, None))))
n = ListNode(5, ListNode(9, ListNode(5, None)))

def sum_lists(m: ListNode, n:ListNode) -> ListNode:
    h = ListNode(int((m.val + n.val) % 10), None)
    c = int((m.val + n.val) / 10)

    while m.next and n.next:
        p = ListNode(int((m.next.val + n.next.val + c) % 10), h)
        h = p
        c = int((m.next.val + n.next.val + c) / 10)
        m = m.next
        n = n.next
        
    while m.next:
        if c:
            c = int(m.next.val + c / 10)
        p = ListNode(int((m.next.val + c) % 10), h)
        h = p
        m = m.next

    while n.next:
        if c:
            c = int(n.next.val + c/ 10)
        p = ListNode(int((n.next.val + c) % 10), h)
        h = p
        n = n.next    

    return h    

sum_lists(m, n).print()


m = ListNode(6, ListNode(1, ListNode(7, None)))
n = ListNode(2, ListNode(9, ListNode(5, None)))

def sum_lists_reverse(m : ListNode, n : ListNode) -> ListNode:
    m1 = m.val
    n1 = n.val
    while m.next:
        m1 = m1 * 10 + m.next.val
        m = m.next

    while n.next:
        n1 = n1 * 10 + n.next.val
        n = n.next

    s = str(m1 + n1)
    h = p = None
    for i in s:
        if p:
            p.next = ListNode(i, None)
            p = p.next
        else:
            h = ListNode(i, None)    
            p = h
    return h

sum_lists_reverse(m, n).print()