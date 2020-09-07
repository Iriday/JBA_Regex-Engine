def match(regex, string):
    if not regex:
        return True
    for s_i in range(string.__len__()):
        if regex.__len__() > string.__len__() - s_i:
            return False
        r_i = 0
        while r_i < regex.__len__():
            if regex[r_i] != string[s_i + r_i] and regex[r_i] != ".":
                break
            r_i += 1
        if r_i == regex.__len__():
            return True
    return False


print(match(*input().split("|")))
