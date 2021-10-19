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
        prevNode = None
        node = self.head
        if node is not None:
            if node.value == val:
                self.head = node.next
                if not all:
                    return
        if all:
            while node is not None:
                _del = 0
                if node.value == val:
                    if prevNode is not None:
                        prevNode.next = node.next
                        _del = 1
                    else:
                        self.head = node.next
                        _del = 1
                if _del == 0:
                    prevNode = node
                    node = node.next
                else:
                    node = node.next
        else:
            while node is not None:
                if node.value == val:
                    break
                lastnode = node
                node = node.next
        if node == None:
            self.tail = prevNode
            return
        lastnode.next = node.next
        node = None

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
                self.add_in_tail(Node(newNode))
            else:
                second_node = Node(newNode)
                second_node.next = node.next
                node.next = second_node
