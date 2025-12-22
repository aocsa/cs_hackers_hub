class Node():
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        self.height = 1


class BinaryTree:
    def __init__(self):
        self.root = None
        self.diff = 0

    def insert(self, data, root):
        if data > root.data:
            if root.right is None:
                root.right = Node(data)
                return root
            else:
                self.insert(data, root.right)
        else:
            if root.left is None:
                root.left = Node(data)
                return root
            else:
                self.insert(data, root.left)
        return root

    def rotate_to_right(self, root):
        left_subtree = root.left
        righ_of_left_subtree = left_subtree.right
        left_subtree.right = root
        root.left = righ_of_left_subtree

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        left_subtree.height = 1 + max(self.get_height(left_subtree.left), self.get_height(left_subtree.right))
        return left_subtree

    def rotate_to_left(self, root):
        right_subtree = root.right
        left_of_right_subtree = right_subtree.left
        right_subtree.left = root
        root.right = left_of_right_subtree

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        right_subtree.height = 1 + max(self.get_height(right_subtree.left), self.get_height(right_subtree.right))
        return right_subtree

    def insert_balanced(self,root , data):
        if root is None:
            return Node(data)
        else:
            if data > root.data:
                if root.right is None:
                    root.right = Node(data)
                else:
                    root.right = self.insert_balanced(root.right, data)
            else:
                if root.left is None:
                    root.left = Node(data)
                else:
                    root.left = self.insert_balanced(root.left, data)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        diff = self.get_balance(root)

        if diff < -1 and data > root.data: # Rotate left
            return self.rotate_to_left(root)
        elif diff < -1 and data < root.data:  # Rotate left and right
            root.right = self.rotate_to_left(root.right)
            return self.rotate_to_right(root)
        elif diff > 1 and data > root.data:  # Rotate right and left
            root.left = self.rotate_to_right(root.left)
            return self.rotate_to_left(root)
        elif diff > 1 and data < root.data: # Rotate right
            return self.rotate_to_right(root)
        return root

    def get_height(self, root):
        if root is not None:
            return 1 + max(self.get_height(root.left), self.get_height(root.right))
        else:
            return 0

    def get_balance(self, root):
        if root is not None:
            return self.get_height(root.left) - self.get_height(root.right)
        else:
            return 0

    def print_tree(self, root, level):
        if root is not None:
            self.print_tree(root.left, level + 1)
            for i in range (level):
                print('.....' ,end='')
            print(root.data)
            self.print_tree(root.right, level + 1)

    def in_order(self, root):
        if root is not None:
            self.in_order(root.left)
            print(root.data, end= '')
            self.in_order(root.right)

    def post_order(self, root):
        if root is not None:
            self.post_order(root.left)
            self.post_order(root.right)
            print(root.data, end=' ')

    def solve(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.data
        left = self.solve(root.left)
        right = self.solve(root.right)
        print('Calculating...', left, root.data, right)
        if root.data == '+':
            return left + right
        elif root.data == '*':
            return left * right
        elif root.data == '-':
            return left - right
        elif root.data == '/':
            return left / right

binary_tree = BinaryTree()
root_node = Node(5)
binary_tree.root = root_node
binary_tree.insert(3, binary_tree.root)
binary_tree.insert(7, binary_tree.root)
binary_tree.insert(2, binary_tree.root)
binary_tree.insert(4, binary_tree.root)
binary_tree.insert(6, binary_tree.root)
binary_tree.insert(8, binary_tree.root)
binary_tree.print_tree(root_node, 0)

print()

another_binary_tree = BinaryTree()
another_root_node = None
another_root_node = another_binary_tree.insert_balanced(another_root_node, 6)
another_root_node = another_binary_tree.insert_balanced(another_root_node, 2)
another_root_node = another_binary_tree.insert_balanced(another_root_node, 7)
another_root_node = another_binary_tree.insert_balanced(another_root_node, 5)
another_root_node = another_binary_tree.insert_balanced(another_root_node, 8)
another_root_node = another_binary_tree.insert_balanced(another_root_node, 4)
another_root_node = another_binary_tree.insert_balanced(another_root_node, 3)
another_binary_tree.print_tree(another_root_node, 0)

print()

expression_solver = BinaryTree()

expression_solver.root = Node('-')
expression_solver.root.left = Node('+')
expression_solver.root.right = Node('/')
expression_solver.root.left.left = Node(1)
expression_solver.root.left.right = Node('*')
expression_solver.root.left.right.left =  Node(3)
expression_solver.root.left.right.right =  Node(5)
expression_solver.root.right.left = Node(3)
expression_solver.root.right.right = Node(1)

expression_solver.print_tree(expression_solver.root, 0)
print()
expression_solver.post_order(expression_solver.root)
print()
print(expression_solver.solve(expression_solver.root))
