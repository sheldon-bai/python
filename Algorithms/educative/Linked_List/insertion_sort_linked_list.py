from linked_list_node import *
from linked_list import *

def insert_current(dummy_head, node):
    if dummy_head.next == None:
        dummy_head.next = node

        return dummy_head

    curr = dummy_head.next
    pre = dummy_head

    while curr:
        if node.data <= curr.data:
            pre.next = node
            node.next = curr

            return dummy_head
        else:
            pre = curr
            curr = curr.next

    pre.next = node

    return dummy_head

def insertion_sort(head):
    #TODO: Write - Your - Code
    if not head or not head.next:
        return head

    dummy_head = LinkedListNode(0)
    sorted_head = LinkedListNode(0)


    while head:
        print('head: ', head.data)
        dummy_head.next = head.next
        curr = head
        head = head.next
        curr.next = None
        sorted_head = insert_current(sorted_head, curr)
        
    return sorted_head.next

def main():
    v_list = [[29, 23, 82, 11, 4, 3, 21], [59, 7, -3, 21, 14, 30, 120]]
    for i in range(len(v_list)):
        obj1 = LinkedList()
        obj1.create_linked_list(v_list[i])

        print(str(i+1) + ". Unsorted list:\t", end="")
        print(obj1)

        # Reversing the created linked list
        obj2 = LinkedList()
        obj2.head = insertion_sort(obj1.head)
        print("   Sorted list:\t\t", end="")

        # Display Reversed List
        print(obj2)
        print("-"*100)

if __name__ == '__main__':
    main()