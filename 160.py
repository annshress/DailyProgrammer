"""[4/30/2014] Challenge #160 Intermediate Part 2 - Damage Control"""


def choose(first, last, *to_destroy):
    # we want to choose the build that creates a biggest gap from the (new)edge
    if len(to_destroy) == 1:
        return to_destroy[0]
    d1 = max(to_destroy) - last
    d2 = min(to_destroy) - first
    if abs(d1) > abs(d2):
        return max(to_destroy)
    return min(to_destroy)


kits = []


def preserve_destroy(first, last, *to_destroy):
    destroy = choose(first, last, *to_destroy)
    pres_kits = abs(last - first)  # -1 for the build being destroyed
    print(destroy, " destroyed ", pres_kits, " kits used")
    kits.append(pres_kits)
    # new updated range would be away from the cleaner end
    secx, secy = list(range(first, destroy)), list(range(destroy + 1, last + 1))
    to_destroy = list(to_destroy)
    to_destroy.remove(destroy)
    if not to_destroy:
        return sum(kits)
    if to_destroy[0] in secx:
        new_range = secx
    else:
        new_range = secy
    return preserve_destroy(new_range[0], new_range[-1], *to_destroy)


N = 20
D = [3, 5, 8, 14]

print(f"{preserve_destroy(1, N, *D)} total kits required")
