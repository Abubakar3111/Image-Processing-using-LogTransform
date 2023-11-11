#Code by Abubakar Asif Abubakar Asif
#Full Stack flutter DEVELOPER
#|AI DEVELOPER| IMAGE PROCESSING EXPERT
#abubakarasif3111@gmail.com
#github.com/Abubakar3111
#https://www.linkedin.com/in/abubakar-asif-b3b94021a/
import numpy as np
import matplotlib.pyplot as plt
import math

# Load the image (replace "Add Your Image Address Here" with the actual file path)
A = plt.imread("Add Your Image Address Here")

# Create a copy of the original image
B = A.copy()

# Get the number of rows and columns in the image
rows = A.shape[0]
cols = A.shape[1]

# Print the shape of the image (number of rows, number of columns, and number of channels if it's a color image)
print("Image Shape:", A.shape)
print("Number of Rows:", rows)
print("Number of Columns:", cols)

# Apply log transformation to each pixel in the image
for x in range(rows):
    for y in range(cols):
        # Add 1 to avoid log(0) and apply log2 transformation
        b = 1 + B[x, y]
        B[x, y] = math.log2(b)

# Create a figure with two subplots for original and log-transformed images
fig = plt.figure()

# Plot the original image
ax1 = fig.add_subplot(1, 2, 1)
plt.title("Original Image")
ax1.imshow(A, cmap='gray')

# Plot the log-transformed image
ax2 = fig.add_subplot(1, 2, 2)
plt.title("Log Transformed Image")
ax2.imshow(B, cmap='gray')

# Display the images
plt.show()
