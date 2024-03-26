import cv2
import numpy as np

# Membaca gambar
img = cv2.imread('gamabar.jpeg')

# Menentukan mean dan standar deviasi noise
mean = 0
sigma = 15

# Menghasilkan noise gaussian
noise = np.random.normal(mean, sigma, (img.shape[0], img.shape[1], 3))

# Menambahkan noise pada gambar
noisy_img = img + noise

# Menampilkan gambar
cv2.imshow('Gaussian Noise', noisy_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
