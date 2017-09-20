import decimal
import pygame
import re

# # # # # # # # # # # # # # # # # #
# Another Example, this one       #
# lets you call functions like:   #
# name(arg1,arg2,...,argn)        #

re_function = re.compile(r'(?P<name>\S+)(?P<params>[\(].*[\)])')


def console_func(console, match):
    print(match)
    print(match.group("name"))
    print(match.group("params"))
    func = console.convert_token(match.group("name"))
    params = console.convert_token(match.group("params"))

    if not isinstance(params, tuple):
        params = [params]
    try:
        out = func(*params)
    except Exception as strerror:
        console.output(strerror)
    else:
        console.output(out)

def add(a, b):
    """Simple add Function! Use: add a b"""
    return a + b

def draw(a, b, c):
    """ Simple draw circle Function! Use: draw 400 400 100"""
    return pygame.draw.circle(pygame.display.get_surface(), (0, 0, 255), (a, b), c, 1)

def pi():
    """
    Compute Pi to the current precision. Use: pi
    """
    decimal.getcontext().prec += 2  # extra digits for intermediate steps
    three = decimal.Decimal(3)  # substitute "three=3.0" for regular floats
    lasts, t, s, n, na, d, da = 0, three, 3, 1, 0, 0, 24
    while s != lasts:
        lasts = s
        n, na = n + na, na + 8
        d, da = d + da, da + 32
        t = (t * n) / d
        s += t
    decimal.getcontext().prec -= 2
    return +s  # unary plus applies the new precision