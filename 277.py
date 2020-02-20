"""
Challenge #277 [Easy] Simplifying fractions
"""
import itertools


def divisors(num):
    """will return possible divisors"""
    divisors = [div for div in range(2, (num // 2) + 1) if num % div == 0]
    divisors += [1, num]
    return set(divisors)


def hcf(a, b):
    common_divs = divisors(a).intersection(divisors(b))
    return max(common_divs)


# Euclidean Algorithm for finding greatest common divisor
def gcd(a, b):
    while b:
        return gcd(b, a % b)
    return a


def simplify(a, b):
    """handles numbers only"""
    # HCF = hcf(a, b)
    HCF = gcd(a, b)
    return a // HCF, b // HCF


input = """1536 78360
51478 5536
46410 119340
7673 4729
4096 1024"""

if __name__ == "__main__":

    for each in input.split("\n"):
        a, b = map(lambda x: int(x), each.split(" "))
        print(each, " => ", simplify(a, b))


############################################
# simplifying fractions of letters instead #
############################################


def replace(a, equalities):
    """replaces possible values in a(numerator or denominator) from given equalities"""
    if not set(equalities.keys()).intersection(list(a)):
        return list(a)
    return replace(
        list(itertools.chain.from_iterable([equalities.get(char, char) for char in a])),
        equalities,
    )


def get_equalities(eqs):
    """get equalities"""
    return {eq.split(" ")[0]: eq.split(" ")[1] for eq in eqs}


def simply_string(fraction, equalities):
    """simplifies the string"""
    a, b = fraction.split(" ")
    numerator = replace(a, equalities)
    denominator = replace(b, equalities)
    for each in denominator[:]:
        if each in numerator:
            numerator.remove(each)
            denominator.remove(each)
    return " / ".join(("".join(numerator or ["1"]), "".join(denominator or ["1"])))


input = """3
x cb
y ab
z xa
ab cb
ab x
x y
z y
z xay"""

if __name__ == "__main__":
    lines = input.split("\n")
    eq_count = int(lines[0])
    equalities = get_equalities(lines[1 : eq_count + 1])
    for fraction in lines[1 + eq_count :]:
        print(fraction, "=>", simply_string(fraction, equalities))

