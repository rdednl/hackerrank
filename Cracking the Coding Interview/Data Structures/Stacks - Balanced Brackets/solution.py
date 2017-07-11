def is_matched(expression):
    expr = []
    for char in expression:
        if char == '(':
            expr.append(')')
        elif char == '[':
            expr.append(']')
        elif char == '{':
            expr.append('}')
        else:
            if (expr == []) or (char != expr[-1]):
                return False
            else:
                expr = expr[0:-1]
    return (expr == [])          
    
t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")