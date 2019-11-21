class LinkedList():
    def __init__(self, value):
        self.head = { 'value': value, 'next': None }
        self.tail = self.head
        self.length = 1

    def __str__(self):
        return str(self.head)

    def append(self, value):
        new_node = { 'value': value, 'next': None }
        self.tail['next'] = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = { 'value': value, 'next': self.head }
        self.head = new_node
        self.length += 1

    def traverse_to_index(self, index):
        counter = 0
        current_node = self.head
        while(counter != index):
            current_node = current_node['next']
            counter += 1
        return current_node

    def insert(self, value, index):
        if(index >= self.length):
            self.append(value)
        new_node = { 'value': value, 'next': None }
        leader = self.traverse_to_index(index-1)
        holding_pointer = leader['next']
        leader['next'] = new_node
        new_node['next'] = holding_pointer
        self.length += 1

    def remove(self, index):
        leader = self.traverse_to_index(index-1)
        leader['next'] = leader['next']['next']
        self.length -= 1

    def values(self):
        values = []
        current_node = self.head
        counter = 0
        while(counter != self.length):
            values.append(current_node['value'])
            current_node = current_node['next']
            counter += 1
        return values

    def reverse(self):
        first = self.head
        self.tail = self.head
        second = first['next']

        while(second):
            temp = second['next']
            second['next'] = first
            first = second
            second = temp

        self.head['next'] = None
        self.head = first

my_linked_list = LinkedList(10)
my_linked_list.append(5)
my_linked_list.append(16)
my_linked_list.append(20)
my_linked_list.prepend(9)
my_linked_list.insert(8, 1)
my_linked_list.remove(1)
#print('List :')
#my_linked_list.print_list()
#print('Reverse:')
my_linked_list.reverse()
#my_linked_list.print_list()
