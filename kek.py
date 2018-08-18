import matplotlib.pyplot as plt, mpld3
import numpy
import matplotlib.animation as animation
from matplotlib import style
lol=plt.figure()
fig=lol.add_subplot(1,1,1)
def animate(i):
    graph_data=open('data.txt','r').read()
    lines=graph_data.split("\n")
    objects = []
    marks = []
    for line in lines:
        if len(line)>1:
            x,y=line.split(',')
            objects.append(x)
            marks.append(int(y))
    fig.clear()
    y_pos=numpy.arange(len(objects))
    fig.set_xticks(y_pos)
    fig.set_xticklabels(objects)
    fig.set_xlabel("Names")
    fig.set_ylabel("Marks")
    fig.set_title("Comparison of marks that shouldn't be done ofc :P")
    fig.bar(y_pos,marks)
    lol.savefig('lol.png')
ani=animation.FuncAnimation(lol,animate,interval=1000)
plt.show()

# objects = ['Nikhil','Aditi','Niharika','Rajat']
# marks = [12,20,18,15]
# y_pos=numpy.arange(len(objects))
# plt.bar(y_pos,marks)
# plt.xticks(y_pos,objects)
# plt.xlabel("Names")
# plt.ylabel("Marks")
# plt.title("Comparison of marks that shouldn't be done ofc :P")
# plt.show()