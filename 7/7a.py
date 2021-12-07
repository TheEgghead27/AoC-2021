n = [int(i) for i in input().split(',')]
n.sort()
print(n)

med = (n[len(n) // 2]) if len(n) % 2 else (n[len(n) // 2] + n[len(n) // 2 - 1]) // 2

print(med)

fuels = 0
for i in n:
    fuels += abs(i - med)
print(fuels)
