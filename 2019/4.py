
def is_valid_password(i):
    s = str(i)
    adjacent = False
    previous = int(s[0])
    for c in s[1:]:
        c = int(c)
        if not adjacent and  c == previous:
            adjacent = True
        if c < previous:
            return False
        previous = c
    return adjacent
    

print(sum( is_valid_password(i) for i in range(108457, 562041)))


# second part

def is_valid_password(i):
    s = str(i)
    adjacent = None
    previous = int(s[0])
    pre_previous = None
    for idx, c in enumerate(s[1:]):
        c = int(c)
        if c == previous:
            if c != pre_previous:
                if idx == 4:
                    adjacent = True
                elif c != int(s[idx+2]):
                    adjacent = True
        if c < previous:
            return False
        pre_previous = previous
        previous = c
    return bool(adjacent)

print(sum( is_valid_password(i) for i in range(108457, 562041)))
