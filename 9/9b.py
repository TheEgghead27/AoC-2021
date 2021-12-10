from sys import stdin
matrix = []
for line in stdin.readlines():
    matrix.append([999] + [int(i) for i in line.rstrip()] + [999])
a = [999] * len(matrix[1])
matrix.insert(0, a)
matrix.append(a)
del a

print(matrix)
points = []
for y in range(1, len(matrix) - 1):  # row
    for i in range(1, len(matrix[0]) - 1):  # column
        bruh = False
        for j in (matrix[y-1][i],matrix[y+1][i],matrix[y][i-1],matrix[y][i+1]):
            if matrix[y][i] >= j:
                bruh = True
                break
        if not bruh and matrix[y][i] < 9:
            print(f"winner {matrix[y][i]} ({y},{i})")
            points.append((y, i))
print(points)


def search(point, friends):
    y,i = point
    if point not in friends:  # we know this is a basin point because our checks sent it
        friends.append(point)  # keep track of all unique good points
    else:
        # print("?!?!?! already checked this point")
        return friends
    for j in ((y-1,i), (y+1,i), (y, i-1), (y, i+1)):  # up, down, left, right
        if matrix[j[0]][j[1]] in (9, 999):  # 9 nor placeholder cant into basin
            continue
        if ((matrix[point[0]][point[1]] - matrix[j[0]][j[1]]) < 0):
            # our test point is a valid basin, it is one higher than the point we already have
            friends = search(j, friends)
    return friends

basins = []
for i in points:
    a = search(i, friends=[])
    print(f"found: {a}, size {len(a)}, point {i}, value {matrix[i[0]][i[1]]}")
    basins.append(len(a))
# get top 3 basins, print answer
basins.sort()
print(basins)
t = 1
for i in basins[-3:]:
    t *= i
print(t)
