def isNegative(s):
    if s[0] == '-':
        return isExponent(s[1:])
    return isExponent(s)
    pass


def isNumber(self, s: str) -> bool:
    return isNegative(s.strip())