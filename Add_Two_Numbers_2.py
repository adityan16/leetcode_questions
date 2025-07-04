"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 
Constraints:
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        c=0
        temp,l=l1,l2
        while(temp!=None and l!=None):
            temp=temp.next
            l=l.next
        l={temp==None:l2}.get(True,l1)
        temp=l
        
        while (l1!=None or l2!=None):
            if l1==None:
                s = c+l2.val
                c=s//10
                l.val=(s%10)
                l={l.next==None:l}.get(True,l.next)
                l2=l2.next
            elif l2==None:
                s = c+l1.val
                c=s//10
                l.val=(s%10)
                l1=l1.next
                l={l.next==None:l}.get(True,l.next)
            else:
                s = c+l1.val+l2.val
                c=s//10
                l.val=(s%10)
                l2,l1=l2.next,l1.next
                l={l.next==None:l}.get(True,l.next)
        if c!=0:
            new_node=ListNode(1)
            l.next=new_node
        return temp