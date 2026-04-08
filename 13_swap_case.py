def swap_case(s):
    r = ""
    for i in s:
        if i.islower():
            r += i.upper()
        elif i.isupper():
            r += i.lower()
        else:
            r += i
    return r
