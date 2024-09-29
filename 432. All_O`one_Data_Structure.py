class LinkedListNode:
    """
    Custom doubly linked list node to store key and its count.
    """
    def __init__(self, key='', count=0, next_node=None, prev_node=None):
        """
        Initialize LinkedListNode with given key, count, next, and previous pointers.
        """
        self.key = key               # Key (string)
        self.count = count           # Count of occurrences
        self.next = next_node        # Next node in the linked list
        self.prev = prev_node        # Previous node in the linked list

class AllOne:
    """
    Class to store strings' count and retrieve strings with minimum and maximum counts.
    """
    def __init__(self):
        """
        Initialize AllOne data structure with a dummy head and tail.
        """
        # Create dummy head and tail nodes
        self.head = LinkedListNode()
        self.tail = LinkedListNode(count=float('inf'), prev_node=self.head)
        # Connect head and tail
        self.head.next = self.tail
        # Dictionary to store key and its corresponding node in the linked list
        self.key_node_map = {}

    def _swap_nodes(self, node1, node2, node3, node4):
        """
        Swap nodes in the linked list.
        """
        # Adjust pointers to swap nodes
        node1.next = node3
        node3.prev, node3.next = node1, node2
        node2.prev, node2.next = node3, node4
        node4.prev = node2
        return node1, node3, node2, node4

    def _insert_new_node(self, key):
        """
        Insert a new node for a new key.
        """
        prev_node, curr_node = self.head, self.head.next
        new_node = LinkedListNode(key=key, count=1, next_node=curr_node, prev_node=prev_node)
        prev_node.next = new_node
        curr_node.prev = new_node
        self.key_node_map[key] = new_node

    def inc(self, key: str) -> None:
        """
        Increment the count of the string key by 1.
        """
        if key not in self.key_node_map:
            self._insert_new_node(key)
            return

        node = self.key_node_map[key]
        node.count += 1   

        while node.next.count < node.count: # Swap nodes if necessary
            node1, node2, node, node4 = self._swap_nodes(node.prev, node, node.next, node.next.next)
            self.key_node_map[key] = node

    def dec(self, key: str) -> None:
        """
        Decrement the count of the string key by 1.
        """
        node = self.key_node_map[key]
        node.count -= 1
        if node.count == 0: # If count becomes zero, remove the node
            prev_node, next_node = node.prev, node.next
            prev_node.next = next_node
            next_node.prev = prev_node
            del self.key_node_map[key]
            return
        while node.prev.count > node.count: # Swap nodes if necessary
            node1, node, node3, node4 = self._swap_nodes(node.prev.prev, node.prev, node, node.next)
            self.key_node_map[key] = node

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with the maximal count.
        """
        return self.tail.prev.key if self.tail.prev else ''

    def getMinKey(self) -> str:    
        """
        Returns one of the keys with the minimum count.
        """
        return self.head.next.key if self.head.next else ''
