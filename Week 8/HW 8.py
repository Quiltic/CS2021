__author__ = "Josh Zack"
__email__ = "zackjm@mail.uc.edu"

"""
Write a function cleanlinks(L) that returns the smallest list obtained by repeatedly applying the clean up rule, which when applied to a linked list removes any consecutive sub list with attributes sum to zero, to the linked list L.

For example,
"""
def cleanlinks(l):
    """
    >>> r = cleanlinks(link(5, link(0, link(3, link(-2, link(-1, link(-5, link(2))))))))
    >>> r
    [2, 'empty']

    >>> r = cleanlinks(link(1, link(2, link(-2, link(-1, link(-5, link(2, link(5))))))))
    >>> r
    [-5, [2, [5, 'empty']]]

    >>> r = cleanlinks(link(1, link(2, link(-2, link(-1, link(-5, link(2, link(5, link(5, link(0, link(3, link(-2, link(-1, link(-5, link(2)))))))))))))))
    >>> r
    [-5, [2, [5, [2, 'empty']]]]

    >>> r = cleanlinks(link(1,link(0,link(1,link(-1)))))
    >>> r
    [1, 'empty']
    """
    
    part = getFirst(l)
    total = getFirst(l)
    copy = getRest(l)
    if copy == 'empty':
        return(l)
    #print(l)
    while (copy != 'empty'):
        if total == 0:
            l = copy
            break
        total += getFirst(copy)
        copy = getRest(copy)
    else:
        return(link(part,cleanlinks(getRest(l))))
    #print(total)
    if part:
        return(cleanlinks(l))
    return('empty')
    #print(part)
    #return(link(part,cleanlinks(getRest(l))))

    """
    rest = getRest(l)
    if rest != 'empty':
        part = cleanlinks(rest)
    total = getFirst(l)
    copy = getRest(l)
    while (copy != 'empty'):
        if total == 0:
            part = copy
            break
        total += getFirst(copy)
        copy = getRest(copy)
    else:
        if total:
            part = l
    print(l,total,part)
    """
    return(part)
    


def link(first,rest = 'empty'):
    #print([first,rest])
    return([first,rest])

def getFirst(l):
    return(l[0])

def getRest(l):
    #print(l)
    if len(l) > 1:
        return(l[1])
    return('empty')

def size(l):
    n = 0
    while getRest(l) != 'empty':
        l = getRest(l)
        n += 1
    return(n)


import doctest
if __name__ == "__main__":
    #r = link(1, link(2, link(-2, link(-1, link(-5, link(2, link(5, link(5, link(0, link(3, link(-2, link(-1, link(-5, link(2))))))))))))))
    #print('asddsadsa   ',cleanlinks(r))
    #print(cleanlinks(link(1,link(0,link(1,link(-1))))))
    doctest.testmod(verbose=True)

"""
N.B. This was an Amazon interview question.


Hints:  One approach to this problem is the following:

0) stick to the abstraction provided by the linked list ADT (link, first, rest)
1)  write a function to  clean the front part of the list which has a prefix that sums to 0
2)  write function to split the linked list at any index point k between 1 and length -1
3)  apply the clean front part to both sublists and join the reduce lists back together
4)  apply cleaning for each value of k  between 1 and length -1
5) repeat as necessary until done.
6) writing helper functions will be useful. 
"""
