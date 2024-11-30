from time import time

import numpy as np

IMAGE_WIDTH = 101
IMAGE_HEIGHT = 101
IMAGE_DEPTH = 101

# in cm
threeDworld = np.zeros((IMAGE_HEIGHT, IMAGE_WIDTH, IMAGE_DEPTH), dtype=np.float64)

threeDworld[10:31,20:41,10:31] = 1
threeDworld[70:91,20:41,70:91] = 1


def trace(startingPoint, dir, cameraPos, threeDworld):
	ii = 0
	while ii < 10000:
		xx = int(cameraPos[0] + dir[0]*ii)
		yy = int(cameraPos[1] + dir[1]*ii)
		zz = int(cameraPos[2] + dir[2]*ii)
		if (xx>=len(threeDworld[0]) or xx<0) or (yy>=len(threeDworld[1]) or yy<0) or (zz>=len(threeDworld[2]) or zz<0):
			return 0
		if threeDworld[xx , yy, zz] == 1:
			return ii
		ii+=1

def dispArrNums(dephtMat):
	for ii in range(len(dephtMat)):
		for jj in range(len(dephtMat[0])):
			print(f"{3*dephtMat[ii,jj]:03}",end=" ")
		print()

def dispDepthArr(dephtMat):
	char = "  "
	flatted = dephtMat.flatten()
	minCol = np.min(flatted[flatted!=0])
	maxCol = np.max(dephtMat)
	print(minCol, maxCol)
	for ii in range(len(dephtMat)):
		for jj in range(len(dephtMat[0])):
			if dephtMat[ii,jj] == 0:
				print(f"\033[48;2;{0};{0};{0}m{char}",end=" ")
			else:
				col = int(256*(minCol-dephtMat[ii,jj])/(maxCol-minCol))
				print(f"\033[48;2;{col};{col};{col}m{char}",end=" ")
		print()

end = 100
dephtMat = np.zeros((end+1, end+1), dtype=np.int32)
cameraPos = (50,0,50)
for jj in range(0,end+1):
	for ii in range(0,end+1):
		dire = np.array((np.cos(np.pi*ii/end), np.sin(np.pi*ii/end), np.cos(np.pi*jj/end)))
		le = np.sqrt(sum(dire**2))
		dire = dire/le
		# print(sum(dire**2))
		ret = trace(cameraPos, dire, cameraPos, threeDworld)
		dephtMat[jj,ii] = ret
		# print(dire)
		# print(f"{ret:02}", end=" ")
		# print(t1 - t0)

	# print()
if (cols := 0):
	dispArrNums(dephtMat)
else:
	dispDepthArr(dephtMat)
