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
        self.length += 1

    def prepend(self, value):
        list = { 'value': value, 'next': self.head }
        self.head = list
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

my_linked_list = LinkedList(10)
my_linked_list.append(5)
my_linked_list.append(16)
my_linked_list.prepend(9)
my_linked_list.insert(8, 1)
my_linked_list.remove(1)
print(my_linked_list)