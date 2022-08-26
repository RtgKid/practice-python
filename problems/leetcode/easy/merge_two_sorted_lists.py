# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1:
            return list2
        
        if not list2:
            return list1
        
        if list1.val <= list2.val:
            c = list1.next
            list1.next = list2
            list2 = list1
            list1 = c
    
        q = list2
        while list1:
            if not list2.next:
                list2.next = list1
                return q
            elif list1.val <= list2.next.val:
                c = list2.next
                d = list1.next
                list2.next = list1
                list1.next = c
                list2 = list1
                list1 = d
                
            else:
                list2 = list2.next
                
                    
        return q  
            