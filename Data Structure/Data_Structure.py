class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        return self.items


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        return self.items


class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = LinkedListNode(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        current = self.head
        previous = None
        while current and current.data != data:
            previous = current
            current = current.next
        if current is None:
            return False
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next
        return True

    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        return elements


class BinaryTreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = BinaryTreeNode(key)
        else:
            self._insert_rec(self.root, key)

    def _insert_rec(self, node, key):
        if key < node.value:
            if node.left is None:
                node.left = BinaryTreeNode(key)
            else:
                self._insert_rec(node.left, key)
        else:
            if node.right is None:
                node.right = BinaryTreeNode(key)
            else:
                self._insert_rec(node.right, key)

    def inorder(self):
        return self._traverse_inorder(self.root)

    def _traverse_inorder(self, node):
        return self._traverse_inorder(node.left) + [node.value] + self._traverse_inorder(node.right) if node else []

    def display(self):
        return self.inorder()


def display_menu():
    print("\nChoose a data structure to explore:")
    print("1. List")
    print("2. Tuple")
    print("3. Set")
    print("4. Dictionary")
    print("5. Stack")
    print("6. Queue")
    print("7. Linked List")
    print("8. Binary Tree")
    print("9. Exit")


def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            lst = []
            while True:
                operation = input("Add (a), Remove (r), Display (d), or Back (b): ")
                if operation == 'a':
                    item = input("Enter item to add: ")
                    lst.append(item)
                elif operation == 'r':
                    item = input("Enter item to remove: ")
                    lst.remove(item) if item in lst else print("Item not found.")
                elif operation == 'd':
                    print("List:", lst)
                elif operation == 'b':
                    break

        elif choice == '2':
            tup = ()
            print("Create a tuple by entering elements separated by spaces.")
            elements = input("Enter elements: ").split()
            tup = tuple(elements)
            print("Tuple:", tup)

        elif choice == '3':
            st = set()
            while True:
                operation = input("Add (a), Remove (r), Display (d), or Back (b): ")
                if operation == 'a':
                    item = input("Enter item to add: ")
                    st.add(item)
                elif operation == 'r':
                    item = input("Enter item to remove: ")
                    st.discard(item)
                elif operation == 'd':
                    print("Set:", st)
                elif operation == 'b':
                    break

        elif choice == '4':
            dct = {}
            while True:
                operation = input("Add (a), Remove (r), Retrieve (r), Display (d), or Back (b): ")
                if operation == 'a':
                    key = input("Enter key: ")
                    value = input("Enter value: ")
                    dct[key] = value
                elif operation == 'r':
                    key = input("Enter key to remove: ")
                    dct.pop(key, None)
                elif operation == 'r':
                    key = input("Enter key to retrieve: ")
                    print("Value:", dct.get(key, "Key not found."))
                elif operation == 'd':
                    print("Dictionary:", dct)
                elif operation == 'b':
                    break

        elif choice == '5':
            stack = Stack()
            while True:
                operation = input("Push (p), Pop (o), Display (d), or Back (b): ")
                if operation == 'p':
                    item = input("Enter item to push: ")
                    stack.push(item)
                elif operation == 'o':
                    popped_item = stack.pop()
                    print("Popped item:", popped_item if popped_item else "Stack is empty.")
                elif operation == 'd':
                    print("Stack:", stack.display())
                elif operation == 'b':
                    break

        elif choice == '6':
            queue = Queue()
            while True:
                operation = input("Enqueue (e), Dequeue (d), Display (d), or Back (b): ")
                if operation == 'e':
                    item = input("Enter item to enqueue: ")
                    queue.enqueue(item)
                elif operation == 'd':
                    dequeued_item = queue.dequeue()
                    print("Dequeued item:", dequeued_item if dequeued_item else "Queue is empty.")
                elif operation == 'd':
                    print("Queue:", queue.display())
                elif operation == 'b':
                    break

        elif choice == '7':
            linked_list = LinkedList()
            while True:
                operation = input("Insert (i), Delete (d), Display (d), or Back (b): ")
                if operation == 'i':
                    item = input("Enter item to insert: ")
                    linked_list.insert(item)
                elif operation == 'd':
                    item = input("Enter item to delete: ")
                    result = linked_list.delete(item)
                    print("Deleted:", result)
                elif operation == 'd':
                    print("Linked List:", linked_list.display())
                elif operation == 'b':
                    break

        elif choice == '8':
            binary_tree = BinaryTree()
            while True:
                operation = input("Insert (i), Display (d), or Back (b): ")
                if operation == 'i':
                    item = int(input("Enter item to insert: "))
                    binary_tree.insert(item)
                elif operation == 'd':
                    print("Binary Tree Inorder:", binary_tree.display())
                elif operation == 'b':
                    break

        elif choice == '9':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()