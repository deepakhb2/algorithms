class LinkedList():
    def __init__(self, value):
        self.head = { 'value': value, 'next': None }
        self.tail = self.head
        self.length = 1

    def __str__(self):
        return str(self.head)

    def append(self, value):
        list = { 'value': value, 'next': None }
        self.tail['next'] = list

my_linked_list = LinkedList(10);
my_linked_list.append(5);
my_linked_list.append(16);
print(my_linked_list)
