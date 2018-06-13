from skimage import data, exposure, img_as_float, img_as_ubyte
import matplotlib.pyplot as plt

image = img_as_float(data.camera())
image_uint8 = img_as_ubyte(data.camera())

hi = exposure.histogram(image_uint8)
cdf = exposure.cumulative_distribution(image_uint8)


plt.figure(1)

plt.subplot(1,2,1)
plt.imshow(image_uint8, cmap='gray')
plt.title('Sample Image')

plt.subplot(1,2,2)
plt.bar(hi[1], hi[0])
plt.hold(True)
plt.plot(cdf[1], cdf[0]*6400, 'r')
plt.hold(False)
plt.title('Histogram and CDF')
plt.xlabel('Pixel Intensity')

plt.show()
