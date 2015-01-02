import numpy as np
import ctypes
from ctypes import cdll
dc3d0 = cdll.LoadLibrary("/usr/lib/dc3d0.so")
@np.vectorize
def ux(alpha, x, y, z, depth, dip, pot1, pot2, pot3, pot4):
  alpha = ctypes.c_float(alpha)
  x = ctypes.c_float(x)
  y = ctypes.c_float(y)   
  z = ctypes.c_float(z)   
  depth = ctypes.c_float(depth)
  dip = ctypes.c_float(dip)
  pot1 = ctypes.c_float(pot1) 
  pot2 = ctypes.c_float(pot2)
  pot3 = ctypes.c_float(pot3)
  pot4 = ctypes.c_float(pot4)
  dc3d0.ux.restype = ctypes.c_float
  return  dc3d0.ux(alpha, x, y, z, depth, dip, pot1, pot2, pot3, pot4)
@np.vectorize
def uy(alpha, x, y, z, depth, dip, pot1, pot2, pot3, pot4):
  alpha = ctypes.c_float(alpha)
  x = ctypes.c_float(x)
  y = ctypes.c_float(y)   
  z = ctypes.c_float(z)   
  depth = ctypes.c_float(depth)
  dip = ctypes.c_float(dip)
  pot1 = ctypes.c_float(pot1) 
  pot2 = ctypes.c_float(pot2)
  pot3 = ctypes.c_float(pot3)
  pot4 = ctypes.c_float(pot4)
  dc3d0.uy.restype = ctypes.c_float
  return  dc3d0.uy(alpha, x, y, z, depth, dip, pot1, pot2, pot3, pot4)
@np.vectorize
def uz(alpha, x, y, z, depth, dip, pot1, pot2, pot3, pot4):
  alpha = ctypes.c_float(alpha)
  x = ctypes.c_float(x)
  y = ctypes.c_float(y)   
  z = ctypes.c_float(z)   
  depth = ctypes.c_float(depth)
  dip = ctypes.c_float(dip)
  pot1 = ctypes.c_float(pot1) 
  pot2 = ctypes.c_float(pot2)
  pot3 = ctypes.c_float(pot3)
  pot4 = ctypes.c_float(pot4)
  dc3d0.uz.restype = ctypes.c_float
  return  dc3d0.uz(alpha, x, y, z, depth, dip, pot1, pot2, pot3, pot4)
@np.vectorize
def iret(alpha, x, y, z, depth, dip, pot1, pot2, pot3, pot4):
  alpha = ctypes.c_float(alpha)
  x = ctypes.c_float(x)
  y = ctypes.c_float(y)   
  z = ctypes.c_float(z)   
  depth = ctypes.c_float(depth)
  dip = ctypes.c_float(dip)
  pot1 = ctypes.c_float(pot1) 
  pot2 = ctypes.c_float(pot2)
  pot3 = ctypes.c_float(pot3)
  pot4 = ctypes.c_float(pot4)
  dc3d0.iret.restype = ctypes.c_int
  return  dc3d0.iret(alpha, x, y, z, depth, dip, pot1, pot2, pot3, pot4)

