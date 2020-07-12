import sys

vertices = [[0, 1, 0, 1, 0],
            [1, 0, 1, 1, 1],
            [0, 1, 0, 0, 1],
            [1, 1, 0, 0, 1],
            [0, 1, 1, 1, 0]]
edges =  [[0, 6, 0, 1, 0],
          [6, 0, 5, 2, 2],
          [0, 5, 0, 0, 5],
          [1, 2, 0, 0, 1],
          [0, 2, 5, 1, 0]]

n = len(vertices[0])
vertice = [[0,0]]

for i in range(n-1):
    vertice.append([0,sys.maxsize])

def not_visited():
    global vertice
    v = -10
    for i in range(n):
        if vertice[i][0] == 0 and (v<0 or vertice[i][1] <= vertice[v][1]):
            v = i
    return v

for j in range (n):
    t = not_visited()
    for k in range(n):
        if vertices[t][k] == 1 and vertice[k][0] == 0:
            new = vertice[t][1] + edges[t][k]
            if vertice[k][1] > new:
                vertice[k][1] = new

        vertice[t][0] = 1


result = []
for d in vertice:
    result.append(d[1])

print(f'The shortest distance of A from the source vertex is {result[0]}')
print(f'The shortest distance of B from the source vertex is {result[1]}')
print(f'The shortest distance of C from the source vertex is {result[2]}')
print(f'The shortest distance of D from the source vertex is {result[3]}')
print(f'The shortest distance of E from the source vertex is {result[4]}')