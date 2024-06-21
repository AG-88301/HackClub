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
                
    def process(r, c):
        if type(shape[r][c]) == int:
            return
        
        if shape[r][c] == '|':
            if 0 < c and type(shape[r][c-1]) == int:
                id = shape[r][c-1]
                shapes[id][r-sizes[id][0]+1][c-sizes[id][1]+1] = '|'
                
            if c < len(shape[0])-1 and type(shape[r][c+1]) == int:
                id = shape[r][c+1]
                shapes[id][r-sizes[id][0]+1][c-sizes[id][1]+1] = '|'
                
        elif shape[r][c] == '-':
            if 0 < r and type(shape[r-1][c]) == int:
                id = shape[r-1][c]
                shapes[id][r-sizes[id][0]+1][c-sizes[id][1]+1] = '-'
                
            if r < len(shape)-1 and type(shape[r+1][c]) == int:
                id = shape[r+1][c]
                shapes[id][r-sizes[id][0]+1][c-sizes[id][1]+1] = '-'
                
        elif shape[r][c] == '+': 
            dirs = [(-1, 1), (1, -1), (-1, -1), (1, 1), (0, 1), (1, 0), (-1, 0), (0, -1)]
            for dx, dy in dirs:
                if 0 <= r+dx < len(shape) and 0 <= c+dy < len(shape[0]) and type(shape[r+dx][c+dy]) == int:
                    id = shape[r+dx][c+dy]
                    shapes[id][r-sizes[id][0]+1][c-sizes[id][1]+1] = '+'
                
                
    shapes = [[[" "] * (3 + sizes[i][3] - sizes[i][1]) for _ in range(3 + sizes[i][2] - sizes[i][0])] for i in range(id)]
    for r in range(len(shape)):
        for c in range(len(shape[0])):
            process(r, c)
            
    for i in range(len(shapes)):
        s = shapes[i]
        for r in range(len(s)):
            for c in range(len(s[0])):
                if s[r][c] == '+':
                    if 0 < r < len(s) - 1:
                        if s[r+1][c] != ' ' and s[r-1][c] != ' ':
                            shapes[i][r][c] = '|'
                    if 0 < c < len(s[0]) - 1:
                        if s[r][c+1] != ' ' and s[r][c-1] != ' ':
                            if shapes[i][r][c] == '|':
                                shapes[i][r][c] = '+'
                            else:
                                shapes[i][r][c] = '-'
    
    shapes = ['\n'.join([''.join(c).rstrip() for c in s]) for s in shapes]
    return shapes

shape = ""
lst = ""
while lst != '.':
    lst = input()
    shape += lst + '\n'
print('\n'.join(break_pieces(shape)))
