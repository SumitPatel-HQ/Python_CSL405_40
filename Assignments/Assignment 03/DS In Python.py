# Linked List Rotation Implementation in Python


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Function to print the linked list
def print_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next

# Function to rotate the linked list by k places
def rotate_right(head, k):
    if not head or not head.next or k == 0:
        return head

    # length of the linked list
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1

    # Adjust k to avoid unnecessary full rotations
    k = k % length
    if k == 0:
        return head

    # Find the new tail (length - k - 1 position)
    new_tail = head
    for _ in range(length - k - 1):
        new_tail = new_tail.next

    # Update head and tail pointers
    new_head = new_tail.next
    new_tail.next = None
    tail.next = head  

    return new_head

# Function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# User Input
values = list(map(int, input("Enter linked list elements separated by spaces: ").split()))
k = int(input("Enter the number of places to rotate: "))

# Creating the linked list
head = create_linked_list(values)
print("\nOriginal Linked List:")
print_list(head)

# Rotating the list
rotated_head = rotate_right(head, k)
print("\nRotated Linked List:")
print_list(rotated_head)
