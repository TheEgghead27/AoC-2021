from sys import stdin

total = 0

for i in stdin.readlines():
    a = []
    for j in i:  # line
        if j in ("(", "[", "{", "<"):
            a.append(j)
        else:
            match j:
                case ")":
                    if a[-1] != "(":
                        total += 3
                        print(a, j)
                        break
                    else:
                        del a[-1]

                case "]":
                    if a[-1] != "[":
                        total += 57                       
                        print(a, j)
                        break
                    else:
                        del a[-1]

                case "}":
                    if a[-1] != "{":
                        total += 1197
                        print(a, j)
                        break
                    else:
                        del a[-1]
                case ">":
                    if a[-1] != "<":
                        total += 25137
                        print(a, j)
                        break
                    else:
                        del a[-1]
print(total)
