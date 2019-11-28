from binarytree import Node


class BST:

    def __init__(self, node=None):
        self.root = node

    def binary_insert(self, num, node=None):
        if node is None:
            if self.root is None:
                self.root = Node(num)
                return
            else:
                node = self.root
        if node.value >= num:
            if node.left is not None:
                self.binary_insert(num, node.left)
            else:
                node.left = Node(num)
        if node.value < num:
            if node.right is not None:
                self.binary_insert(num, node.right)
            else:
                node.right = Node(num)

    def inorder(self, ans_list, node=None):
        if node is None:
            node = self.root
        if node.left is not None:
            ans_list = self.inorder(ans_list, node.left)
        ans_list += [node.value]
        if node.right is not None:
            ans_list = self.inorder(ans_list, node.right)

        return ans_list

    def preorder(self, ans_list, node=None):
        if node is None:
            node = self.root
        ans_list += [node.value]
        if node.left is not None:
            ans_list = self.preorder(ans_list, node.left)
        if node.right is not None:
            ans_list = self.preorder(ans_list, node.right)

        return ans_list

    def postorder(self, ans_list, node=None):
        if node is None:
            node = self.root
        if node.left is not None:
            ans_list = self.postorder(ans_list, node.left)
        if node.right is not None:
            ans_list = self.postorder(ans_list, node.right)
        ans_list += [node.value]
        return ans_list

    def get_output(self):
        output = self.root.__str__()
        output += '\n\nPREORDER\t' + str(self.preorder([]))
        output += '\nINORDER\t\t' + str(self.inorder([]))
        output += '\nPOSTORDER\t' + str(self.postorder([]))
        return output


bst = BST()
bst.binary_insert(10)
bst.binary_insert(7)
bst.binary_insert(11)
bst.binary_insert(6)
bst.binary_insert(8)
bst.binary_insert(20)
bst.binary_insert(1)
bst.binary_insert(9)
bst.binary_insert(14)
bst.binary_insert(22)

print(bst.root)
