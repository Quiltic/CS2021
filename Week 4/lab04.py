__author__ = "Josh Zack"
__email__ = "zackjm@mail.uc.edu"

##Lab04 Required Questions ##

#########
# Lists #
#########

# RQ1
def cascade(lst):
    """Returns the cascade of the given list.

    >>> cascade([1, 2, 3, 4])
    [1, 2, 3, 4, 4, 3, 2, 1]
    """
    "*** YOUR CODE HERE ***"
    l = list(lst)
    l.reverse()
    return(flatten([lst,l]))



# RQ2
def maptwice(fn, seq):
    """Applies fn twice onto each element in seq and returns the resulting list.

    >>> maptwice(lambda x: x*x, [1, 2, 3])
    [1, 16, 81]
    """
    "*** YOUR CODE HERE ***"
    out = []
    for a in seq:
        out.append(fn(a)*fn(a))
    return(out)



#RQ3
def filterout(pred, seq):
    """Keeps elements in seq only if they satisfy pred.

    >>> filterout(lambda x: x % 2 == 0, [1, 2, 3, 4])
    [1, 3]
    """
    "*** YOUR CODE HERE ***"
    out = []
    for a in seq:
        if not pred(a):
            out.append(a)
    return(out)


#RQ4
def comp(n, pred):
    """ Uses a one line list comprehension to return list of the first n integers (0...n-1) which satisfy the predicate pred.
    >>> comp(7, lambda x: x%2 ==0)
    [0, 2, 4, 6]
    """
    "*** YOUR CODE HERE ***"
    #print(pred)
    return(list(a for a in range(n) if pred(a)))


#RQ5
def flatten(lst):
    """ Takes a nested list and "flattens" it.
    
    >>> flatten([1, 2, 3]) 
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] 
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    >>> lst = [1, [[2], 3], 4, [5, 6]]
    >>> flatten(lst)
    [1, 2, 3, 4, 5, 6]
    """
    "*** YOUR CODE HERE ***"
    out = []
    for a in lst:
        if type(a) == list:
            a = flatten(a)
            for b in a:
                out.append(b)
        else:
            out.append(a)
    return(out)


import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)