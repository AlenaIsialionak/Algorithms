class Entry:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
    def __repr__(self):
        return str(self.priority)

# implementation of the methods enqueue() and swim()
class PQ:

    def __init__(self, size):
        self.size = size
        self.storage = [None] * (size + 1) # узлы хранятся в ячейках от storage[1] до storage[size], а storage[0] не используется
        self.N = 0

    def less(self, i, j): # проверяет, что storage[i] имеет меньший приоритет, чем storage[j]
        return self.storage[i].priority < self.storage[j].priority # i-parant, j - child

    def swap(self, i, j): # меняет местами i-й и j-й узел
        self.storage[i], self.storage[j] = self.storage[j], self.storage[i]

    def enqueue(self, v, p): # чтобы добавить элемпент в кучу, надо разместить его в первой свободной ячейке массива, а затtм позволить ему всплыть
        if self.N == self.size:
            raise RuntimeError ('Priority Queue is Full!')

        self.N += 1
        self.storage[self.N] = Entry(v, p)
        self.swim(self.N)

    def swim(self, child): # swim() перестраивает массив storage, возвращая куче пирамидальность.
        while child > 1 and self.less(child // 2, child): # родительский узел для storage[child] находится в storage[child//2]
            self.swap(child, child//2) # меняем местами storage[child] and storage[child//2]
            child = child//2 # если надо узел продолжит всплывать, и теперь child равен индексу родителя

     # количество обменов не может превышать log2N, where N - общее число ячеек в двочной куче.

    def dequeue(self):
        if self.N == 0:
            raise RuntimeError('Priority Queue is empty!')

        max_entry = self.storage[1] # запомним ячейку на вершине кучм
        self.storage[1] = self.storage[self.N] # переставим на вершину последний (самый правый в самом нижнем  уровне) элемент, а его место освободим
        self.storage[self.N] = None
        self.N -= 1  # уменьшим количество узлов
        self.sink(1) # и запусим метод sink() для storage[1]
        return max_entry.value # вернем значение элемента, снятого с вершины кучи

    def sink(self, parent):
        while 2*parent <= self.N: # проверка продолжается, пока у узла есть хотя бы левый потомок
            child = 2*parent
            if child < self.N and self.less(child, child + 1): # если правый потомок существует и приоритет левого потомка меньше нам нужен правый потомок
                child += 1
            if not self.less(parent, child): # если приоритет родителя не меньше максимального приоритета потомков, пирамидальность восстановлена
                break

            self.swap(child, parent) # если нет, поменяем местами родителя и потомка и продолжим топить наш узел уде с нового места
            parent = child



h = PQ(10)
for (a, b) in [('a', 1), ('b', 3), ('c', 9), ('d', 4), ('f', 8), ('h', 7)]:
    h.enqueue(a, b)

print(h.storage)
