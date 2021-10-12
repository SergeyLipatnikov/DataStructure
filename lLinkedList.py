class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        return [] # здесь будет ваш код

    def delete(self, val, all=False):
        if all:
            return True
        else:
            node = self.head
            while node is not None:
                if node.next.value == val:
                    print("Check", node.next.value)
                    node.next = node.next.next
                    break
                node = node.next

    def clean(self):
        pass # здесь будет ваш код


    def len(self):
        return 0 # здесь будет ваш код

    def insert(self, afterNode, newNode):
        pass # здесь будет ваш код

n1 = Node(12)
n2 = Node(55)
s_list = LinkedList()
s_list.add_in_tail(n1)
s_list.add_in_tail(n2)
s_list.add_in_tail(Node(128))
# s_list.add_in_tail(Node(128))
# s_list.add_in_tail(Node(128))
# s_list.add_in_tail(Node(128))
# s_list.add_in_tail(Node(128))
# s_list.print_all_nodes()
s_list.delete(12)
s_list.print_all_nodes()