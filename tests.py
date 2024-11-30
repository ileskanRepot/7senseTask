import pytest
import numpy as np
from random import randrange, seed

from app import getObjectsCloserThan

def setSeed(curSeed = randrange(0,int(1E8))):
	seed(curSeed)
	return curSeed

def test_noCloser():
	print(setSeed())
	imageHeight = 10
	imageWidth = 15
	closerStreshHold = 2
	criticalStreshHold = 1

	depthMap = closerStreshHold+np.random.rand(imageHeight, imageWidth).flatten()* 10
	closer = getObjectsCloserThan(depthMap, closerStreshHold, criticalStreshHold, imageWidth, imageHeight)

	assert len(closer) == 0

def test_oneInRange():
	print(setSeed())
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
	print(setSeed())
	imageHeight = 10
	imageWidth = 15
	closerStreshHold = 2
	criticalStreshHold = 1

	depthMap = closerStreshHold+np.random.rand(imageHeight, imageWidth).flatten()* 10

	xCoord = randrange(0,imageWidth)
	yCoord = randrange(0,imageHeight)
	depthMap[xCoord + imageWidth*yCoord] = criticalStreshHold / 2

	closer = getObjectsCloserThan(depthMap, closerStreshHold, criticalStreshHold, imageWidth, imageHeight)

	print(closer)
	assert closer == -1

def test_manyInRange():
	print(setSeed())
	imageHeight = 10
	imageWidth = 15
	closerStreshHold = 2
	criticalStreshHold = 1

	depthMap = closerStreshHold+np.random.rand(imageHeight, imageWidth).flatten()* 10

	rang = randrange(0,imageWidth)
	for xCoord in range(rang):
		yCoord = randrange(0,imageHeight)
		depthMap[xCoord + imageWidth*yCoord] = (criticalStreshHold + closerStreshHold) / 2

	closer = getObjectsCloserThan(depthMap, closerStreshHold, criticalStreshHold, imageWidth, imageHeight)

	assert len(closer) == rang
