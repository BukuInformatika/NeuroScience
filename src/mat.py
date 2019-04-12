from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

x,y = np.loadtxt('Book1.csv', unpack = True, delimiter = ',')

plt.plot(x,y)
plt.title('Brainwave data result test')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()