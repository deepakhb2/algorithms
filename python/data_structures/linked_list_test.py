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
        pass

    def test_prepend(self):
        pass

    def test_traverse_to_index(self):
        pass

    def test_insert(self):
        pass

    def test_remove(self):
        pass

    def test_reverse(self):
        pass

    def test_values(self):
        self.assertEqual(self.list.values(), [10])

if __name__ == "__main__":
    unittest.main()
