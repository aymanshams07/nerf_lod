import numpy as np

positions = np.random.uniform(low=-10, high=10, size=(100, 3))

# print (positions)

camera = (0,2,0)

distance = np.linalg.norm(positions-camera, axis=1)
#print (distance, "distance")
importance = 1/ 1+ distance
print (importance, "importance")

indices = np.argsort(-importance)
print (indices, ": indices")