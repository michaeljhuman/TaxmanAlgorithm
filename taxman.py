import logging
import math
from math import sqrt, floor
from operator import itemgetter, attrgetter

logging.basicConfig( filename='tm.log', level=logging.INFO)

# Return all the factors of x, that at in theList
def factors( x, theList):
    fctrs=[]
    for i in theList[::-1]:
        if i >= x:
            continue
        if x % i == 0:
            fctrs.append( i)
    return fctrs

# Remove all the elements in removeList from theList
def remove( theList, removeList):
    for i in removeList:
        theList.remove( i)

def computeScore( myChoices, tmTakes):
    s=0
    for i in myChoices:
        s+=i
    for i in tmTakes:
        s-=i
    return s

# This assumes theList has a largest prime
def largestPrime( theList):
    for i in theList[::-1]:
        fctrs=factors( i, theList)
        print( fctrs)
        if len( fctrs) == 1:
            return i
    raise 'Bad input'

# Simply choose the largest number left, with a single factor
def tm1( theList):
    for i in theList[::-1]:
        fctrs=factors( i, theList)
        if len( fctrs) == 0:
            continue
        if len( fctrs) == 1:
            return i
    return 0

# Returns a number, if choosing i would remove all the factors for that number
# candidate is the candidate choice
# candidateFctr is the single factor for the candidate
# factorList is the factors the number greater than i
def tm2DetectPoorMove( candidate, candidateFctr, factorList):
    for factorListElem in factorList.items():
        (i, iFctrs) = factorListElem
        if len( iFctrs) != 2:
            continue
        count=0
        for fctr in iFctrs:
            if fctr == candidate or fctr == candidateFctr:
                count += 1
        if count == 2:
            # Choosing candidate is a worse choise than choosing i
            # Therefore, return i
            return i
    return 0

def tm2( theList):
    savedFactorDict = {}
    for i in theList[::-1]:
        fctrs=factors( i, theList)
        if len( fctrs) == 0:
            continue
        if len( fctrs) == 1:
            betterChoice = tm2DetectPoorMove( i, fctrs[0], savedFactorDict)
            # We will return i, unless it's a bad choice per tm2DetectPoorMove
            if betterChoice != 0:
                return betterChoice
            else:
                return i
        savedFactorDict[i] = fctrs
    return 0

def tm3( theList):
    candidateList = []
    for i in theList[::-1]:
        fctrs=factors( i, theList)
        diff=i
        for j in fctrs:
            diff-=j
        if len( fctrs) > 0:
            candidateList.append( (diff, len( fctrs), i, fctrs))
        # Sort by diff (descending), factor count ( ascending),
        # i ( descending)
        candidateList=sorted( candidateList,
            key=lambda item: ( -item[0], item[1], -item[2]))
    if len( candidateList) == 0:
        return 0
    else:
        #logging.debug( 'candidateList: ', candidateList)
        return candidateList[0][2]

def tm4recurse( theList, depth):
    scores=[]
    for i in theList[::-1]:
        tempList=theList.copy()
        fctrs=factors( i, tempList)
        if len( fctrs) < 1:
            continue
        tempList.remove( i)
        remove( tempList, fctrs)
        score=i - sum( fctrs)
        myChoices=[i]
        #print( 'here', tm4recurse( tempList, depth+1))
        ( tempScore, myChoicesTemp)=tm4recurse( tempList, depth+1)
        if len( myChoicesTemp) == 0:
            # No choices left, so subtract everything in tempList from the score
            scores.append( ( score - sum(tempList), [i]))
            continue
        myChoices.extend( myChoicesTemp)
        scores.append( (score + tempScore, myChoices))
    scores=sorted( scores, key=itemgetter(0), reverse=True)
    if len( scores) == 0:
        return( 0, [])
    else:
        if depth == 0:
            logging.info( 'scores: %s', scores)
        return( scores[0][0], scores[0][1])

def tm4( theList):
    # If 1 is left, than choose the highest prime
    if theList[0] == 1:
        print('Here')
        print( largestPrime( theList))
        return largestPrime( theList)
    ( score, myChoices)=tm4recurse( theList, 0)
    if len( myChoices) == 0:
        return 0
    else:
        return myChoices[0]

def runIt( name, n, alg):
    logging.info( 'alg: %s; n: %d', name, n)
    print( 'Algorithm: %s; n: %d' % ( name, n))
    theList=list( range( 1, n+1))
    myChoices=[]
    tmTakes=[]
    while True:
        myChoice=alg( theList)
        if myChoice == 0:
            break
        logging.info( 'myChoice: %s', myChoice)
        myChoices.append( myChoice)
        print( 'myChoice: ', myChoice)
        theList.remove( myChoice)
        tmTakesTemp=factors( myChoice, theList)
        logging.info( 'tmTakes: %s', tmTakesTemp)
        remove( theList, tmTakesTemp)
        tmTakes.extend( tmTakesTemp)

    tmTakes.extend( theList)

    print( 'Player took: ', myChoices)
    print( 'Taxman took: ', tmTakes)
    print( 'MyScore: %d; Taxman: %d; Differences: %d'
        % ( sum( myChoices), sum( tmTakes), computeScore( myChoices, tmTakes)))
    print('')

n=28

runIt( 'tm1', n, tm1)
runIt( 'tm2', n, tm2)
runIt( 'tm3', n, tm3)
runIt( 'tm4', n, tm4)


