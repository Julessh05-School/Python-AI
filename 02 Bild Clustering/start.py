# -*- coding: utf-8 -*-
"""
Spyder Editor

"""

import matplotlib.image as mpimg
from matplotlib import pyplot as plt

# Bild laden
image_path = "mountain.jpg"
img = mpimg.imread(image_path)

# Bild anzeigen
# plt.imshow(img)
# plt.axis("off")
# plt.show()

# Liste der RGB-Werte erzeugen; die Liste ist dann der Input des k-Means-Clustering Verfahrens
pixels = [pixel.tolist() for row in img for pixel in row]

# Neues Bild
new_img = []
for row in range(len(img)):
    new_row = []
    for pixel in range(len(img[row])):
        # Jeder Farbwert eines Pixels des neuen Bildes wird aus dem Farbwert des korrespondierenden Pixels aus dem Ursprungsbild berechnen
        new_row.append(mpimg.recolor(img[row][pixel]))
    new_img.append(new_row)

plt.imshow(new_img)
plt.axis("off")
plt.show()