import time


def timestamp(precision='s'):
    tsp = time.time()
    if precision == 's':
        return int(tsp)

    if precision == 'ms':
        return int(tsp * 1000)

    raise TypeError('accept "s" or "ms", but got "%s"' % precision)
