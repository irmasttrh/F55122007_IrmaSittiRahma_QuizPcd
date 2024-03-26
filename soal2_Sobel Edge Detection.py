import cv2
import numpy as np

# Membaca gambar
img = cv2.imread('gamabar.jpeg', cv2.IMREAD_GRAYSCALE)

# Sobel edge detection
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

# Menghitung gradien magnitudo
sobel_mag = np.sqrt(sobel_x**2 + sobel_y**2)

cv2.imshow('Sobel Edge Detection', sobel_mag)
cv2.waitKey(0)
cv2.destroyAllWindows()
