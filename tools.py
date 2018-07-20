def euclidean_distance(str1, str2):
    s = 0
    for i in range(0, min(len(str1), len(str2))):
        s += (ord(str1[i])-ord(str2[i]))**2
    if len(str1) > len(str2):
        for i in range(len(str2), len(str1)):
            s += ord(str1[i])**2
    else:
        for i in range(len(str1), len(str2)):
            s += ord(str2[i])**2
    return s**(1/2.0)
