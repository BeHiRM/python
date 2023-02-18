
def ispalin(s):
    n = len(s)
    for i in range(n//2):
        if s[i] != s[n-1-i]:
            return False
        return True


x = "alirezaalireza"
print(ispalin(x))
