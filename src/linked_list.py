"""Module defining linked list."""


class LinkedList(object):
    """Classic linked list data structure."""

    def __init__(self, head=None):
        """Initialize LinkedList instance."""
        self.head = head

    def push(self, val):
        """Insert val at the head of linked list."""
        self.head = Node(val, self.head)

    def pop(self):
        """Pop the first value off of the head and return it."""
        first = self.head
        self.head = self.head.next
        return first

    def size(self):
        """Return length of linked list."""
        length = 0
        curr = self.head
        while curr is not None:
            length += 1
            curr = curr.next
        return length


class Node(object):
    """Node class."""

    def __init__(self, val, next):
        """Initialize Node instance."""
        self.val = val
        self.next = next