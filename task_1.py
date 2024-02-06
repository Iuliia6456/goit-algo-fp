class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def insertion_sort(self):
        current = self.head
        while current is not None:
            temp = current.next
            while temp is not None:
                if current.data > temp.data:
                    current.data, temp.data = temp.data, current.data
                temp = temp.next
            current = current.next

    def mergeSortedLists(llist1, llist2):
        llist1.insertion_sort()
        llist2.insertion_sort()
        merged_list = LinkedList()

        current1, current2 = llist1.head, llist2.head

        while current1 is not None and current2 is not None:
            if current1.data < current2.data:
                merged_list.push(current1.data)
                current1 = current1.next
            else:
                merged_list.push(current2.data)
                current2 = current2.next

        while current1 is not None:
            merged_list.push(current1.data)
            current1 = current1.next

        while current2 is not None:
            merged_list.push(current2.data)
            current2 = current2.next

        merged_list.reverse()
        return merged_list

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ") 
            temp = temp.next
        print()

llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)

llist2 = LinkedList()
llist2.push(5)
llist2.push(10)
llist2.push(19)
llist2.push(47)

print(f"\nOriginal Linked List:")
llist.printList()
llist.reverse()
print(f"\nReversed Linked List:")
llist.printList()
llist.insertion_sort()
print(f"\nSorted Linked List:")
llist.printList()

merged_list = LinkedList.mergeSortedLists(llist, llist2)
print("\nMerged Linked List:")
merged_list.printList()
print()







        