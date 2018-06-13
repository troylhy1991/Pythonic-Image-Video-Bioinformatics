from skimage import io,color
import matplotlib.pyplot as plt

def negative_image(img):

    return 255 - img

img = io.imread('./images/negative_image.jpg')

img_gray = color.rgb2gray(img)

negative_img = negative_image(img_gray)

plt.figure(1)
plt.subplot(1,2,1)
plt.imshow(img)
plt.title('Original Image')

plt.subplot(1,2,2)
plt.imshow(negative_img, cmap='gray')
plt.title('Negative Image')

plt.show()
