import sys
import math


def parts(w, l):
    p = []

    for x in w:
        if len(' '.join(p + [x])) > l:
            yield p
            p = [x]
        else:
            p.append(x)

    if p:
        yield p


def iter_joins(w, spaces):
    if len(w) == 1 and spaces == 0:
        yield w[0]

        return

    if spaces < len(w) - 1:
        return

    for i in range(0, spaces):
        n = i + 1

        for l in iter_joins(w[1:], spaces - n):
            yield w[0] + ' ' * n + l


def split_line(l):
    s = ''
    a = ''

    for ch in (l + ' '):
        if ch == ' ':
            if s:
                s += ch
            else:
                yield a
                a = ''
                s = ch
        else:
            if a:
                a += ch
            else:
                yield s
                s = ''
                a = ch


def split_line_pairs(l):
    it = split_line(l)

    while True:
        try:
            yield next(it), next(it)
        except StopIteration:
            return


def imbalance(l):
    w = 0.0
    m = 0

    for s, a in split_line_pairs(l):
        m = max(m, len(s))
        w += len(s) / (len(a) ** 0.5)

    for s, a in split_line_pairs(''.join(reversed(l))):
        m = max(m, len(s))
        w += len(s) / (len(a) ** 0.5)

    return w * (m ** 2)


def just_line(w, l, last):
    if last or len(w) < 2:
        return ' '.join(w)

    r = []

    for l in iter_joins(w, l - len(''.join(w))):
        r.append((imbalance(l), l))

    return sorted(r, key=lambda x: x[0])[0][1]


def iter_l(it):
    f = next(it)

    while True:
        try:
            n = next(it)

            yield f, False

            f = n
        except StopIteration:
            yield f, True

            return


def just(s, l):
    w = [x.strip() for x in s.split(' ')]

    def iter_parts():
        for p, last in iter_l(parts(w, l)):
            yield just_line(p, l, last)
            yield '\n'

    return ''.join(iter_parts())


for l in sys.stdin.read().split('\n\n'):
    l = l.replace('\n', ' ').strip()

    if l:
        print(just(l, 80))
