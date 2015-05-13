import matplotlib.pyplot
from numpy import *
from meshtool.filters.print_filters.print_bounds import getBoundsInfo
import collada
import math
from array import array

folder = '/Gustavo/Desktop/3dmodel'
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

trilist[0]
triset.vertex[triset.vertex_index][0]

taylor = getBoundsInfo(mesh)

print taylor['bounds']










































