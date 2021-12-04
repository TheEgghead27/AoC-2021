def find_values(n, i = 0, pref_up = lambda a,b: a >= b):
    if len(n) == 1:  # hope and fucking pray we dont have duplicates
        return n[0]
    ones = 0
    on = []
    zeroes = 0
    off = []
    for j in n:
        if j[i] == "1":
            ones += 1
            on.append(j)
        else:
            zeroes += 1
            off.append(j)
    if pref_up(ones, zeroes):
        del off, zeroes
        return find_values(on, i + 1, pref_up)
    else:
        del on, ones
        return find_values(off, i + 1, pref_up)




n = []
try:
    while True:
        n.append(input())
except EOFError:
    pass
"""
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
"""
oxy = find_values(n) 
carb = find_values(n, pref_up=lambda a, b: a < b)
print(int(oxy, 2) * int(carb, 2))
