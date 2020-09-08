def match(regex, string):
    def match_from(regex_, string_, str_start_poz):
        r_i = 0
        while r_i < regex_.__len__():
            if regex_[r_i] != string_[str_start_poz + r_i] and regex_[r_i] != ".":
                break
            r_i += 1
        return r_i == regex_.__len__()

    start, end = regex.startswith("^"), regex.endswith("$")
    if start:
        regex = regex[1:]
    if end:
        regex = regex[0:-1]

    if not regex:
        return True
    if regex.__len__() > string.__len__() or (start and end and regex.__len__() != string.__len__()):
        return False

    if start or end:
        return match_from(regex, string, 0 if start else string.__len__() - regex.__len__())

    for s_i in range(string.__len__()):
        if regex.__len__() > string.__len__() - s_i:
            return False
        if match_from(regex, string, s_i):
            return True
    return False


print(match(*input().split("|")))
