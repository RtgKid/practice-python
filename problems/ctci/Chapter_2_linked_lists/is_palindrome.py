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


m = ListNode(7, ListNode(1, ListNode(6, ListNode(1, ListNode(7, None)))))
n = ListNode(7, ListNode(1, ListNode(1, ListNode(7, None))))
q = ListNode(7, ListNode(1, ListNode(2, ListNode(7, None))))

def is_palindrome(h : ListNode) -> bool:
    s = []
    j = 0
    p = h
    while h.next:
        if h.next.next:
            h = h.next.next
            j += 2
        else:
            h = h.next
            j += 1
        s.append(p.val)    
        p = p.next

    if (j+ 1) % 2 != 0:
        p = p.next   
    while p:
        if p.val != s.pop():
            return False
        p = p.next    

    return True

print(is_palindrome(m))
print(is_palindrome(n))
print(is_palindrome(q))
