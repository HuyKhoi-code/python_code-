class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class Linked:
    def __init__(self):
        self.headval = None

    def print_list(self):
        printval = self.headval
        while printval is not None:
            print(printval.val)
            printval = printval.next

    def add_val_Start(self, newdata):
        new_node = Node(newdata)
        new_node.next = self.headval
        self.headval = new_node

    def add_val_End(self, newdata):
        new_node = Node(newdata)
        if self.headval is None:
            self.headval = new_node
            return
        curr = self.headval
        while (curr.next):
            curr = curr.next
        curr.next = new_node
    
    def add_val_between (self, middle, newdata):
        new_node = Node(newdata)
        if middle is None:
            print ("can't find middle node")
            return 
        new_node.next = middle.next
        middle.next = new_node

list = Linked()
list.headval = Node("monday")
""" val2 = Node("tuesday")
n3 = Node("wednesday")
list.headval.next = val2
val2.next = n3 """
list.add_val_Start("sunday")
list.add_val_End("thursday")
list.add_val_End("saturday")
middle = list.headval.next.next.next.next
list.add_val_between(middle,"friday")

list.print_list()
