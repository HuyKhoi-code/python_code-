class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_end(self, newval):
        new_node = Node(newval)
        if self.head is None:
            new_node = self.head
            return 
        curr = self.head
        while (curr.next):
            curr = curr.next
        curr.next = new_node

    def swap_node(self, val1, val2):
        prev1 = None
        prev2 = None
        node1 = self.head
        node2 = self.head

        if (self.head is None):
            return 

        if (val1 == val2):
            return 

        # search for val1 and val2 in list 
        while (node1 != None and node1.val != val1):
            prev1 = node1
            node1 = node1.next

        while (node2 != None and node2.val != val2):
            prev2 = node2
            node2 = node2.next

        # swap val1 and val2
        if (node1 != None and node2 != None):
            if (prev1 != None):
                prev1.next = node2
            else:
                self.head = node2
            if (prev2 != None):
                prev2.next = node1
            else:
                self.head = node1
            
            node1.next, node2.next = node2.next, node1.next
    
    def print_list(self):
        curr = self.head
        while (curr != None):
            print (curr.val)
            curr = curr.next

num_list = LinkedList()
num_list.head = Node(1)
num_list.add_end(2)
num_list.add_end(3)
num_list.add_end(4)
num_list.add_end(5)
num_list.print_list()
num_list.swap_node(2,4)
num_list.print_list()





            
    
    