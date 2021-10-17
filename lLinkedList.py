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
        Found_nodes = []
        node = self.head
        while node is not None:
            if node.value == val:
                Found_nodes.append(node)
            node = node.next
        return Found_nodes

    def delete(self, val, all):
        node = self.head
        if not node:
            return
        elif node.value == val:
            node.value = node.next.value
            node.next = node.next.next 
        if all:
            while node is not None:
                if (node.next != None) and (node.next.value == val):
                    node.next = node.next.next
                    while node is not None:
                        if (node.next != None) and (node.next.value == val):
                            node.next = node.next.next
                        else:
                            if node.next is None:
                                self.tail.next = node
                                self.tail = node
                            break
                node = node.next
        else:
            while node is not None:
                if (node.next != None) and node.next.value == val:
                    node.next = node.next.next
                    if node.next is None:
                        self.tail.next = node
                        self.tail = node
                    break
                node = node.next

    def clean(self):
        self.head = None
        self.tail = None


    def len(self):
        node = self.head
        count = 0
        while node is not None:
            count += 1
            node = node.next
        return count

    def insert(self, afterNode, newNode):
        if afterNode is None:
            first_node = self.head
            self.head = Node(newNode)
            self.head.next = first_node
        else:
            node = self.find(afterNode)
            if node.next is None:
                self.tail.next = Node(newNode)
                self.tail = Node(newNode)
            else:
                second_node = Node(newNode)
                second_node.next = node.next
                node.next = second_node

