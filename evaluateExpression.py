def calc(expression):
    expression = expression.replace(" ", "").replace("--", '+').replace('+-', '-').replace('-+', '-')
    expr = ['']
    ind = 0
    while ind < len(expression):
        i = expression[ind]
        if i == '-':
            if expr[-1] == '-':
                expr[-1] = '+'
            elif expr[-1] == '+':
                expr[-1] = '-'  
            elif expr[-1] == '':
                expr[-1] = '-o'
                expr.append('')
            else:
                expr.append('-')
                expr.append('')
                
        elif i in '+*/':
            expr.append(i)
            expr.append('')
            
        elif i == '(':
            depth = 1
            brack = ""
            ind += 1
            while depth:
                if expression[ind] == '(':
                    depth += 1
                elif expression[ind] == ')':
                    depth -= 1
                brack += expression[ind]
                ind += 1
            ind -= 1
            expr[-1] = calc(brack[:-1])
        else:
            if expr[-1] == '': expr[-1] = 0
            expr[-1] = expr[-1] * 10 + float(i)
        ind += 1
        
    n = []
    ind = 0
    while ind < len(expr):
        i = expr[ind]
        if i == '-o':
            n.append(-expr[ind+1])
            ind += 2
        else:
            n.append(i)
            ind += 1

    new = [n[0]]
    ind = 1
    while ind < len(n):
        i = n[ind]
        if i == '*':
            new[-1] *= n[ind + 1]
            ind += 2
        elif i == '/':
            new[-1] /= n[ind + 1]
            ind += 2
        else:
            new.append(i)
            ind += 1
    
    expr = [new[0]]
    ind = 1
    while ind < len(new):
        i = new[ind]
        if i == '+':
            expr[-1] += new[ind + 1]
            ind += 2
        elif i == '-':
            expr[-1] -= new[ind + 1]
            ind += 2
        else:
            new.append(i)
            ind += 1
    return int(expr[0]) if expr[0] == int(expr[0]) else expr[0]

expression = input()
print(calc(expression))
