def is_palindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] == ' ' or s[i] == '.':
            i += 1
        if s[j] == ' ' or s[j] == '.':
            j -= 1
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


assert is_palindrome('a b c s s c ba') is True
assert is_palindrome('') is True
assert is_palindrome('a.b c.s s c ba') is True
assert is_palindrome('a b c s s ba') is False
