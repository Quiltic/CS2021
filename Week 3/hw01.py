
__author__ = "Josh Zack"
__email__ = "zackjm@mail.uc.edu"



def greedy(top, bottom):
    """Return a+abs(b), but without calling abs.

    >>> greedy(1, 2)
    '1/2'
    >>> greedy(11, 12)
    '1/2 + 1/3 + 1/12'
    >>> greedy(3, 4)
    '1/2 + 1/4'
    """
    out = "" # what the file will output
    frac = (top/bottom) # the fraction turned into decimal
    a = 1 
    while (frac > 0.0000001): # to make it stop when it gets too small

        if round(frac-(1/a), 10) >= 0: # make sure it isent going over
            frac -= (1/a) # remove the amount
            out += (" + 1/%s" % a) # add it to the output

        a += 1

    out = out[3:] # remove the " + " from the begining
    return(out)


import doctest
if __name__ == "__main__":
    doctest.testmod(verbose=True)

    print(3*"\n") # 3 new lines
    p = int(input("Give the Numerator for the fraction: "))
    q = int(input("Give the Denominator for the fraction: "))
    print(greedy(p,q))