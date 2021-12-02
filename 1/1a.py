try:
    ups = 0
    x = int(input())
    while True:
        y = int(input())
        if y > x: ups += 1
        x = y
except EOFError:
    print(ups)
