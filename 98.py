"""
Challenge #98 [intermediate] (Multiple cycling)
"""


def multiple_cycle(lim, x):
    count = 0
    output = 0
    while output < lim:
        each = x[count % len(x)]
        count += 1
        m = output // each + 1
        output = each * m
        print(output, end="  ")
    return count


if __name__ == "__main__":
    # print(multiple_cycle(16, [5, 7, 3]))
    print(multiple_cycle(1000000000, [5395, 7168, 2367, 9999, 3]))
