import math

first_matrix = ((0,3,1,3,0,0),
     (3,0,4,0,0,0),
     (1,4,0,0,7,5),
     (3,0,0,0,0,2),
     (0,0,5,2,4,0)
)

count_v = len(first_matrix)

end_matrix = [math.inf]*count_v

start_v = 0

#просмотренные вершины
check_v = {start_v}

end_matrix[start_v] = 0

#если есть связь между двумя вершинами - 1
def get_link_v(start_v, first_matrix):
    for i, weigth in enumerate(first_matrix[start_v]):
        if weigth > 0:
            yield 1

def arg_min(end_matrix, check_v):
    amin = -1
    minimum = max(end_matrix)
    for i, end_matrix in enumerate(end_matrix):
        if end_matrix < minimum and i not in check_v:
            minimum = end_matrix
            amin = i
    return amin

while start_v != -1:
    for j in get_link_v(start_v, first_matrix):
        if j not in check_v:
            w = end_matrix[start_v] + first_matrix[start_v][j]
            if w < end_matrix[j]:
                end_matrix[j] = w
    start_v = arg_min(end_matrix, check_v)
    if start_v > 0:
        check_v.add(start_v)

print(end_matrix)