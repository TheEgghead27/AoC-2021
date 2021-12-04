n = []
try:
    while True:
        n.append(input())
except EOFError:
    pass

a = [0 for i in n[0]]
num_len = len(n[0])
full_len = 0

for i in n:
    full_len += 1
    for j in range(0, num_len):
        if i[j] == "1":
            a[j] += 1

gamma = 0
epsilon = 0
goal = full_len / 2
for i in a:
    gamma *= 2
    epsilon *= 2
    if i > goal:
        gamma += 1
    else:
        epsilon += 1

print(gamma * epsilon)
print(a, goal)
