"""
Challenge #153 [Easy] Pascal's Pyramid

TRINOMIAL DISTRIBUTION CONNECTION: https://en.wikipedia.org/wiki/Pascal's_pyramid#Trinomial_distribution_connection
"""
import functools


def factorial(n):
    if n in [0, 1]:
        return 1
    return n * factorial(n - 1)


def trinomial_distribution(layer):
    jagged_arrays = []
    for each in range(layer + 1):
        jagged_arrays.append(
            list(
                zip(
                    [layer - each - n for n in range(layer - each + 1)],
                    [each] * (layer - each + 1),
                    [n for n in range(layer - each + 1)],
                )
            )
        )
    return jagged_arrays


def nth_layer_of_pascals_pyramid(layer):
    distribution = trinomial_distribution(layer)
    for p in distribution:
        for number in p:
            print(
                factorial(layer)
                // functools.reduce(
                    lambda x, y: x * y, [factorial(num) for num in number]
                ),
                end=" ",
            )
        print()


LAYER = 5
nth_layer_of_pascals_pyramid(LAYER)
