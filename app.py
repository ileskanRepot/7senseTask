from time import time
import numpy as np
from sys import stderr

from example import addVec, ObjectTooCloseForComfort, __str__

IMAGE_WIDTH = 5
IMAGE_HEIGHT = 10

CRITICAL_RANGE = 1

def getObjectsCloserThan(numpyData:np.array, objectStreshold:float, criticalStreshold:float, width:int, height:int):
	try:
		test = np.array(addVec(numpyData, objectStreshold, criticalStreshold, width, height))
		return test
	except ObjectTooCloseForComfort as ee:
		print(f"\033[41m{ee}\033[0m",file=stderr)
		return -1

if __name__ == "__main__":
	tGen0 = time()
	depthMap = 0+np.random.rand(IMAGE_HEIGHT, IMAGE_WIDTH).flatten() * 100
	print(depthMap)
	tGen1 = time()

	closerThan = 2.0
	# print([ii for ii in depthMap if ii < closerThan])
	tCPP0 = time()
	closer = getObjectsCloserThan(depthMap, closerThan, CRITICAL_RANGE, IMAGE_WIDTH, IMAGE_HEIGHT)
	tCPP1 = time()
	print(tGen1-tGen0)
	print(tCPP1-tCPP0)
	print(closer)
