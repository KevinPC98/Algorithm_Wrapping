'''
Algorithm Wrapping
User: KevinPC98
'''
import matplotlib.pyplot as plt
class Wrapping(object):
	"""docstring for Wrapping"""
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.n = len(self.x)

	def Derecha(self,a,b,c):
		return self.Area2(a,b,c)<0

	def Area2(self,a,b,c):
		return (((a[0]-c[0])*(b[1]-c[1]))-((a[1]-c[1])*(b[0]-c[0])))/2

	def Main(self):
		h = 0
		H = list()
		H.append(self.x.index(min(self.x)))
		while True:
			i = (H[h] % (self.n-1)) + 1
			for j in range(0,self.n):
				if self.Derecha([self.x[H[h]],self.y[H[h]]],[self.x[i],self.y[i]],[self.x[j],self.y[j]]):
					i = j
			h += 1
			if len(H)<=h:
				H.append(i)
			else:
				H[h] = i
			if i == H[0]:
				break
		print("X coordinates: ",self.x)
		print("Y coordinates: ",self.y)
		print("Border Points: ", H)
		self.graficar(self.x,self.y,H)

	def graficar(self,x,y,H):
		plt.figure(figsize=(7,7))
		for i in range(0,len(x)):
			plt.plot(x[i],y[i],'o',color="black")
			if i<len(H):
				plt.plot([x[H[i]],x[H[i-1]]],[y[H[i]],y[H[i-1]]],color="red")
		plt.plot([x[H[-2]],x[H[-1]]],[y[H[-2]],y[H[-1]]],color="red")
		plt.grid()
		plt.show()
