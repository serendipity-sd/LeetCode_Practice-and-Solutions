"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        if (head == None or head.next == None): return head;
        
        h_odd = head;
        h_even = head.next;
        odd = h_odd;
        even = h_even;
        
        while (even != None):
            if(even.next != None):
                odd.next = even.next;
            else:
                odd.next = h_even;
                return h_odd
            
            odd = odd.next
            even.next = odd.next
            even = even.next
            
        odd.next = h_even;
        
        return h_odd;
        
        
