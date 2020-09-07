def match(regex, string):
    if regex.__len__() > string.__len__():
        return False
    for i in range(regex.__len__()):
        if regex[i] != string[i] and regex[i] != ".":
            return False
    return True


print(match(*input().split("|")))
