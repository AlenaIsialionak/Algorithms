class Node:
    def __init__(self, item = 0, next = None):
        self.next = None
        self.item = item

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def __str__(self):
        linked_list = []
        current = self.head
        while current:
            linked_list.append(current.item)
            current = current.next
        return f'{linked_list}'

    def add(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def append(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    @classmethod
    def from_iterable(cls, sort_list):
        linked_list = cls()
        for elem in sort_list:
            linked_list.append(elem)
        return linked_list


    def __len__(self):
        return self.size


    def list_print(self):
        current = self.head
        linked_list = []
        while current:
            linked_list.append(current.item)
            current = current.next

        return linked_list

    def add_two_numbers(self, l1, l2, result):
        remainder = 0
        cur = None
        cur1 = l1.head
        cur2 = l2.head
        while cur1 or cur2 or remainder:
            val1 = cur1.item if cur1 else 0
            val2 = cur2.item if cur1 else 0

            val = val1 + val2 + remainder
            digit = val % 10
            remainder = val // 10
            new_node = Node(digit)
            if cur is None:
                cur = result.head = new_node
            else:
                cur.next = new_node
                cur = cur.next
            cur1 = cur1.next if cur1 else None
            cur2 = cur2.next if cur2 else None

        return result

    def getIntersectionNode(self, listA, listB):
        lA, lB = listA.head, listB.head

        while lA != lB:
            lA = listB.head if not lA else lA.next
            lB = listA.head if not lB else lB.next
        return lA


    def deleteDuplicates1(self, list1, new_list):
        if not list1:
            return list1
        prev = None
        cur = list1.head
        while cur and cur.next:
            print(prev, cur.item, cur.next.item)
            if cur.item != prev:
                if new_list.head:
                    el.next = Node(cur.item)
                    el = el.next
                else:
                    new_Node = Node(cur.item)
                    new_list.head = new_Node
                    el = new_Node

            prev = cur.item
            cur = cur.next
        if cur.item != prev:
            if not new_list.head:
                new_list.head = Node(cur.item)
            else:
                el.next = Node(cur.item)


        return new_list


    def deleteDuplicates2(self, list1, new_list):
        if not list1:
            return list1
        prev = None
        cur = list1.head
        while cur and cur.next:
            print(prev, cur.item, cur.next.item)
            if cur.item != cur.next.item and cur.item != prev:
                if new_list.head:
                    el.next = Node(cur.item)
                    el = el.next

                else:
                    new_Node = Node(cur.item)
                    new_list.head = new_Node
                    el = new_Node

            prev = cur.item
            cur = cur.next
        if cur.item != prev:
            if not new_list.head:
                new_list.head = Node(cur.item)
            else:
                el.next = Node(cur.item)

        return new_list


    def removeNthFromEnd(self, list1, n: int, res):

        if not list1.head:
            return list1

        point1, point2 = list1.head, list1.head
        res.head = point2
        prev = None

        for num in range(n):

            point1 = point1.next

        if not point1:
            res = list1.head.next
            return res


        while point1:
            prev = point2
            point2 = point2.next
            point1 = point1.next



        prev.next = point2.next
        while point2:
            point2 = point2.next
        return res


    def swapPairs(self, list1, res):
        res.head = Node(0, list1.head)
        prev, cur = res.head, list1.head

        while cur.next and cur.next.next:
            # save ptrs
            nxtPair = cur.next.next
            second = cur.next

            # reverse this pair
            second.next = cur
            cur.next = nxtPair
            prev.next = second

            # update ptrs
            prev = cur
            cur = nxtPair
        res.head = res.head.next
        return res


    def swapNode(self, list2, res, n: int):

        point1 = list2.head
        point2 = list2.head
        res.head = point2

        for _ in range(n):
            el1 = point1.item
            point1 = point1.next

        while point1:
            point1 = point1.next
            point2 = point2.next

        el2 = point2.item
        point2.item = el1

        point1_2 = res.head
        point2_2 = point2.next

        while point2_2:
            point2_2 = point2_2.next
            point1_2 = point1_2.next
        point1_2.item = el2


        return res





list1 = LinkedList()
list2 = LinkedList()
result = LinkedList()
# for i in [4, 2, 1, 1, 9, 1, 1]:
#     list1.add(i)
# print(list1.list_print())
for i in [1, 2, 3, 4, 5]:
    list2.append(i)
print(list2)
# ans =LinkedList().add_two_numbers(list1, list2, result)
# print(ans.list_print())
# ans =LinkedList().getIntersectionNode(list1, list2)]
res = LinkedList()
# print(list2.removeNthFromEnd(list2, 1, res))
# print(list2.swapPairs(list2, res))
print(list2.swapNode(list2, res, 2))