import random
import matplotlib.pyplot as plt
import numpy as np

a = []
m = []
n = []
t0 = 0
t1 = 0
alph = 0.0005
adj0 =0
adj1 =0
mini = 0.0005

u = np.arange(0,10,0.1)

for c in range(11):
    a.append((random.randrange(1,10,1),random.randrange(1,10,1)))

print(a)

for x in range(100000):
    adj0 = 0
    adj1 = 0
    for cord in a:
        adj0 += t0 + t1*cord[0]-cord[1]
        adj1 += (t0 + t1*cord[0]-cord[1])*(cord[0])

    temp0 = t0 - alph*adj0/len(a)
    temp1 = t1 - alph*adj1/len(a)

    t0 = temp0
    t1 = temp1

print("for y = mx + c")
print("c =")
print(round(t0,3))
print("m =")
print(round(t1,3))

for i in range(11):
    m.append(a[i][0])
    n.append(a[i][1])

y =  t0 + u*t1

plt.plot(u,y)    
plt.scatter(m,n)
plt.show()



    
        
