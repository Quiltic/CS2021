def fib(n):
    """
    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(10)
    55
    """

    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return(a)

import doctest
if __name__ == "__main__":
    doctest.testmod(verbose=True)