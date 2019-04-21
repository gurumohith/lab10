import numpy as np
import matplotlib.pyplot as plt
from pylab import *
p=float(input("enter pass band gain:"))
s=float(input("enter stop band gain:"))
wp=float(input("enter pass band frequency:"))
ws=float(input("enter stop band frequency:"))
if(ws>wp):
	x=np.log(((1/p**2)-1)/((1/s**2)-1))
	y=np.log(wp/ws)
	N=0.5*(x/y)
	print("order of the filter is:",N)
	a=((1/ws**2)-1)
	b=(0.5/N)
	c=(a**b)
	wc=ws/c
	print("cut off frequency is:",wc)
	w=np.arange(0,100,10)
	H=1/((1+(w/wc)**(2*N))*0.5)
	plt.plot(w,H)
	plt.show()
else:
	print("filter is not possible")

