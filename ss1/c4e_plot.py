from matplotlib import pyplot

#1 chuan bi datebase
labels = ['Android','ios','web']
values = [30, 40, 30]
colors = ['red', 'blue', 'black']
explode = [0, 0.2, 0]

#2 plot
pyplot.pie(values, labels=labels, colors=colors, explode=explode, shadow=True)
#cau hinh cho vong tron can xung
pyplot.axis('equal')

#3 show ra
pyplot.show()
