import numpy as np
print("2D-array")
array_2d = np.array([[1,2,3],[4,5,6]])
print(array_2d)
element_1 = array_2d[0,1]
element_2 = array_2d[1,2]
sum_elements = element_1 + element_2
print("Element at (0,1):", element_1)
print("Element at (1,2):", element_2)
print("Sum of elements:", sum_elements)
