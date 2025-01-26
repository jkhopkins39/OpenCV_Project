import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("flower.jpg")
cv.imshow("Flower", img)
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

weights = np.array([0.114, 0.587, 0.2989]) #Order: BGR
dotProductGray = np.dot(img[..., :3], weights)
dotProductGray = np.clip(dotProductGray, 0, 255).astype(np.uint8) #Pass through clip method to correct dimensions and return type

#This version displays the grayscale applied by OpenCV
plt.imshow(gray, cmap='gray')
plt.title("OpenCV Grayscale (problem 1a)")
plt.show()

plt.imshow(dotProductGray, cmap='gray')
plt.title("Dot Product Grayscale (problem 1b)")
plt.show()

#Pass the array of kernel sizes, each element "size" makes a kernel based on its size, applying kernel with filter2D.
def custom_average_filter(image, kernel_sizes):
    fig, axes = plt.subplots(1, len(kernel_sizes)+1, figsize=(15,5)) #Define subplot to display 5 images in a row
    axes[0].imshow(gray, cmap='gray') #Display image converted to grayscale
    axes[0].set_title('Original Image') 
    axes[0].axis('off')
    fig.canvas.manager.set_window_title("Problem 2")
    for i, size in enumerate(kernel_sizes):
        # Create a kernel of size (size, size)
        kernel = np.ones((size, size), np.float32) / (size * size)
        
        # Apply the kernel (averaging filter)
        filtered_image = cv.filter2D(gray, -1, kernel)
        
        # Display the result
        axes[i + 1].imshow(filtered_image, cmap='gray')
        axes[i + 1].set_title(f'Kernel Size {size}x{size}')
        axes[i + 1].axis('off')

    plt.tight_layout()
    plt.show()

kernel_sizes = [3,5,10,15]
custom_average_filter(gray, kernel_sizes)

downsampled100 = cv.resize(gray, (100,100), interpolation=cv.INTER_LINEAR)
downsampled50 = cv.resize(gray, (50,50), interpolation=cv.INTER_LINEAR)
downsampled25 = cv.resize(gray, (25,25), interpolation=cv.INTER_LINEAR)
downsampled15 = cv.resize(gray, (15,15), interpolation=cv.INTER_LINEAR)

linearUpsampled100 = cv.resize(downsampled100, (200,200), interpolation=cv.INTER_LINEAR)
linearUpsampled50 = cv.resize(downsampled50, (200,200), interpolation=cv.INTER_LINEAR)
linearUpsampled25 = cv.resize(downsampled25, (200,200), interpolation=cv.INTER_LINEAR)
linearUpsampled15 = cv.resize(downsampled15, (200,200), interpolation=cv.INTER_LINEAR)

cubicUpsampled100 = cv.resize(downsampled100, (200,200), interpolation=cv.INTER_CUBIC)
cubicUpsampled50 = cv.resize(downsampled50, (200,200), interpolation=cv.INTER_CUBIC)
cubicUpsampled25 = cv.resize(downsampled25, (200,200), interpolation=cv.INTER_CUBIC)
cubicUpsampled15 = cv.resize(downsampled15, (200,200), interpolation=cv.INTER_CUBIC)

images = [
    (downsampled100, "Downsampled to 100x100"),
    (downsampled50, "Downsampled to 50x50"),
    (downsampled25, "Downsampled to 25x25"),
    (downsampled15, "Downsampled to 15x15"),
    (linearUpsampled100, "Linear upsampled from 100x100"),
    (linearUpsampled50, "Linear upsampled from 50x50"),
    (linearUpsampled25, "Linear upsampled from 25x25"),
    (linearUpsampled15, "Linear upsampled from 15x15"),
    (cubicUpsampled100, "Cubic upsampled from 100x100"),
    (cubicUpsampled50, "Cubic upsampled from 50x50"),
    (cubicUpsampled25, "Cubic upsampled from 25x25"),
    (cubicUpsampled15, "Cubic upsampled from 15x15")
]

fig, axes = plt.subplots(3, 4, figsize=(15,10))

for ax, (image, title) in zip(axes.ravel(), images):
    ax.imshow(image, cmap='gray')
    ax.set_title(title)
    ax.axis('off')

fig.canvas.manager.set_window_title("Problem 3")

plt.tight_layout()
plt.show()