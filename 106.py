"""
[10/23/2012] Challenge #106 [Intermediate] (Jugs)
"""


def print_me(func):
    def wrapper(instance, *args):
        func(instance, *args)
        print(f"{instance} is now {instance.filled} l full")

    return wrapper


class Jug:
    def __init__(self, max):
        self.max = max
        self.filled = 0

    def __str__(self):
        return f"{self.max}L jug"

    @property
    def empty(self):
        return self.max - self.filled

    @print_me
    def fill_me(self, fill=0):
        if not fill:
            self.filled = self.max
        if self.filled + fill < self.max:
            self.filled += fill
            self.filled = self.max

    @print_me
    def empty_me(self):
        self.filled = 0
        return self

    def transfer(self, other):
        print(
            f"{self} ({self.filled}l) transfers to {other} ({other.filled}l)",
            end=" ===> ",
        )
        remaining = other.max - other.filled
        if self.filled < remaining:
            other.filled += self.filled
            self.filled = 0
        elif self.filled == remaining:
            other.filled = remaining
            self.filled = 0
        else:
            emp = other.empty
            other.filled = other.max
            self.filled -= emp
        print(f"{self} now ({self.filled}l)-> {other} now ({other.filled}l)")


S, B = 5, 7
DESIRED = 6
small = Jug(S)
big = Jug(B)


def process():
    while True:
        big.fill_me()
        yield
        big.transfer(small)
        yield
        small.empty_me()
        big.transfer(small)
        yield


for i in process():
    if (big.filled == DESIRED) or (small.filled == DESIRED):
        print(big, "->", big.filled, small, "->", small.filled)
        break
