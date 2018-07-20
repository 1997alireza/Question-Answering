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


def edit_distance(str1, str2):
    # w_ins == w_del == w_sub
    l1 = len(str1)
    l2 = len(str2)
    diff = [[0 for i in range(0, l2+1)] for j in range(0, l1+1)]
    diff[0][0] = 0
    for i in range(1, l1+1):
        diff[i][0] = i
    for i in range(1, l2+1):
        diff[0][i] = i
    for i in range(1, l1+1):
        for j in range(1, l2+1):
            if str1[i-1] == str2[j-1]:
                diff[i][j] = diff[i-1][j-1]
            else:
                diff[i][j] = min(
                    diff[i-1][j],
                    diff[i][j-1],
                    diff[i-1][j-1]
                ) + 1
    return diff[l1][l2]


def find_best_match(sheet, q_col, question, distance_function=euclidean_distance):
    best_index = 0
    best_score = distance_function(question, str(sheet.cell(0, q_col).value))
    for row in range(1, sheet.nrows):
        q = str(sheet.cell(row, q_col).value)
        ed = distance_function(question, q)
        if best_score > ed:
            best_score = ed
            best_index = row
    # print(best_index)
    return best_index



