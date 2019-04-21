#!/usr/bin/python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeNode:
    def __init__(self, data=None, l_child=None, r_child=None):
        self.data = data
        self.left_child = l_child
        self.right_child = r_child
        self.parent = None


class TreeOrders:
    def __init__(self):
        self.root = None
        self.n = None
        self.key = None
        self.left = None
        self.right = None
        self.result = None
        self.build_array = None

    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        self.build_array = [None] * self.n
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

            new_node = self.create_node(self.key[i], self.left[i], self.right[i])
            self.build_tree(i, new_node)

    def create_node(self, key, l_ind, r_ind):
        if l_ind == -1:
            l_ind = None
        if r_ind == -1:
            r_ind = None
        temp_node = TreeNode(key, l_ind, r_ind)
        return temp_node

    def build_tree(self, cur_ind, new_node):
        if cur_ind == 0:
            self.root = new_node
            self.build_array[cur_ind] = new_node
        elif 0 < cur_ind < self.n:
            is_a_child_of = self.build_array[cur_ind]
            if is_a_child_of is None:
                self.build_array[cur_ind] = new_node
            else:
                my_parent = self.build_array[is_a_child_of]
                if my_parent.left_child == cur_ind:
                    my_parent.left_child = new_node
                elif my_parent.right_child == cur_ind:
                    my_parent.right_child = new_node

                new_node.parent = my_parent
                self.build_array[cur_ind] = new_node

        if new_node.left_child is not None:
            if new_node.left_child < cur_ind:
                my_left_child = self.build_array[new_node.left_child]
                new_node.left_child = my_left_child
            else:
                self.build_array[new_node.left_child] = cur_ind

        if new_node.right_child is not None:
            if new_node.right_child < cur_ind:
                my_right_child = self.build_array[new_node.right_child]
                new_node.right_child = my_right_child
            else:
                self.build_array[new_node.right_child] = cur_ind


def is_bst(root, min_key=-sys.maxsize-1, max_key=sys.maxsize):
    if root is None:
        return True

    if (min_key < root.data < max_key and
        is_bst(root.left_child, min_key, root.data) and
        is_bst(root.right_child, root.data, max_key)):
        return True
    else:
        return False


def main():
    tree = TreeOrders()
    tree.read()

    if is_bst(tree.root):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()

