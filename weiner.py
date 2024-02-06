import numpy as np
import matplotlib.pyplot as plt
import math




b=1
a=.5
rng = np.random.default_rng()
rng.normal()

time=1600
n = 1000
start= 0
value=[]
x_value=[]
value_sum = [] 
for i in range(0,time):
    for j in range(0,n):
        value.append(a*(1/n)+ b*rng.normal()*math.sqrt((1/n)))
        x_value.append(i+j/n)
        if(i>0 or j>0):
            value_sum.append(value[n*i+j] + value_sum[n*i+j-1] )
        else:
            value_sum.append(value[i])

for i in range(0,time*n):
        value_sum[i]= value_sum[i] + start
plt.plot(x_value,value_sum)

plt.show()

def temp():
    x = np.array([1, 2, 3, 4])
    y = x*2
    
    plt.plot(x, y)
    plt.xlabel("X-axis")  # add X-axis label
    plt.ylabel("Y-axis")  # add Y-axis label
    plt.title(
        "Any suitable title")  # add title
    plt.show()