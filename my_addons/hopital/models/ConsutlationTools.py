from itertools import tee
from datetime import datetime, timedelta


def now(date=None):
    return datetime.now()


def sum(date, minutes):
    return date + timedelta(0, minutes * 60)


def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return [t for t in zip(a, b)]


def formatter(fmt):
    return lambda d: datetime.strptime(d, fmt)


def is_placeable(origin, spc, data):
    v = len(data) > 1
    if v:
        data = pairwise(data)
    elif len(data) == 1:
        data = [data]
    else:
        return True
    or_date_end = sum(origin[0], origin[1] + spc)
    if origin[0] < data[0][0][0]:
        return or_date_end < data[0][0][0]
    if v:
        for lap in data:
            if lap[1][0] > origin[0] > lap[0][0]:
                lap_0_end = sum(lap[0][0], lap[0][1] + spc)
                return lap_0_end <= origin[0] and or_date_end < lap[1][0]
    la_date_end = sum(data[-1][v][0], data[-1][v][1] + spc)
    return origin[0] > la_date_end
