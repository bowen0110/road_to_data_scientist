class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None




# o(n)
def remove(head, target):
    preNode = None
    curNode = head
    while curNode is not None and curNode.data != target:
        preNode = curNode
        curNode = curNode.next

    if curNode is not None:
        if curNode is head:
            head = curNode.next
        else:
            preNode.next = curNode.next
            curNode.next = None


# o(n)
def search(head, target):
    curNode = head
    while curNode is not None and curNode.data != target:
        curNode = curNode.next
    return curNode is not None

# o(n)
def traverse(head):
    curNode = head
    while curNode is not None:
        print( curNode.data )
        curNode = curNode.next


theHead = ListNode(10)

# to add a node requires O(1) time
newNode = ListNode(20)
newNode.next = theHead
theHead = newNode

remove(theHead, 20)

traverse(theHead)