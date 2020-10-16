import matplotlib.pyplot as pyplot

x1=[1,3,5,7,9]
y1=[4,5,8,7,12]
pyplot.bar(x1,y1,label='this is bar1')
x2=[2,4,6,8,10]
y2=[2,3,4,5,10]
pyplot.bar(x2,y2,label='this is bar2')

pyplot.xlabel('X axis')
pyplot.ylabel('Y axis')
pyplot.title('Bar chart example \n hope you enjoy')
pyplot.legend()
pyplot.show()

