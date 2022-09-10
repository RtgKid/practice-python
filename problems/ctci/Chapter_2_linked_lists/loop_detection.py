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

c = ListNode(1, None)
p = ListNode(5, ListNode(10, ListNode(2, ListNode(1, c))))
c.next = p
m = ListNode(3, ListNode(5, ListNode(8, p)))
 
def detect_loop(h : ListNode) -> ListNode:
    l = t = n = h
    if not h.next or not h.next.next:
        return
    
    l = l.next
    t = h.next.next
    while t != l:
        l = l.next
        t = t.next.next
    
    while l != n:
        l = l.next
        n = n.next

    return l    


print(detect_loop(m).val)   