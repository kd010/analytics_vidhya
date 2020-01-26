import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

white_start_row = np.ones((64,64,3))
black_start_row = np.zeros((64,64,3))

for i in range(7):
    if (i+1)%2 == 0:
        white_start_row = np.append(white_start_row, np.ones((64,64,3)), 1)
        black_start_row = np.append(black_start_row, np.zeros((64,64,3)), 1)
    else:
        white_start_row = np.append(white_start_row, np.zeros((64,64,3)), 1)
        black_start_row = np.append(black_start_row, np.ones((64,64,3)), 1)

img = white_start_row

for i in range(7):
    if i%2 == 0:
        img = np.append(img, black_start_row, 0)
    else:
        img = np.append(img, white_start_row, 0)
    

plt.imshow(img)
plt.show()