def match(regex, string):
    def match_from(regex_, string_, str_start_poz, dollar_=False):
        r_len = regex_.__len__()
        s_len = string_.__len__()
        r = 0  # regex index
        s = str_start_poz  # string index

        while r < r_len and s < s_len:
            # if next val in "?*+"
            if r + 1 != r_len and regex_[r + 1] in "?*+":
                metacharacter = regex_[r + 1]
                # values are equal
                if regex_[r] == string_[s]:
                    r += 1  # handles metacharacter "?" too
                    if metacharacter in "+*":
                        while s + 1 != s_len and string_[s] == string_[s + 1]:
                            s += 1
                # "."
                elif regex_[r] == ".":
                    if metacharacter in "*+":
                        if r + 2 == r_len:  # if regex ends with ".*" or ".+" return true
                            return True
                        else:
                            r += 2
                            while s < s_len and regex_[r] != string_[s]:
                                s += 1
                            if regex_[r] != string_[s]:
                                return False
                    elif metacharacter == "?":
                        if r + 2 == r_len:
                            r += 1
                        else:
                            r += 2
                            if s + 1 != s_len and r == string_[s + 1]:
                                s += 1
                # values are not equal
                else:
                    if metacharacter in "?*":
                        r += 1
                        s -= 1
                    elif metacharacter == "+":
                        return False
            # if next val not in "?*+" (common case)
            else:
                if regex_[r] != string_[s] and regex_[r] != ".":
                    break

            r += 1
            s += 1

        if r + 2 == r_len and regex_[r + 1] in "?*":
            r += 2
        return r == r_len if not dollar_ else r == r_len and s == s_len

    circumflex, dollar = regex.startswith("^"), regex.endswith("$")
    if circumflex:
        regex = regex[1:]
    if dollar:
        regex = regex[0:-1]

    if not regex:
        return True

    if circumflex:
        return match_from(regex, string, 0, dollar_=dollar)
    for i in range(string.__len__()):
        if match_from(regex, string, i, dollar_=dollar):
            return True
    return False


print(match(*input().split("|")))
