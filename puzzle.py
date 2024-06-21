def break_pieces(shape):
    shape = shape.splitlines()
    while len(shape[0].strip()) == 0:
        shape.pop(0)
    x = 0
    for i in shape:
        x = max(len(i), x)
    
    for i in range(len(shape)):
        shape[i] = shape[i] + ' '*(x - len(shape[i]))
    shape = [list(s) for s in shape]
    dirs = [0, 1, 0, -1, 0]
    
    def fill(r, c, id):
        if not (0 <= r < len(shape) and 0 <= c < len(shape[0]) and shape[r][c] == ' '):
            return
        shape[r][c] = id
        
        if id != '.':
            sizes[id] = (
                min(sizes[id][0], r), 
                min(sizes[id][1], c),
                max(sizes[id][2], r), 
                max(sizes[id][3], c)
            )
    
        for i in range(4):
            fill(r+dirs[i], c+dirs[i+1], id)
    
    for r in range(len(shape)):
        fill(r, 0, '.')
        fill(r, len(shape[0])-1, '.')
    for c in range(len(shape[0])):
        fill(0, c, '.')
        fill(len(shape)-1, c, '.')
    
    id = 0
    sizes = []
    for r in range(len(shape)):
        for c in range(len(shape[0])):
            if shape[r][c] == ' ': 
                sizes.append((float('inf'), float('inf'), 0, 0))
                fill(r, c, id)
                id += 1
                
    return shape

shape = ""
lst = ""
while lst != '.':
    lst = input()
    shape += lst + '\n'
print('\n'.join(''.join(map(str, i)) for i in break_pieces(shape)))
