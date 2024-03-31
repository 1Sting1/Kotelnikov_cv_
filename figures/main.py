import numpy as np
from skimage.measure import label

def area(LB, label=1):
    return np.sum(LB == label)

def unique_areas(LB):
    unique_areas = {}
    for i in np.unique(LB):
        if i != 0:
            ar = area(LB, label=i)
            if ar not in unique_areas:
                unique_areas[ar] = 0
    for i in np.unique(LB):
        if i != 0:
            unique_areas[area(LB, label=i)] += 1
    return dict(sorted(unique_areas.items()))

image = np.load("ps.npy.txt")
labeled = label(image)
result = unique_areas(labeled)

print(result)