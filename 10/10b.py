from sys import stdin

total = 0
lines = stdin.readlines()
goods = []
for i in range(len(lines)):  # for line
    a = []
    bad = False
    for j in lines[i]:  # each char
        if j in ("(", "[", "{", "<"):
            a.append(j)
        else:
            match j:
                case ")":
                    if a[-1] != "(":
                        bad = True
                        break
                    else:
                        del a[-1]

                case "]":
                    if a[-1] != "[":
                        bad = True
                        break
                    else:
                        del a[-1]

                case "}":
                    if a[-1] != "{":
                        bad = True
                        break
                    else:
                        del a[-1]

                case ">":
                    if a[-1] != "<":
                        bad = True
                        break
                    else:
                        del a[-1]
    if not bad:
        goods.append(a)

scores = [0 for i in goods]
for i in range(len(goods)):
    for j in reversed(goods[i]):
        match j:
            case "\n":
                continue
            case "(":
                scores[i] *= 5
                scores[i] += 1
            case "[":
                scores[i] *= 5
                scores[i] += 2
            case "{":
                scores[i] *= 5
                scores[i] += 3
            case "<":
                scores[i] *= 5
                scores[i] += 4
            
scores.sort()
print(scores[len(scores) // 2])
print(scores)
