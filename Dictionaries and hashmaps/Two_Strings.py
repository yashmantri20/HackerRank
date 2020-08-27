def twoStrings(s1, s2):
    for i in s2:
        if i in s1:
            return "YES"
    return "NO"