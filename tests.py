import pytest
import numpy as np
from random import randrange, seed

from app import getObjectsCloserThan

def test_noCloser():
	imageHeight = 10
	imageWidth = 15
	closerStreshHold = 2
	criticalStreshHold = 1

	depthMap = closerStreshHold+np.random.rand(imageHeight, imageWidth).flatten()* 10
	closer = getObjectsCloserThan(depthMap, closerStreshHold, criticalStreshHold, imageWidth, imageHeight)

	assert len(closer) == 0

def test_oneInRange():
	imageHeight = 10
	imageWidth = 15
	closerStreshHold = 2
	criticalStreshHold = 1

	depthMap = closerStreshHold+np.random.rand(imageHeight, imageWidth).flatten()* 10

	xCoord = randrange(0,imageWidth)
	yCoord = randrange(0,imageHeight)
	depthMap[xCoord + imageWidth*yCoord] = (closerStreshHold + criticalStreshHold) / 2

	closer = getObjectsCloserThan(depthMap, closerStreshHold, criticalStreshHold, imageWidth, imageHeight)

	assert len(closer) == 1

def test_oneInCriticalRange():
	imageHeight = 10
	imageWidth = 15
	closerStreshHold = 2
	criticalStreshHold = 1

	depthMap = closerStreshHold+np.random.rand(imageHeight, imageWidth).flatten()* 10

	xCoord = randrange(0,imageWidth)
	yCoord = randrange(0,imageHeight)
	depthMap[xCoord + imageWidth*yCoord] = criticalStreshHold / 2

	closer = getObjectsCloserThan(depthMap, closerStreshHold, criticalStreshHold, imageWidth, imageHeight)

	assert closer == -1

