from skimage.measure import label
from skimage.morphology import binary_closing, binary_dilation, binary_opening, binary_erosion
import matplotlib.pyplot as plt
import numpy as np

data = np.load("wires3npy.txt")
labeled = label(data)

for i in range (1, labeled.max()+1):
  print(f"Провод {i}")
  temp = np.zeros_like(data)
  temp[labeled == 1] = 1
  res = binary_erosion (temp, np.ones((3,1)))
  parts = label(res). max()
  match parts:
    case 0:
      print(f"Провод порван")
    case 1:
      print(f"Провод цел")
    case _:
      print(f"Части {parts}")

plt.subplot(111)
plt.imshow(data)