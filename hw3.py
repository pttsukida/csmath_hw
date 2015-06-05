import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np
import math
mean = [3,0]
cov = [[1,0],[0,4]] 
x1,y1 = np.random.multivariate_normal(mean,cov,500).T

mean = [-1,0]
cov = [[3,0],[0,1]] 
x2,y2 = np.random.multivariate_normal(mean,cov,200).T

x=np.append(x1,x2) 
y=np.append(y1,y2)

def drawcircle(u,cov):
	rx=cov[0,0]
	ry=cov[1,1]
	e=Ellipse(xy=(u[0,0],u[0,1]),width=rx,height=ry,edgecolor='r', fc='None', lw=2)
	return e
def calcGaussion(x,u,cov):
	#print np.linalg.det(cov),cov
	a=1.0/(2*math.pi*math.sqrt(np.linalg.det(cov)))
	c=x-u
	invcov=np.linalg.inv(cov)
	b=math.exp(-0.5*c*invcov*c.T)
	return b*a
	#b=(x-u).reshape(1,2)
def e_step(x,p1,u1,cov1,p2,u2,cov2):
	pj1=[]
	pj2=[]
	for a in x:
		py1=p1*calcGaussion(a,u1,cov1)
		py2=p2*calcGaussion(a,u2,cov2)
		pj1.append(py1/(py1+py2))
		pj2.append(py2/(py1+py2))
	return pj1,pj2
def m_step(pj1,pj2,x):
	n1=sum(pj1)
	n2=sum(pj2)
	p1_=n1/(n1+n2)
	p2_=n2/(n1+n2)

	u1=np.matrix([0,0])
	u2=np.matrix([0,0])

	for i in range(len(x)):
		u1=u1+pj1[i]*(x[i])
		u2=u2+pj2[i]*(x[i])
	u1=u1/n1
	u2=u2/n2
	c1=np.matrix([[0.0,0],[0,0]])
	c2=np.matrix([[0.0,0],[0,0]])
	d1=0
	d2=0
	for i in range(len(x)):
		d1=x[i]-u1
		c1+=pj1[i]*(d1.T*d1)
		d2=x[i]-u2
		c2+=pj2[i]*(d2.T*d2)

	c1*=1.0/n1
	c2*=1.0/n2

	return p1_,p2_,u1,u2,c1,c2

f=plt.figure()


p1=0.5
mean1 = np.matrix([0,0])
cov1 = np.matrix([[1,0],[0,1]])

p2=0.5 
mean2 = np.matrix([0,0])
cov2 = [[1,0],[0,2]] 
xy=[]
for i in range(len(x)):
	t=np.matrix([x[i],y[i]])
	xy.append(t)

for i in range(50):
	pj1,pj2=e_step(xy,p1,mean1,cov1,p2,mean2,cov2)
	p1,p2,mean1,mean2,cov1,cov2=m_step(pj1,pj2,xy)

	if i%20==0:
		plt.plot(x,y,'x');
		ax = plt.gca() 
		e=drawcircle(mean1,cov1)
		ax.add_patch(e)
		e=drawcircle(mean2,cov2)
		ax.add_patch(e)
		plt.axis('equal'); 	
		plt.show()
print "p ",p1,p2
print "mean:",mean1,mean2
print "cov1:",cov1
print "cov2",cov2
