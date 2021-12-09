totals = []
try:
    while True:
        print("*" * 50)
        n = input().split(" ")
        data = {"threetwofive": [], "sixnineo": []}
        nsorted = []
        for i in n:
            i = list(i)
            i.sort()
            i = ''.join(i)
            nsorted.append(i)
            l = len(i)
            match l:
                case 2:
                    data[1] = i
                    # break
                case 3:
                    data[7] = i
                    # break
                case 4:
                    data[4] = i
                    # break
                case 5:
                    if i not in data["threetwofive"]:
                        data["threetwofive"].append(i)
                    # break
                case 6:
                    if i not in data["sixnineo"]:
                        data["sixnineo"].append(i)
                    # break
                case 7:
                    data[8] = i
                    # break
        
        numberos = {
                "a": next(filter(lambda a: a, [i if i not in data[1] else None for i in data[7]])),
        }

        for i in data[1]:
            for j in data["sixnineo"]:
                if i not in j:
                    data[6] = j  # six is the only one to not have point c
                    break
        data["sixnineo"].remove(data[6])
        numberos["c"] = next(filter(lambda a: a, [i if i not in data[6] else None for i in data[8]]))  # c is also the only point it lacks
        numberos["f"] = next(filter(lambda a: a, [i if i in data[1] else None for i in data[6]]))  # both have f

        ed = []
        for j in data["sixnineo"]:  # 9 and 0 left
            for i in data[8]:
                if i not in j:
                    ed.append(i)  # candidates for e and d
                    break
        for i in ed:
            if i not in data[4]:
                numberos["e"] = i  # 4 has spot d,  but not e
                break
        ed.remove(numberos["e"])
        numberos["d"] = ed[0]
        del ed

        for i in data["sixnineo"]:
            if numberos["d"] in i:
                data[9] = i  # 0 lacks point d
                continue
            data[0] = i
        del data["sixnineo"]
        
        for i in data["threetwofive"]:
            if numberos["f"] in i:
                if numberos["c"] in i:
                    data[3] = i
                else:  # 5 no c
                    data[5] = i
            else:  # 2 only one w/o f
                data[2] = i

        del data["threetwofive"]

        print(numberos)
        print(data)

        number = 0
        for i in (nsorted[-4:]):
            for j in data.keys():
                print(f"Key: {j}")
                if i == data[j]:
                    number += j
                    number *= 10
                    print(i, j)
        number = number // 10
        print(number)
        print(n, nsorted)
        totals.append(number)
        del data, numberos, nsorted, n


except EOFError:
    print(f"Final: {sum(totals)}\n{totals}")
