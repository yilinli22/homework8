from containers.BinaryTree import BinaryTree, Node
from containers.BST import BST


class AVLTree(BST):

    def __init__(self, xs=None):
        '''
        FIXME:
        Implement this function.
        '''
        super().__init__(xs)
        # if xs is not None:
        #     self.insert_list(xs)

    def balance_factor(self):
        '''
        Returns the balance factor of a tree.
        '''
        return AVLTree._balance_factor(self.root)

    @staticmethod
    def _balance_factor(node):
        '''
        Returns the balance factor of a node.
        '''
        if node is None:
            return 0
        return BinaryTree._height(node.left) - BinaryTree._height(node.right)

    def is_avl_satisfied(self):

        return AVLTree._is_avl_satisfied(self.root)

    @staticmethod
    def _is_avl_satisfied(node):
        '''
        FIXME:
        Implement this function.
        '''
        if AVLTree._balance_factor(node) not in [-1, 0, 1]:
            return False
        if node is None:
            return True
        else:
            return (AVLTree._is_avl_satisfied(node.left)) and\
                   (AVLTree._is_avl_satisfied(node.right))

    @staticmethod
    def _left_rotate(node):
        '''
        FIXME:
        Implement this function.
        '''
        if not node or not node.right:
            return node
        newRoot = Node(node.right.value)
        newRoot.right = node.right.right
        newRoot.left = Node(node.value)
        newRoot.left.left = node.left
        newRoot.left.right = node.right.left
        return newRoot

    @staticmethod
    def _right_rotate(node):
        '''
        FIXME:
        Implement this function.
        '''
        if not node or not node.right:
            return node
        newRoot = Node(node.left.value)
        newRoot.left = node.left.left
        newRoot.right = Node(node.value)
        newRoot.right.right = node.right
        newRoot.right.left = node.left.right
        return newRoot

    def insert(self, value):
        #print("insert=", value)
        if self.root is None:
            self.root = Node(value)
        if value == self.root.value:
            return
        self.root = AVLTree._insert(self.root, value)

    @staticmethod
    def _insert(node, value):
        #print("_insert=", value)
        if AVLTree._is_avl_satisfied(node):
            pass
        if value > node.value:
            if not node.right:
                node.right = Node(value)
            else:
                return AVLTree._insert(node.right, value)
        elif value < node.value:
            if not node.left:
                node.left = Node(value)
            else:
                return AVLTree._insert(node.left, value)
        else:
            node.right = AVLTree._rebalance(node.right)
            node.left = AVLTree._rebalance(node.left)
            node = AVLTree._rebalance(node)
        return node

    @staticmethod
    def _rebalance(node):
        '''
        There are no test cases for the rebalance function,
        so you do not technically have to implement it.
        But both the insert function needs the rebalancing code,
        so I recommend including that code here.
        '''
        if not node:
            return
        if AVLTree._balance_factor(node) < 0:
            if AVLTree._balance_factor(node.right) > 0:
                node.right = AVLTree._right_rotate(node.right)
                node = AVLTree._left_rotate(node)
            else:
                node = AVLTree._left_rotate(node)
        elif AVLTree._balance_factor(node) > 0:
            if AVLTree._balance_factor(node.left) < 0:
                node.left = AVLTree._left_rotate(node.left)
                node = AVLTree._right_rotate(node)
            else:
                node = AVLTree._right_rotate(node)
        return node
