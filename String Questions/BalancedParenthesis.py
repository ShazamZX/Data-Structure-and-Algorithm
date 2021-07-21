#Check whether the given parenthesis is balanced or not

def parenthesis(s):
    stack = []
    for i in s:
        if i == '{' or i =='(' or i=='[':
            stack.append(i)
        else:
            if not stack:
                return False
            current = stack.pop()
            if current == '(' and i != ')':
                return False
            if current == '[' and i != ']':
                return False
            if current == '{' and i != '}':
                return False
    if stack:
        return False
    return True

#driver code


print(parenthesis("{[]}()"))