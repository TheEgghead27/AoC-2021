from sys import stdin
matrix = []
for line in stdin.readlines():
    matrix.append([999] + [int(i) for i in line.rstrip()] + [999])
a = [999] * len(matrix[1])
matrix.insert(0, a)
matrix.append(a)
del a

print(matrix)
total = 0
for y in range(1, len(matrix) - 1):  # row
    for i in range(1, len(matrix[0]) - 1):  # column
        bruh = False
        for j in (matrix[y-1][i],matrix[y+1][i],matrix[y][i-1],matrix[y][i+1]):
            if matrix[y][i] >= j:
                bruh = True
                break
        if not bruh:
            print(f"winner {matrix[y][i]} ({y},{i})")
            total += matrix[y][i] + 1
print(total)
