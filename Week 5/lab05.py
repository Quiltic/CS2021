__author__ = "Josh Zack"
__email__ = "zackjm@mail.uc.edu"

## Lab 5: Required Questions - Dictionaries Questions ##

# RQ1
def merge(dict1, dict2):
    """Merges two Dictionaries. Returns a new dictionary that combines both. You may assume all keys are unique.

    >>> merge({1: 'one', 3:'three', 5:'five'}, {2: 'two', 4: 'four'})
    {1: 'one', 3: 'three', 5: 'five', 2: 'two', 4: 'four'}
    """
    "*** YOUR CODE HERE ***"
    newdic = {}
    '''
    for a in range(len(dict1)+len(dict2)):
        try:
            newdic[a+1] = dict1[a+1]
        except:
            newdic[a+1] = dict2[a+1]
    '''
    for a in dict1:
        newdic[a] = dict1[a]

    for a in dict2:
        newdic[a] = dict2[a]
    #'''

    return(newdic)


# RQ2
def counter(message):
    """ Returns a dictionary of each word in message mapped
    to the number of times it appears in the input string.
    >>> x = counter('to be or not to be')
    >>> x['to']
    2
    >>> x['be']
    2
    >>> x['not']
    1
    >>> y = counter('run forrest run')
    >>> y['run']
    2
    >>> y['forrest']
    1
    """
    "*** YOUR CODE HERE ***"
    
    wordListing = {}

    working = True
    while working:
        try:
            word = message[:message.index(' ')]
            message = message[message.index(' ')+1:]
        except:
            word = message.replace('\n', '')
            working = False
        try:
            wordListing[word] += 1
        except:
            wordListing[word] = 1
    
    return(wordListing)

# RQ3
def replace_all(d, x, y):
    """
    >>> d = {'foo': 2, 'bar': 3, 'garply': 3, 'xyzzy': 99}
    >>> replace_all(d, 3, 'poof')
    >>> d == {'foo': 2, 'bar': 'poof', 'garply': 'poof', 'xyzzy': 99}
    True
    """
    "*** YOUR CODE HERE ***"
    for a in d:
        if d[a] == x:
            d[a] = y
        
    #return(d)


# RQ4
def sumdicts(lst):
    """ 
    Takes a list of dictionaries and returns a single dictionary which contains all the keys value pairs. And 
    if the same key appears in more than one dictionary, then the sum of values in list of dictionaries is returned 
    as the value for that key
    >>> d = sumdicts ([{'a': 5, 'b': 10, 'c': 90, 'd': 19}, {'a': 45, 'b': 78}, {'a': 90, 'c': 10}] )
    >>> d == {'a': 140, 'b': 88, 'c': 100, 'd': 19}
    True
    """
    "*** YOUR CODE HERE ***"

    newdic = {}
    for dic in lst:
        for a in dic:
            try:
                newdic[a] += dic[a]
            except:
                newdic[a] = dic[a]
    return(newdic)
    

#RQ5
from Shake import *
def middle_tweet(word, table):
    """ Calls the function random_tweet() 5 times (see Interactive Worksheet) and returns the one string that is of length right in middle of the 5.
    Returns a string that is a random sentence of average length starting with word, and choosing successors from table.
    """
    "*** YOUR CODE HERE ***"
    import random
    average = 0
    for _ in range(5):
        average += len(random_tweet(table))
    
    average /= 5
    result = ''

    while len(result) != int(average):
        result = construct_tweet(word,table)
    return(result)
    

import doctest
if __name__ == "__main__":
    doctest.testmod(verbose=True)

    shakestokens = shakespeare_tokens()
    shakestable = build_successors_table(shakestokens)
    result = middle_tweet("We",shakestable)
    print(result,'\n',"Length of tweet:",len(result))
    