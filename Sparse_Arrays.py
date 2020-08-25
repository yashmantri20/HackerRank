def matchingStrings(strings, queries):
    d = {}
    result = []
    for i in strings:
        if i not in d:
            d[i] = 1
        else:
            d[i] = d[i] + 1
    for i in queries:
        if i in d:
            result.append(d[i])
        else:
            result.append(0)
    return result
