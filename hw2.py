from matplotlib.pyplot import *
import numpy as np

#get the digit vectors from file
digits=[]
count=0
with open('optdigits-orig.tra') as f:
	text=f.readlines()
	l=len(text)
	i=0
	count=0
	while(i<l):
		if(text[i]==' 3\n'):
			count+=1
			s=''
			for j in range(32):
				line=text[i-32+j].strip('\n')
				s+=line
			q=[]
			for c in s:
				q+=[int(c)]
			digits+=[q]
		i+=1



#PCA analysis
p=2
mean=np.average(digits,0)
meandata=digits-mean
u, s, v = np.linalg.svd(meandata.T)
l=s.shape[0]
s=np.diag(s[0:p])
u=u[0:p,:]
x1=u[0]
x2=u[1]
w1s=[]
w2s=[]
for x in meandata:
	w1=np.dot(x,x1)/np.linalg.norm(x1)
	w2=np.dot(x,x2)/np.linalg.norm(x2)
	w1s+=[w1]
	w2s+=[w2]

#draw original points	
im=figure()
ax=im.add_subplot(111)
ax.set_xlabel('first princpal component')
ax.set_ylabel('second princpal component')
ax.plot(w1s,w2s,'go')
show(im)
#print np.allclose(meandata, np.dot(u, np.dot(s, v)))


