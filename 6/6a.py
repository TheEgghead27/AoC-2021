# n = []
# m = -1  # off by one because initial value doesnt count as a day


# try:
#     while True:
n = [int(i) for i in input().split(' ')[-1].split(',')]
m = 0
# except EOFError:
#    pass

while m < 80:
    print(m)
    for i in range(len(n)):  # no python 3.10 no match case :(
        if not n[i]:
            n[i] = 6
            n.append(8)
        else:
            n[i] -= 1
    m += 1
print(m, len(n))

