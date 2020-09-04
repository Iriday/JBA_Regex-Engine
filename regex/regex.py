def match(regex, string):
    if regex.__len__() == 0:
        return True
    if regex == string:
        return True
    if string.__len__() == 0:
        return False
    if regex == ".":
        return True
    return False


print(match(*input().split("|")))
