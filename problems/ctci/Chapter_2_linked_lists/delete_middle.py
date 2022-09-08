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

m = ListNode(2, ListNode(3, None))
p = ListNode(0, ListNode(2, m))

p.print()


def delete_middle(h:ListNode, m:ListNode) -> ListNode:
    while m.next:
        m.val = m.next.val
        if m.next.next:
            m = m.next
        else:
            m.next = None
    return h    


delete_middle(p, m).print()    

