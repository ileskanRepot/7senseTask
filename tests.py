import pytest
import numpy as np
from random import randrange, seed

from getObjectClose import getObjectsCloserThanWrapper


def setSeed(curSeed=randrange(0, int(1e8))):
    """! Set a seed for the function
    @param curSeed Optional parameter. If you want a random seed you can leave this blank
    """
    seed(curSeed)
    return curSeed


def test_noCloser():
    """! Test if works correctly when no objects are closer than the range"""
    print(setSeed())
    imageHeight = 10
    imageWidth = 15
    closerStreshHold = 2
    criticalStreshHold = 1

    depthMap = closerStreshHold + np.random.rand(imageHeight, imageWidth).flatten() * 10
    closer = getObjectsCloserThanWrapper(
        depthMap, closerStreshHold, criticalStreshHold, imageWidth, imageHeight
    )

    assert len(closer) == 0


def test_oneInRange():
    """! Test if works correctly when one object is closer than the range"""
    print(setSeed())
    imageHeight = 10
    imageWidth = 15
    closerStreshHold = 2
    criticalStreshHold = 1

    depthMap = closerStreshHold + np.random.rand(imageHeight, imageWidth).flatten() * 10

    xCoord = randrange(0, imageWidth)
    yCoord = randrange(0, imageHeight)
    depthMap[xCoord + imageWidth * yCoord] = (closerStreshHold + criticalStreshHold) / 2

    closer = getObjectsCloserThanWrapper(
        depthMap, closerStreshHold, criticalStreshHold, imageWidth, imageHeight
    )

    assert len(closer) == 1


def test_oneInCriticalRange():
    """! Test if works correctly when one object is closer than the critical range"""
    print(setSeed())
    imageHeight = 10
    imageWidth = 15
    closerStreshHold = 2
    criticalStreshHold = 1

    depthMap = closerStreshHold + np.random.rand(imageHeight, imageWidth).flatten() * 10

    xCoord = randrange(0, imageWidth)
    yCoord = randrange(0, imageHeight)
    depthMap[xCoord + imageWidth * yCoord] = criticalStreshHold / 2

    closer = getObjectsCloserThanWrapper(
        depthMap, closerStreshHold, criticalStreshHold, imageWidth, imageHeight
    )

    print(closer)
    assert closer == -1


def test_manyInRange():
    """! Test if works correctly when many objects are closer than the range"""
    print(setSeed())
    imageHeight = 10
    imageWidth = 15
    closerStreshHold = 2
    criticalStreshHold = 1

    depthMap = closerStreshHold + np.random.rand(imageHeight, imageWidth).flatten() * 10

    rang = randrange(0, imageWidth)
    for xCoord in range(rang):
        yCoord = randrange(0, imageHeight)
        depthMap[xCoord + imageWidth * yCoord] = (
            criticalStreshHold + closerStreshHold
        ) / 2

    closer = getObjectsCloserThanWrapper(
        depthMap, closerStreshHold, criticalStreshHold, imageWidth, imageHeight
    )

    assert len(closer) == rang
