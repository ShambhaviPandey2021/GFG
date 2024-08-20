#User function Template for python3

class Solution:
    def createParentMapping(self, root, parent_map):
        queue = deque([root])
        parent_map[root] = None
        while queue:
            node = queue.popleft()
            if node.left:
                parent_map[node.left] = node
                queue.append(node.left)
            if node.right:
                parent_map[node.right] = node
                queue.append(node.right)

    def findTargetNode(self, root, target):
        if root is None:
            return None
        if root.data == target:
            return root
        left = self.findTargetNode(root.left, target)
        if left:
            return left
        return self.findTargetNode(root.right, target)
        
    def minTime(self, root,target):
        # code here
        if not root:
            return 0
        
        parent_map = {}
        self.createParentMapping(root, parent_map)
        
        target_node = self.findTargetNode(root, target)
        if not target_node:
            return 0
        
        visited = set()
        queue = deque([(target_node, 0)])  
        visited.add(target_node)
        max_time = 0
        
        while queue:
            current_node, current_time = queue.popleft()
            max_time = max(max_time, current_time)
            
            # Traverse the left child
            if current_node.left and current_node.left not in visited:
                visited.add(current_node.left)
                queue.append((current_node.left, current_time + 1))
            
            # Traverse the right child
            if current_node.right and current_node.right not in visited:
                visited.add(current_node.right)
                queue.append((current_node.right, current_time + 1))
            
            # Traverse the parent
            parent_node = parent_map[current_node]
            if parent_node and parent_node not in visited:
                visited.add(parent_node)
                queue.append((parent_node, current_time + 1))
        
        return max_time


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import deque

# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        line=input()
        target=int(input())
        root=buildTree(line)
        print(Solution().minTime(root,target))

# } Driver Code Ends