from stack_linked_list_version import StackLinkedList

src = '{{{{{{{{[]()}}}}}}}})'

def checkDelimiters(src):
    stack = StackLinkedList()
    for line in src:
        for word in line:
            if word in '[{(':
                stack.push(word)
            elif word in ']})':
                if stack.isEmpty():
                    return False
                else:
                    item = stack.pop()
                    if (item is '}' and word is not '{') or \
                        (item is ']' and word is not '[') or \
                        (item is ')' and word is not '('):
                        return False
    return stack.isEmpty()


print(checkDelimiters(src))