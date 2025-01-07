import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = [1,2,9,4,1]
y = [5,3,8,7,9]
colors = ['seagreen', 'lightgreen', 'darkgreen', 'olive', 'springgreen']
# plt.bar(x,y, color='red')
plt.pie(x, colors=colors)
# plt.hist(x, bins=5)
plt.title("Basic Graph Plot")
# plt.xlabel("X values")
# plt.ylabel("Y values")
plt.show()