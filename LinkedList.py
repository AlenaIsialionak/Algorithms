class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

    def get_item(self):
        return self.item

    def set_item(self, new_item):
        self.item = new_item

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class LinkedList:
    def __init__(self):
        self.head = self.tail = None
        self._name = self.__class__.__name__
        self._size = 0

    def __iter__(self):
        current = self.head
        while current:
            yield current.item
            current = current.next
    def __str__(self):
        return f"{self._name}({','.join(map(str, self))})"

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def index(self, item):
        current, counter = self.head, 0

        while counter < self._size:
            if current.get_item() == item:
                return counter
            current = current.get_next()
            counter += 1

        if counter == self._size - 1:
            raise ValueError

    def add(self, value):
        node = Node(value)
        if self.head is None:
            self.tail = self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

        self._size += 1

    def append(self, value):
        node = Node(value)
        if self.tail is None:
            node.next = self.head
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self._size += 1

    def insert(self, item, position):
        if self._size == 0 or position <= 0:
            self.add(item)
        elif position > self._size - 1:
            self.append(item)
        else:
            node = Node(item)
            current, counter = self.head, 0
            previous = None

            while counter < self._size:
                if counter == position:
                    break
                previous = current
                current = current.get_next()
                counter += 1
            previous.next = node
            node.prev = previous
            node.next = current
            current.prev = node

            self._size += 1
    def __update_prev_and_next(self, prev, curr):
        if prev is None:
            self.head = curr.get_next()
        else:
            next_ = curr.get_next()
            if next_ is None:
                self.tail = prev
            prev.set_next(next_)

    def pop(self, position=None):
        if self._size == 0:
            raise IndexError(f"pop from empty list {self._name}")

        if position is not None and (position < 0 or position >= self._size):
            raise IndexError(f"pop index {position} is out of range")
        elif position is None:
            position = self._size - 1

        current, counter = self.head, 0
        previous = None

        while counter < self._size:
            if counter == position:
                break
            previous = current
            current = current.get_next()
            counter += 1

        self.__update_prev_and_next(previous, current)
        self._size -= 1

        return current.get_item()

    def remove(self, item):
        current = self.head
        previous, found = None, False
        counter = 0

        while counter < self._size:
            if current.get_item() == item:
                found = True
                break
            previous = current
            current = current.get_next()
            counter += 1

        if not found:
            raise ValueError(f"remove error: {item} not in {self._name}")
        else:
            self.__update_prev_and_next(previous, current)
            self._size -= 1

    def reverse_list1(self):
        current = self.head
        prev_element = None
        while current:
            next_elem = current.next
            current.next = prev_element
            prev_element = current
            current = next_elem
        self.head = prev_element

    def reverse_list2(self):
        current = self.tail
        reverse_list = []
        while current:
            reverse_list.append(current.item)
            current = current.prev

        return reverse_list

    @classmethod
    def from_iterable(cls, sort_list):
        linked_list = cls()
        for elem in sort_list:
            linked_list.append(elem)
        return linked_list


    # def __eq__(self, linked_list2):
    #     if self._size != len(linked_list2):
    #         return False
    #     if not isinstance(linked_list2, LinkedList):
    #         raise TypeError
    #     else:
    #         return self.__str__() == linked_list2.__str__()

    def __eq__(self, linked_list2):
        if self.head is None and linked_list2.head is None:
            return True
        if not isinstance(linked_list2, LinkedList):
            raise TypeError
        current1, current2 = self.head, linked_list2.head
        while current1:
            if current2 is None or current1.item != current2.item:
                return False
            current1, current2 = current1.next, current2.next
        if current2:
            return False
        else:
            return True

    def odd_even(self):
        if self.head is None or self.head.next is None:
            return self.head
        odd = self.head
        even = self.head.next
        even_head = even
        while odd and odd.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return

    def sort_list(self):
        current = self.head
        arr = []
        while current:
            arr.append(current.item)
            current = current.next
        arr.sort(reverse=True)
        print(arr)
        current = self.head
        while current:
            current.item = arr.pop()
            current = current.next

        return self.head



def reverse_k_node(head, k):
    current = head
    for _ in range(k):
        if not current:
            return head
        current = current.next

    prev = None
    current = head
    for _ in range(k):
        next_elem = current.next
        current.next = prev
        prev = current
        current = next_elem

    head.next = reverse_k_node(current, k)
    return




new_list = LinkedList()
for i in [3, 1, 2, 4]:
    new_list.add(i)
print(new_list)
# new_list.sort_list()
# print(new_list)
print(reverse_k_node(new_list.head, 1))
print(new_list)


