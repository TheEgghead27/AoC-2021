class Bruh:
    def __init__(self, i):
        self.i = int(i)
        self.y = False

    def __repr__(self):
        return str(self.i)


n = [int(i) for i in input().split(",")]
a = []
try:
    while True:
        input()
        b = []
        for i in range(0, 5):
            c = []
            for j in input().split(' '):
                if j:
                    c.append(Bruh(j))
            b.append(c)
        a.append(b)
except EOFError:
    pass


def find_winner(n, a):
    for i in n:  # each number drawn
        for j in a:  # each board
            for k in j:  # each row
                rights = 0
                for l in k:  # each number (fuck i hate myself)
                    if l.i == i:
                        l.y = True
                        rights += 1
                    elif l.y:
                        rights += 1
                if rights == len(k):  # bingo row
                    return j, i
            for k in range(0, len(j)):  # for each column
                rights = 0
                for l in j:  # get each row
                    if l[k].y:
                        rights += 1

                if rights == len(j):  # bingo row
                    return j, i


def calc_value(board, number):
    sum = 0
    for i in board:
        for j in i:
            if not j.y:
                sum += j.i
    return sum * number


if __name__ == '__main__':
    print(calc_value(*find_winner(n, a)))
