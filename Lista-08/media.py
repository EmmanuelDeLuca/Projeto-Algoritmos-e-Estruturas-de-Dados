# class Solution:
#     def averageOfLevels(self, root: TreeNode) -> List[float]:
#         q, ans = [root], []
#         while len(q):
#             qlen, row = len(q), 0
#             for i in range(qlen):
#                 curr = q.pop(0)
#                 row += curr.val
#                 if curr.left: q.append(curr.left)
#                 if curr.right: q.append(curr.right)
#             ans.append(row/qlen)
#         return ans
# S = Solution()
# Python3 program to find averages of
# all levels in a binary tree.

# # Importing Queue
# from queue import Queue
# class newNode:
# 	def __init__(self, data):
# 		self.val = data
# 		self.left = self.right = None

# def averageOfLevels(root):

# 	q = Queue()
# 	q.put(root)
# 	while (not q.empty()):
# 		Sum = 0
# 		count = 0
# 		temp = Queue()
# 		while (not q.empty()):
# 			n = q.queue[0]
# 			q.get()
# 			Sum += n.val
# 			count += 1
# 			if (n.left != None):
# 				temp.put(n.left)
# 			if (n.right != None):
# 				temp.put(n.right)
# 		q = temp
# 		print((Sum * 1.0 / count), end = " ")

def averageOfLevels(root):
    # In case the tree is empty (you never know :P)
    if root is None:
        return

    # Create the queue for BFS and the list of averages
    queue = []
    averages = []

    # Enqueue Root and initialize nodes_count_per_level and sum_per_level

    queue.append(root)
    nodes_count_per_level = 0
    sum_per_level = 1
    

    # Append None as the root is alone
    queue.append(None)

    # BFS
    while(len(queue) > 0):
        node = queue.pop(0)
        if node is None:
            averages.append(sum_per_level / nodes_count_per_level)
            sum_per_level, nodes_count_per_level = 0, 0
            queue.append(None)

            if queue[0] is None:
                break
            else:
                continue
        sum_per_level += node.val
        nodes_count_per_level += 1
        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)
        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)
    print(averages)

if __name__ == '__main__':
    b = []
    A = input().split()
    for i in range(len(A)):
        b.append(int(i))
    averageOfLevels(b)

	
