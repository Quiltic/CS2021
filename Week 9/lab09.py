__author__ = "Josh Zack"
__email__ = "zackjm@mail.uc.edu"

"""
Lab 09 - Required Questions
"""

def reverse(link):
    """Returns a Link that is the reverse of )
    the original.

    >>> print_link(reverse(Link(1)))
    <1>
    >>> link = Link(1, Link(2, Link(3)))
    >>> new = reverse(link)
    >>> print_link(new)
    <3 2 1>
    >>> print_link(link)
    <1 2 3>
    """
    "*** YOUR CODE HERE ***"
    r = Link.empty
    while link != Link.empty:
      r = Link(link.first,r)
      link = link.rest
    
    return(r)
    

#'''

def add_links(link1, link2):
    """Adds two Links, returning a new Link

    >>> l1 = Link(1, Link(2))  
    >>> l2 = Link(3, Link(4, Link(5)))
    >>> new = add_links(l1,l2)
    >>> print_link(new)
    <1 2 3 4 5>
    """
    "*** YOUR CODE HERE ***"
    link1 = reverse(link1)
    link2 = reverse(link2)
    
    r = Link.empty

    while link2 != Link.empty:
      r = Link(link2.first,r)
      link2 = link2.rest

    while link1 != Link.empty:
      r = Link(link1.first,r)
      link1 = link1.rest
    
    return(r)





def slice_link(link, start, end):
    """Slices a Link from start to end (as with a normal Python list).

    >>> link = Link(3, Link(1, Link(4, Link(1, Link(5, Link(9))))))
    >>> new = slice_link(link, 1, 4)
    >>> print_link(new)
    <1 4 1>
    """
    "*** YOUR CODE HERE ***"

    for _ in range(start):
      link = link.rest
    
    begin = link

    nextta = begin.rest #because of this line the thing below needs to be -2
    for _ in range(end-2-start):
      nextta = nextta.rest

    nextta.rest = Link.empty

    """
    #begin = Link.empty
    while link.first != start:
      link = link.rest
    begin = link

    nextta = begin.rest
    while nextta.first != end:
      nextta = nextta.rest

    nextta = nextta.rest
    nextta.rest = Link.empty
    """
    return(begin)
    


# Linked List Class
class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

def print_link(link):
    """Print elements of a linked list link.

    >>> link = Link(1, Link(2, Link(3)))
    >>> print_link(link)
    <1 2 3>
    >>> link1 = Link(1, Link(Link(2), Link(3)))
    >>> print_link(link1)
    <1 <2> 3>
    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> print_link(link1)
    <3 <4> 5 6>
    """
    print('<' +helper(link).rstrip() +'>')



def helper(link):
    if link == Link.empty:
        return ''
    elif isinstance(link.first, Link):
        return '<' +helper(link.first).rstrip() + '> '+ helper(link.rest)
    else:
        return str(link.first) +' '+  helper(link.rest)

def rep_link(link):
  """  Modified print_link to return string  """
  return('<' +helper(link).rstrip() +'>')

def mygetitem(s, i):
  #gets item at i from list s
  if isinstance(i,slice):
    return slice_link(s, i.start, i.stop)

  for _ in range(i):
    s = s.rest
  return(s.first)
  

def mysetitem(s, i, item):
  #sets item at i from list s
  for _ in range(i):
    s = s.rest

  s.first = item


Link.__repr__ = rep_link
Link.__neg__ = reverse
Link.__add__ = add_links 
Link.__getitem__ = mygetitem # write to return Link item 
Link.__setitem__ = mysetitem # write to set Link item   

#'''
def magic_test():
  """
  >>> s = Link(3, Link(1, Link(4, Link(1, Link(5, Link(9))))))
  >>> s
  <3 1 4 1 5 9>
  >>> -s
  <9 5 1 4 1 3>
  >>> --s
  <3 1 4 1 5 9>
  >>> s[0]=30
  >>> s
  <30 1 4 1 5 9>
  >>> s+s
  <30 1 4 1 5 9 30 1 4 1 5 9>
  >>> s[1:3]
  <1 4>
  """
  import doctest
  doctest.testmod(verbose=False)
    
#'''
#import doctest
if __name__ == "__main__":
  #doctest.testmod(verbose=False)
  magic_test()
  


"""
You should modify mygetitem to handle slice types as follows...
  def mygetitem(s, i):
        if isinstance(i,slice):
            return slice__link(s, i.start, i.stop)...
"""