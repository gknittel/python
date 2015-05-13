import matplotlib.pyplot
from numpy import *
import collada
import math
from array import array

folder = '/home/gustavo/3dmodels/'
filename = 'subsea_remeshed.dae'

mesh = collada.Collada(folder + filename)

f = open(folder + filename)
mesh = collada.Collada(f)

geom = mesh.geometries[0]
geom.primitives

triset = geom.primitives[0]
trilist = list(triset)
len(trilist)
print len(triset.vertex)














































