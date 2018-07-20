class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
    def rotateRight(self, head, k):
        if head == None or k == 0:
            return head
        
        length = 1
        node = head
        while node.next != None:
            length += 1
            node = node.next
            
        m = k % length
        
        node.next = head
        
        for i in range(length - m):
            node = node.next
        
        head = node.next
        
        node.next = None
        return head