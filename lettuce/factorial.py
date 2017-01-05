def f1(n):
    c = 1
    for i in range(n):
        i = i + 1
        c = c * i
    return c

def f2(n):
    if n > 1:
        return n *f2(n-1)
    else:
        return 1

if __name__ == '__main__':
    print(f1(10))
    print(f2(10))


