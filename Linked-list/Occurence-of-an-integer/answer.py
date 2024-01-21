class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def count(self, head, search_for):
        total = 0
        if head.data == search_for:
            total += 1
        current_node = head
        while current_node.next != None:
            current_node = current_node.next
            if current_node.data == search_for:
                total += 1
        return total


head = Node(1)

link1 = Node(2)

link2 = Node(2)

link3 = Node(1)

link4 = Node(1)

head.next = link1
link1.next = link2
link2.next = link3
link3.next = link4

solution = Solution()
print(solution.count(head,1))
    