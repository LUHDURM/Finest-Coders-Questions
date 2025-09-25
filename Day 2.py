class Node:
    def __init__(self, key):
        self.data = key
        self.next = None

class Solution:
    def reverseKGroup(self, head: Node, k: int) -> Node:
        if not head or k == 1:
            return head

        dummy = Node(0)
        dummy.next = head
        curr, prev, nex = dummy, dummy, dummy

  
        count = 0
        while curr.next:
            curr = curr.next
            count += 1

        while count >= k:
            curr = prev.next
            nex = curr.next
            for i in range(1, k):
                curr.next = nex.next
                nex.next = prev.next
                prev.next = nex
                nex = curr.next
            prev = curr
            count -= k

        return dummy.next


def printList(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")


if __name__ == "__main__":
   
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    k = 2
    sol = Solution()
    new_head = sol.reverseKGroup(head, k)
    printList(new_head)
