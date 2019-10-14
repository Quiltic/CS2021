__author__ = "Josh Zack"
__email__ = "zackjm@mail.uc.edu"

"""The Game of Hog."""

from dice import four_sided, six_sided, make_test_dice

GOAL_SCORE = 100 # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################

def roll_dice(num_rolls, dice=six_sided):
    """ 
    >>> roll_dice(1,make_test_dice(4, 2, 1, 3))
    4
    >>> roll_dice(2,make_test_dice(4, 2, 1, 3))
    6
    >>> roll_dice(3,make_test_dice(4, 2, 1, 3))
    1
    >>> roll_dice(4,make_test_dice(4, 2, 1, 3))
    1
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN Question 1

    diceout = []
    pureout = 0
    for a in range(num_rolls):
        diceout.append(dice())
        if (pureout != 1):
            pureout += diceout[a]
        if (diceout[a] == 1):
            pureout = 1
    
    return(pureout)

    # END Question 1


def take_turn(num_rolls, opponent_score, dice=six_sided):
    """
    >>> take_turn(2, 0, make_test_dice(4, 6, 1))
    10
    >>> take_turn(3, 0, make_test_dice(4, 6, 1))
    1
    >>> take_turn(0, 35)
    6
    >>> take_turn(0, 71)
    8
    >>> take_turn(0, 7)
    8
    >>> take_turn(0, 0)
    1
    >>> take_turn(0, 9)
    10
    >>> take_turn(2, 0, make_test_dice(6))
    12
    >>> take_turn(0, 50)
    6
    """
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free bacon).

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function of no args that returns an integer outcome.
    """
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    # BEGIN Question 2
    if num_rolls != 0:
        return (roll_dice(num_rolls,dice))
    else:
        return (int(max(str(opponent_score)))+1)
    # END Question 2

def select_dice(score, opponent_score):
    """
    >>> select_dice(4, 24) == four_sided
    True
    >>> select_dice(16, 64) == four_sided
    False
    >>> select_dice(0, 0) == four_sided
    True
    >>> select_dice(50, 80) == four_sided
    False
    """

    """Select six-sided dice unless the sum of SCORE and OPPONENT_SCORE is a
    multiple of 7, in which case select four-sided dice (Hog wild).
    """
    # BEGIN Question 3
    if ((score+opponent_score) % 7 == 0):
        return (four_sided)
    return (six_sided)
    # END Question 3

def is_swap(score0, score1):
    """
    >>> is_swap(19, 91)
    True
    >>> is_swap(20, 40)
    False
    >>> is_swap(41, 14)
    True
    >>> is_swap(23, 42)
    False
    >>> is_swap(55, 55)
    True
    >>> is_swap(114, 41) # We check the last two digits
    True
    """
    """Return True if ending a turn with SCORE0 and SCORE1 will result in a
    swap.

    Swaps occur when the last two digits of the first score are the reverse
    of the last two digits of the second score.
    """
    # BEGIN Question 4
    score0 = str(score0)
    score1 = str(score1)
    
    #make them the same len
    while len(score0) < 3:
        score0 = '0'+ score0
        #print(score0)
    while len(score1) < 3:
        score1 = '0'+ score1
        #print(score1)

    if (score0[2] == score1[1]):
        if (score0[1] == score1[2]): 
            return (True) #swap
    return (False) #dont swap
    # END Question 4


def other(who):
    """Return the other player, for a player WHO numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - who

#'''
def play(strategy0, strategy1, score0=0, score1=0, goal=GOAL_SCORE):
    """
    >>> four_sided = make_test_dice(1)
    >>> six_sided = make_test_dice(3)
    >>> always = always_roll
    >>> s0, s1 = play(always(5), always(3), score0=91, score1=10)
    >>> s0, s1
    (106, 10)
    >>> s0, s1 = play(always(5), always(5), goal=10)
    >>> s0, s1
    (1, 15)
    >>> s0, s1 = play(always(5), always(3), score0=36, score1=15, goal=50)
    >>> s0, s1
    (15, 51)
    >>> # Swine swap applies to 3 digit scores
    >>> s0, s1 = play(always(5), always(3), score0=98, score1=31)
    >>> s0, s1
    (31, 113)
    >>> # Goal edge case
    >>> s0, s1 = play(always(4), always(3), score0=88, score1=20)
    >>> s0, s1
    (100, 20)
    """
    """Simulate a game and return the final scores of both players, with
    Player 0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first
    strategy1:  The strategy function for Player 1, who plays second
    score0   :  The starting score for Player 0
    score1   :  The starting score for Player 1
    """
    who = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
    # BEGIN Question 5
    while (score1 < goal) and (score0 < goal):
        #print("Player %s's Turn" % (who))
        #print(score0,score1)
        #dice = input("How many dice do you want to roll?: ")
        if who == 0:
            dice = strategy0(score0,score1) #number of dice to roll
            #print(take_turn(dice,score1,select_dice(score0,score1)))
            score0 += take_turn(dice,score1,select_dice(score0,score1)) #hog wild
        elif who == 1:
            dice = strategy1(score1,score0) #number of dice to roll
            score1 += take_turn(dice,score0,select_dice(score0,score1))
        
        #Swine Swap
        if is_swap(score0,score1):
            score0, score1 = (score1, score0)
        
        #other persons turn
        who = other(who)

        

    # END Question 5
    return score0, score1

#'''
def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n
    return strategy


import doctest
if __name__ == "__main__":
    #Docktests always fail without this because the origional fair dice overide it
    four_sided = make_test_dice(1)
    six_sided = make_test_dice(3)
    doctest.testmod(verbose=False)

    #fix the dice from the doctest problem
    from dice import four_sided, six_sided
