#A class to store a binary tree node
class TNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# Recursive function to check if a given binary tree is height-balanced or not
def is_Balanced(root,isBalanced=True):

    # base case: tree is empty or not balanced
    if root is None or not isBalanced:
        return 0, isBalanced

    # get the height of the left subtree
    left_height, isBalanced = is_Balanced(root.left, isBalanced)

    # get the height of the right subtree
    right_height, isBalanced = is_Balanced(root.right, isBalanced)

    # tree is unbalanced if the absolute difference between the height of
    # its left and right subtree is more than 1
    if abs(left_height - right_height) >1 :
        isBalanced = False

    # return height of subtree rooted at the current node
    return max(left_height, right_height) + 1, isBalanced


if __name__ == '__main__':

    ''' Construct the following tree
                  A
                /   \
              B       C
             / \       \
            D   E       F
    '''

    d = TNode('D',None,None)
    f = TNode('F',None,None)
    e = TNode('E', None, f)
    c = TNode('C',None,None)
    b = TNode('B', c, d)
    root = TNode('A',b,e)


    if is_Balanced(root):
        print('Binary tree is balanced')
    else:
        print('Binary tree is not balanced')
