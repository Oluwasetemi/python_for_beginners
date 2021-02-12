def ask_ok(prompt, retries=4, reminder='Please try again!'):
    """function ask_ok expecting a yes or no"""
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


# ask_ok('what is my name? ')


def f(a, L=None):
    import sys
    print(sys.argv)
    if L is None:
        L = [9]
        L.append(a)
        return L


print(f(1))
print(f(2))
print(f(3))


def make_incrementor(n):
    return lambda x: x + n


x = make_incrementor(2)(2)
print(x)
