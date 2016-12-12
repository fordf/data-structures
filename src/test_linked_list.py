"""Testing module for linked_list module."""
from linked_list import LinkedList
from linked_list import Node


LINKED_LIST = LinkedList()
LINKED_LIST.push(3)
LINKED_LIST.push("boomshakalaka")
LINKED_LIST.push(4)


def test_linked_list_init():
    """Test LinkedList class init method."""
    lst = LinkedList()
    assert lst.head is None


def test_node_init():
    """Test Node class init method."""
    node1 = Node(1, None)
    node2 = Node(2, node1)
    assert node1.val == 1
    assert node1.next is None
    assert node2.val == 2
    assert node2.next is node1


def test_linked_list_push():
    """Test linked list push method."""
    assert LINKED_LIST.head.val == 4
    assert LINKED_LIST.head.next.val == "boomshakalaka"
    assert LINKED_LIST.head.next.next.val == 3
    assert LINKED_LIST.head.next.next.next is None


def test_linked_list_size():
    """Test linked list size method."""
    assert LINKED_LIST.size() == 3