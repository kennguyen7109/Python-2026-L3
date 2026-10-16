import matplotlib, math
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
x = [i/10 for i in range(-50,50)]
y = [2*i + math.sin(i)**2 + 3 for i in x]
plt.plot(x,y, marker="*")
plt.grid(True)
plt.title("hello, po!")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("po.pdf")
plt.show()