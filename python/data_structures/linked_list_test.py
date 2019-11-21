import unittest
from linked_list import LinkedList

class LinkedListTest(unittest.TestCase):

    def setUp(self):
        self.list = LinkedList(10)

    def test_init(self):
        head = self.list.head
        tail = self.list.tail
        self.assertEqual(head['value'], 10)
        self.assertEqual(tail['value'], 10)

    def test_append(self):
        self.list.append(11)
        self.assertEqual(self.list.tail['value'], 11)

    def test_prepend(self):
        self.list.prepend(9)
        self.assertEqual(self.list.head['value'], 9)

    def test_traverse_to_index(self):
        self.list.append(11)
        self.list.append(12)
        node = self.list.traverse_to_index(1)
        self.assertEqual(node['value'], 11)

    def test_insert(self):
        self.list.append(11)
        self.list.append(12)
        self.list.insert(11.5, 2)
        node = self.list.traverse_to_index(2)
        self.assertEqual(node['value'], 11.5)

    def test_remove(self):
        self.list.append(11)
        self.list.remove(1)
        self.assertEqual(self.list.tail['value'], 10)

    def test_values(self):
        self.assertEqual(self.list.values(), [10])

    def test_reverse(self):
        self.list.append(11)
        self.list.append(12)
        self.list.insert(11.5, 2)
        self.list.reverse()
        self.assertEqual(self.list.values(), [12, 11.5, 11, 10])

if __name__ == "__main__":
    unittest.main()
