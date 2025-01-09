import numpy as np
import matplotlib.pyplot as plt

# #displays 2 line plots
# plt.subplot(211)
# plt.plot(np.array([4,6,3,10,7]))
# plt.subplot(212)
# plt.plot(np.random.uniform(10,15,20))
# plt.show()


# #displays a bar chart
# x = [1,2,3,4,5]
# y = [7,2,3,5.5,1]
# plt.xticks(x, ['b1','b2','b3','b4','b5'])
# plt.bar(x,y,align='center')
# plt.grid()
# plt.show()

# #pie chart with uniform distribution
# a = np.random.uniform(1,10,7)
# L = ['b1','b2','b3','b4','b5','b6','b7']
# plt.pie(a, labels=L)
# plt.title('A pie chart example')
# plt.show()

# #Displays a scatterplot
# x = np.random.uniform(1,100,50)
# y = np.random.normal(20,10,50)
# plt.scatter(x,y)
# plt.show()

# #Displays box and whisker plot
# x = np.random.uniform(1,100,50)
# plt.boxplot(x)
# plt.show()

#Finally this is an example of annotation and labeling a graph for readability
x=np.linspace(0, 2*np.pi, 100)
sinx=np.sin(x) # calculate sin(x)
plt.plot(x,sinx, label='sin') # legend
plt.legend(loc="best") #show legend
plt.xlabel("Radian") # x label
plt.ylabel("Amplitude") # y label
plt.annotate(r'$sin(\frac{\pi}{2})=1$', xy=(1.5, 1))
xytext=(1 , 0.5)
arrowprops=dict(arrowstyle="->")
plt.text(5, 0.5, 'This is \nSine wave')
plt.show()