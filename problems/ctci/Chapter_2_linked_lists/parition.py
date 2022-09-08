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

m = ListNode(3, ListNode(5, ListNode(8, ListNode(5, ListNode(10, ListNode(2, ListNode(1, ListNode(1, None))))))))
m.print()


def partition(h:ListNode, n:int) -> ListNode:
    p = h   
    l = h
    q = None

    while l.next:
        if l.next.val < n and l != p:
            q = l.next
            h = q
            if q.next:
                l.next = q.next
            else:
                l.next = None    
            q.next = p
            p = q
        else:
            l = l.next    

    return h        

partition(m, 5).print()