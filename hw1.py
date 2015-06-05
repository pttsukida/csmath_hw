from matplotlib.pyplot import *
from numpy import *

Samplesize=100
degree=9
ll=-18
lam=pow(e,ll)
#gen x
x=[x*2.2*3.14/Samplesize+0.1 for x in range(Samplesize)]
y=sin(x)

#gen noise
v = random.normal(0,0.3,Samplesize)
for i in range(len(y)):
	y[i]+=v[i]

#draw original points	
im=figure()
ax=im.add_subplot(111)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.plot(x,y,'ro')


#begin regression

#create matrix A
def genRow(x,d):
	r=[]
	while (d>=0):
		r+=[pow(x,d)]
		d-=1
	return r
a=zeros(shape=(Samplesize,degree+1))

for i,t in enumerate(x):
	a[i]=genRow(t,degree)


at=transpose(a)
invata=linalg.inv(dot(at,a)+lam*identity(degree+1))
atb=dot(at,y)

w=dot(invata,atb)

#draw estimated curve
x2=[nx/100.0 for nx in range(650)]
y2=[]
for nx in x2:
	y2+=[polyval(w,nx)]

ax.text(4,1.1,'M=%d'%(degree))
ax.text(4,1.3,'ln t=%d'%(ll))
ax.plot(x2,y2)
show(im)

