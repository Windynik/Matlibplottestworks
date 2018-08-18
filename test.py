import matplotlib.pyplot as plt, mpld3
import numpy
import matplotlib.animation as animation
from matplotlib import style
style.use('fivethirtyeight')
fig=plt.figure()
lol=fig.add_subplot(1,1,1)

def animate(i):
    graph_data=open('data.txt','r').read()
    lines=graph_data.split("\n")
    xs=[]
    ys=[]
    for line in lines:
        if len(line)>1:
            x,y=line.split(',')
            xs.append(x)
            ys.append(y)
    lol.clear()
    
    y_pos=numpy.arange(len(xs))
    lol.set_xticks(y_pos)
    lol.set_xticklabels(xs)
    
    lol.bar(xs,ys)
    lol.set_ylim(bottom=0)
    lol.set_xlabel("Names")
    lol.set_ylabel("Marks")
    lol.set_title("Marks really shouldn't be compared.. D:")
    
    
    
    

# def lel(i):
#     objects = ['Nikhil','Aditi','Niharika','Rajat']
#     marks = [12,20,18,15]
#     y_pos=numpy.arange(len(objects))
#     fig.bar(y_pos,marks)
#     fig.xticks(y_pos,objects)
#     fig.xlabel("Names")
#     fig.ylabel("Marks")
#     fig.title("Comparison of marks that shouldn't be done ofc :P")
#     fig.bar(y_pos,marks)

ani=animation.FuncAnimation(fig,animate,interval=1000)
plt.show()


# objects = ['Nikhil','Aditi','Niharika','Rajat']
# marks = [12,20,18,15]
# y_pos=numpy.arange(len(objects))

# plt.bar(y_pos,marks)
# plt.xticks(y_pos,objects)
# plt.xlabel("Names")
# plt.ylabel("Marks")
# plt.title("Comparison of marks that shouldn't be done ofc :P")
# while(True):
    # x=input("Input the name to be added : ")
    # y=input("Input the marks associated with that name : ")
    # objects.append(x)
    # marks.append(y)
    # plt.bar(y_pos,marks)
    # plt.show()

# mpld3.save_html(lol,"lol.html")
exit()