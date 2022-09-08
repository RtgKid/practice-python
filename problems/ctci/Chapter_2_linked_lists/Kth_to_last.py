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


def kth_to_last(h : ListNode, k) -> ListNode:
    j = 0
    l = t = h

    while l.next:
        if j >= k:
            t = t.next
        else:
            j += 1
        l = l.next        
    return t     

m = ListNode(0, ListNode(2, ListNode(2, ListNode(3, None))))
m.print()

print(kth_to_last(m, 1).val)