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
                

def remove_deps(l : ListNode) -> ListNode:
    d = {}
    head = l
    d[head.val] = 1 
    while l.next:
        if l.next.val in d:
            if l.next.next:
                l.next = l.next.next
            else:
                l.next = None    
        else:
            d[l.next.val] = 1
            l = l.next    

    return head

m = ListNode(0, ListNode(2, ListNode(2, ListNode(3, None))))
m.print()
remove_deps(m).print()

n = ListNode(2, ListNode(2, ListNode(2, ListNode(3, None))))
remove_deps(n).print()
