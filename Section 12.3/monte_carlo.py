from random import *
import numba


@numba.jit(nopython=True, nogil=True, cache=True)
def monte_carklo_search():
    n = 1000000000
    k = 0
    s0 = 16

    for _ in range(n):
        x = uniform(-2, 2)
        y = uniform(-2, 2)

        if y ** 3 - 2 * x ** 2 <= -1 and 2 * y + x ** 3 <= 3:
            k += 1

    print((k / n) * s0)


monte_carklo_search()
