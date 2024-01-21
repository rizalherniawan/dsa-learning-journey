class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        # length = 1
        # current = head
        start = head
        next_node = head
        # last = head
        # while last != None:
        #     last = last.next
        #     length += 1
        # while current != None:
        #     target = current.next
        #     while target != None and current.val == target.val:
        #         target = target.next
            
        #     current.next = target
        #     current = target.next
        while next_node != None:
            if next_node.val != head.val:
                head.next = next_node
                head = head.next
            next_node = next_node.next
        head.next = None
        Solution.print_itterate(self, start)

    
    def print_itterate(self, head):
        current_node = head
        while current_node != None:
            print(current_node.val)
            current_node = current_node.next

head = ListNode(1)
link1 = ListNode(1)
link2 = ListNode(1)
link3 = ListNode(2)
link4 = ListNode(3)
link5 = ListNode(4)
link6 = ListNode(4)


head.next = link1
link1.next = link2
link2.next = link3
link3.next = link4
link4.next = link5
link5.next = link6

soluttion = Solution()
soluttion.deleteDuplicates(head)

# soluttion.print_itterate(head)


        
        
        
