
__author__ = "Josh Zack"
__email__ = "zackjm@mail.uc.edu"



def greedy(top, bottom):
    """Return a+abs(b), but without calling abs.

    >>> greedy(1, 2)
    1/2
    >>> greedy(11, 12)
    1/2 + 1/3 + 1/12
    >>> greedy(3, 4)
    1/2 + 1/4
    """
    out = ""
    frac = (top/bottom)
    a = 1
    while (frac > 0.0000001):
        if round(frac-(1/a), 10) >= 0.:
            frac -= (1/a)
            out += (" + 1/%s" % a)
        a += 1

        #print(frac)
    out = out[3:]
    print(out)


import doctest
if __name__ == "__main__":
    doctest.testmod(verbose=True)

    print(3*"\n")
    p = int(input("Give the Numerator for the fraction: "))
    q = int(input("Give the Denominator for the fraction: "))
    greedy(p,q)