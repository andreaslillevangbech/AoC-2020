import sys, numpy, scipy.ndimage
D = 4

cube = numpy.array([[c == "#" for c in line[:-1]] for line in sys.stdin])
cube = numpy.expand_dims(cube, axis=tuple(range(D - 2)))
N = numpy.ones(shape=(3,) * D)
N[(1,) * D] = 0

for _ in range(6):
    cube = numpy.pad(cube, 1).astype(int)
    cnt = scipy.ndimage.convolve(cube, N, mode="constant", cval=0)
    cube = (cube == 1) & ((cnt == 2) | (cnt == 3)) | (cube == 0) & (cnt == 3)

print(numpy.sum(cube))
