__author__ = "Josh Zack"
__email__ = "zackjm@mail.uc.edu"

#############
# Iterators #
#############

#RQ1
class Cheer:
    """
    >>> UC = Cheer("Bearcats")
    >>> for c in UC:
    ...     print(c)
    ...
    Give me an B
    Give me an e
    Give me an a
    Give me an r
    Give me an c
    Give me an a
    Give me an t
    Give me an s
    >>> for c in UC:    # a standard iterator does not restart
    ...     print(char)
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, stuff):
        self.words = stuff
        self.point = 0
    
    def __iter__(self):
        return(self)

    def __next__(self):
        if self.point >= len(self.words):
            raise StopIteration
        letter = self.words[self.point]
        self.point += 1
        return("Give me an "+ letter)



#RQ2
class Countdown:
    """
    An iterator that counts down from N to 0.
    >>> for number in Countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    >>> for number in Countdown(2):
    ...     print(number)
    ...
    2
    1
    0
    """
    
    "*** YOUR CODE HERE ***"

    def __init__(self, stuff):
        self.start = stuff
        self.point = stuff
    
    def __iter__(self):
        return(self)

    def __next__(self):
        if self.point < 0:
            raise StopIteration
        self.point -= 1
        return(self.point+1)



##############
# Generators #
##############

# RQ3
def naturals():
    """A generator function that yields the infinite sequence of natural
    numbers, starting at 1.

    >>> m = naturals()
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    "*** YOUR CODE HERE ***"
    a = 1
    while True:
        yield a
        a += 1


#RQ4
def scale(s, k):
    """Yield elements of the iterable s scaled by a number k.

    >>> s = scale([1, 5, 2], 5)
    >>> type(s)
    <class 'generator'>
    >>> list(s)
    [5, 25, 10]

    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    "*** YOUR CODE HERE ***"
    point = 0
    for a in s:
        yield a*k
        point += 1


# RQ5
def countdown(n):
    """
    A generator that counts down from N to 0.
    >>> for number in countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    >>> for number in countdown(2):
    ...     print(number)
    ...
    2
    1
    0
    """
    "*** YOUR CODE HERE ***"
    point = n
    while point >= 0:
        yield point
        point -= 1


# RQ6
def hailstone(n):
    """
    Pick a positive integer n as the start.
    If n is even, divide it by 2.
    If n is odd, multiply it by 3 and add 1.
    Continue this process until n is 1.
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"
    point = n
    while point > 1:
        yield int(point)
        if point%2 == 0:
            point /= 2
        else:
            point = point*3 + 1

    yield int(point)

#'''

import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=False)