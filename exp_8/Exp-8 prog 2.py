import numpy as np
arr = np.array([1, 2, 3], dtype='int32')
print("Data Type:", arr.dtype)
arr = arr.astype('float64')
print("Updated type:", arr.dtype)
