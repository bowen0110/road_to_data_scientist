from stack_python_list_version import StackPythonList

my_stack = StackPythonList()
# my_stack.pop()
# my_stack.peek()

assert len(my_stack) == 0
assert my_stack.isEmpty()

my_stack.push(15)
my_stack.push(13)
my_stack.push(15)
my_stack.push(12)
my_stack.push(16)

assert len(my_stack) == 5
# assert my_stack.isEmpty()

my_stack.pop()
print(my_stack.peek())
print(my_stack._stack)



from stack_linked_list_version import StackLinkedList


def printLinkedListStack(stack):
    curNode = stack._stack
    value = list()
    while curNode:
        value.append(curNode._data)
        curNode = curNode.next
    print(value)

s = StackLinkedList()
s.push(12)
s.push(112)
s.push(42)
s.push(2)
s.push(5)
s.push(0)
s.pop()
s.pop()

print(s.peek())
printLinkedListStack(s)
print(s.isEmpty())
print(len(s))
