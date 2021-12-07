def try_location(avg: int):
    f = 0
    for i in n:
        j = abs(i - avg)
        j = j * (1 + (0.5 * (j - 1)))
        f += j
    return f

n = [int(i) for i in input().split(',')]
avg = (sum(n) // len(n))

fuels = min([try_location(avg), try_location(avg + 1)])  # in case of non-int avg, try floor and ceil, find the best

print(fuels)
