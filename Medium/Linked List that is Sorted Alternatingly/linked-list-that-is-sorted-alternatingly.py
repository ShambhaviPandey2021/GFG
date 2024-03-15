#User function Template for python3

'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def sort(self, head):
        if not head or not head.next:
            return head
        
        def split(head):
            asc_head = Node(0)
            desc_head = Node(0)
            asc_curr = asc_head
            desc_curr = desc_head
            is_asc = True
            
            while head:
                if is_asc:
                    asc_curr.next = head
                    asc_curr = asc_curr.next
                else:
                    desc_curr.next = head
                    desc_curr = desc_curr.next
                
                head = head.next
                is_asc = not is_asc
            
            asc_curr.next = None
            desc_curr.next = None
            
            return asc_head.next, desc_head.next
        
        def reverse(head):
            prev = None
            curr = head
            
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            
            return prev
        
        def merge(asc_head, desc_head):
            dummy = Node(0)
            curr = dummy
            
            while asc_head and desc_head:
                if asc_head.data < desc_head.data:
                    curr.next = asc_head
                    asc_head = asc_head.next
                else:
                    curr.next = desc_head
                    desc_head = desc_head.next
                
                curr = curr.next
            
            curr.next = asc_head or desc_head
            
            return dummy.next
        
        asc_head, desc_head = split(head)
        desc_head = reverse(desc_head)
        sorted_head = merge(asc_head, desc_head)
        
        return sorted_head




#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Llist:
    def __init__(self):
        self.head=None
    
    def insert(self,data,tail):
        node=Node(data)
        
        if not self.head:
            self.head=node
            return node
        
        tail.next=node
        return node
        

def printList(head):
    while head:
        print(head.data,end=' ')
        head=head.next
        
if __name__ == '__main__':
    t=int(input())
    
    for tcs in range(t):
        
        n1=int(input())
        arr1=[int(x) for x in input().split()]
        ll1=Llist()
        tail=None
        for nodeData in arr1:
            tail=ll1.insert(nodeData,tail)
            
        
        ob = Solution()
        resHead=ob.sort(ll1.head)
        printList(resHead)
        print()
        
    
    
# } Driver Code Ends