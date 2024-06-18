
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
        
    return expr
expression = input()
print(calc(expression))
