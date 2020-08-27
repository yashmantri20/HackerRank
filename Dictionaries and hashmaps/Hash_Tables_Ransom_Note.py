def checkMagazine(magazine, note):
    d = dict()
    for i in magazine:
        if i not in d:
            d[i] = 1
        else:
            d[i] = d[i] + 1
    
    for i in note:
        if i in d:
            if d[i] >= 1:
                d[i] = d[i] - 1
            else:
                print("No")
                return
        else:
            print("No")
            return
    print("Yes")