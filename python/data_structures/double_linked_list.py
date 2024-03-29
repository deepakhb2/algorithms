class DoubleLinkedList:
    def __init__(self, value):
        self.head = { 'value': value, 'next': None, 'previous': None }
        self.tail = self.head
        self.length = 1

    def __str__(self):
        return str(self.head)

    def append(self, value):
        new_node = { 'value': value, 'next': None, 'previous': None }
        new_node['previous'] = self.tail
        self.tail['next'] = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = { 'value': value, 'next': None, 'previous': None }
        new_node['next'] = self.head
        self.head['previous'] = new_node
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
        new_node = { 'value': value, 'next': None, 'previous': None }
        leader = self.traverse_to_index(index-1)
        holding_pointer = leader['next']
        leader['next'] = new_node
        new_node['previous'] = leader
        new_node['next'] = holding_pointer
        holding_pointer['previous'] = new_node
        self.length += 1

    def remove(self, index):
        leader = self.traverse_to_index(index-1)
        leader['next']['next']['previous'] = leader
        leader['next'] = leader['next']['next']
        self.length -= 1

    def reverse(self):
        first = self.head
        self.tail = self.head
        second = first['next']

        while(second):
            temp = second['next']
            second['next'] = first
            first['previous'] = second
            first = second
            second = temp

        self.head['next'] = None
        self.head = first

    def print_list(self):
        current_node = self.head
        counter = 0
        while(counter != self.length):
            print(current_node['value'])
            current_node = current_node['next']
            counter += 1

my_linked_list = DoubleLinkedList(10)
my_linked_list.append(5)
my_linked_list.append(16)
my_linked_list.prepend(9)
my_linked_list.insert(8, 1)
my_linked_list.remove(1)
print('List :')
my_linked_list.print_list()
print('Reverse:')
my_linked_list.reverse()
my_linked_list.print_list()
