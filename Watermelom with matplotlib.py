import matplotlib
import matplotlib.pyplot as plt

data = [
        [10,10,10,10,10,10,10,10,10,10,5,10,10,10],
        [10,10,10,10,10,10,10,10,10,9,6,5,10,10],
        [10,10,10,10,10,10,10,10,10,9,9,9,6,5,10],
        [10,10,10,10,10,10,10,9,9,1,9,9,6,5],
        [10,10,10,10,10,10,9,9,9,9,9,9,6,5],
        [10,10,10,10,10,9,9,9,9,1,9,9,6,5],
        [10,10,10,10,9,9,9,9,9,9,9,6,5,5],
        [10,10,10,9,9,9,9,1,9,9,9,6,5,5],
        [10,10,9,1,9,1,9,9,9,9,6,5,5,10],
        [10,5,6,9,9,9,9,9,9,9,6,5,10,10],
        [10,10,5,6,6,6,6,6,6,6,5,10,10,10],
        [10,10,10,6,6,6,6,6,6,6,10,10,10,10]
        ]

data = [[1,2,3,4,5,6,7,8,9,10]]
plt.imshow(data, cmap="nippy_spectral")
plt.show()