import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file = pd.read_csv("istherecorrelation.csv", delimiter= ";")
file.plot(x='WO [x1000]', y='NL Beer consumption [x1000 hectoliter]', kind= 'scatter')
plt.title('Beer consumption for university students')
plt.xlabel('WO [x1000]')
plt.ylabel('NL Beer consumption [x1000 hectoliter]')

plt.savefig("plot_beer.png", dpi = 300)
plt.show()