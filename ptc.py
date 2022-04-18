import numpy as np
N = int(input())
arr = np.array([input().split() for i in range(N)], float)
print(np.round(np.linalg.det(arr), decimals=2))