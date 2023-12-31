#유틸리티 함수 선언
from functools import *

def intersect(*ar): #*이 있으면 Tuple
    return reduce(__intersectSC,ar)

def __intersectSC(listX, listY): #__숨김
    setList = []
    for x in listX:
        if x in listY:
            setList.append(x)
    return setList

def difference(*ar):
    setList = []
    intersectSet = intersect(*ar)
    unionSet = union(*ar)
    for x in unionSet:
        if not x in intersectSet:
            setList.append(x)
    return setList

def union(*ar):
    setList = []
    for item in ar:
        for x in item:
            if not x in setList:
                setList.append(x)
    return setList


