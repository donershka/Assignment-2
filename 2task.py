class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def find_middle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


n = int(input())
values = list(map(int, input().split()))

head = ListNode(values[0])
current = head

for i in range(1, n):
    current.next = ListNode(values[i])
    current = current.next

middle = find_middle(head)
print(middle.val)