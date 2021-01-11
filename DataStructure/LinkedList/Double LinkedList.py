class Node(object):
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DList(object):
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None, self.head)
        self.head.next = self.tail
        self.size = 0

    def list_size(self):
        return self.size

    def is_empty(self):
        if self.size != 0:
            return False
        else:
            return True

    def append_left(self, value):
        if self.is_empty():
            self.head = Node(value)
            self.tail = self.head
        else:
            cur = self.head
            self.head = Node(value, None, self.head)
            cur.prev = self.head
        self.size += 1

    def append(self, value):
        if self.is_empty():
            self.head = Node(value)
            self.tail = self.head
        else:
            tmp = self.tail
            self.tail = Node(value, tmp)
            tmp.next = self.tail
        self.size += 1

    def insert(self, value, idx):
        if idx > self.list_size() or idx < 0:
            print("Wrong Index")
            return
        elif self.is_empty():
            self.head = Node(value)
            self.tail = self.head
        elif idx == 0:
            cur = self.head
            self.head = Node(value, None, self.head)
            cur.prev = self.head
        elif idx == self.size:
            cur = self.tail
            self.tail = Node(value, cur)
            cur.next = self.tail
        else:
            if idx >= self.size // 2:
                cur = self.head
                i = 1
                while i < idx:
                    cur = cur.next
                    i += 1
                # 왼쪽의 cur.next 는 cur 노드의 next 부분(cur 노드)
                # 오른쪽의 cur.next 는 cur.next 가 가리키는 노드(cur.next 노드)
                cur.next = Node(value, cur, cur.next)
            else:
                cur = self.tail
                i = self.size
                while i > idx:
                    cur = cur.prev
                    i -= 1
                cur.next = Node(value, cur, cur.next)
        # if 문에서 return 을 걸어야 idx 가 잘못 들어왔을 때 size 를 증가시키지 않는다.
        self.size += 1

    def delete(self, idx):
        if idx > self.list_size() or idx < 0:
            print("Wrong Index")
            return
        elif self.is_empty():
            print("list is empty")
            return
        elif idx == 0:
            self.head = self.head.next
        else:
            cur = self.head
            i = 0
            while i + 1 < idx:
                cur = cur.next
                i += 1
            cur.next = cur.next.next
        self.size -= 1

    def print_list(self):
        cur = self.head
        while cur:
            if cur.next is not None:
                print(cur.data, '<=> ', end='')
            else:
                print(cur.data)
            cur = cur.next


mylist = DList()
mylist.append('A')
mylist.print_list()
mylist.append('B')
mylist.print_list()
mylist.append('C')
mylist.print_list()
mylist.insert('D', 1)
mylist.print_list()
mylist.append_left('E')
mylist.print_list()
print(mylist.list_size())
mylist.delete(0)
mylist.print_list()
mylist.delete(3)
mylist.print_list()
mylist.delete(0)
mylist.print_list()
mylist.append_left('A')
mylist.print_list()

# 참고
# https://underflow101.tistory.com/4
