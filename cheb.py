import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
from pylab import *
x=float(input("enter the passband gain="))
y=float(input("enter the stopband gain="))
wp=float(input("enter wp in rad/sec="))
ws=float(input("enter ws in rad/sec="))
w=1000
e=((1/x**2)-1)**0.5
f=np.arccos((1/e)*((1/y**2)-1)**0.5)
g=np.arccos(ws/wp)
N=f/g
print("order of the filter:",N)
for i in range(0,w):
	if(w>wp):
		a=np.cos(N*np.arccos(i/wp))
		h=1/(1+(e*a)**2)**0.5
		plt.plot(w,h)
		plt.show()
	else:
		b=np.cosh(N*np.arccosh(i/wp))
		k=1/(1+(e*b)**2)**0.5
		plt.plot(w,k)
		plt.show()
