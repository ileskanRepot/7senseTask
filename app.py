from time import time
import numpy as np
from sys import stderr

from getObjects import getObjectClose, ObjectTooCloseForComfort

IMAGE_WIDTH = 5
IMAGE_HEIGHT = 10

CRITICAL_RANGE = 1


def getObjectsCloserThanWrapper(
    numpyData: np.array,
    objectStreshold: float,
    criticalStreshold: float,
    width: int,
    height: int,
):
    """! Check if the numbers in the dataset are closer than specified range. Prints to stderr and return -1 if there are objects closer that specified crical range.

    @param numpyData         depthMap as numpy array
    @param objectStreshold   Streshold for elements to notify
    @param criticalStreshold Streshold for elements to notify
    @param width             width of the depthMap
    @param height            height of the depthMap
  
    @return Array of distances and positions of objects closer that objectStreshold. -1 if there are any objects in the critical range
    """
    try:
        test = np.array(
            getObjectClose(numpyData, objectStreshold, criticalStreshold, width, height)
        )
        return test
    except ObjectTooCloseForComfort as ee:
        print(f"\033[41m{ee}\033[0m", file=stderr)
        return -1


if __name__ == "__main__":
    tGen0 = time()
    depthMap = 0 + np.random.rand(IMAGE_HEIGHT, IMAGE_WIDTH).flatten() * 100
    print(depthMap)
    tGen1 = time()

    closerThan = 2.0
    closerThan = 2.0
    # print([ii for ii in depthMap if ii < closerThan])
    closerThan = 2.0
    # print([ii for ii in depthMap if ii < closerThan])
    tCPP0 = time()
    closer = getObjectsCloserThanWrapper(
        depthMap, closerThan, CRITICAL_RANGE, IMAGE_WIDTH, IMAGE_HEIGHT
    )
    tCPP1 = time()
    print(tGen1 - tGen0)
    print(tCPP1 - tCPP0)
    print(closer)
