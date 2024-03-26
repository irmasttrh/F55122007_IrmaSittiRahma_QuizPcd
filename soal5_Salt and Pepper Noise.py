import cv2
import numpy as np

# Membaca gambar
img = cv2.imread('gamabar.jpeg')

# Menentukan probabilitas noise
prob = 0.05

# Menghasilkan noise salt and pepper
noise = np.random.randint(0, 255, (img.shape[0], img.shape[1], 3), np.uint8)

# Menambahkan noise pada gambar
noisy_img = img + noise

# Menampilkan gambar
cv2.imshow('Salt and Pepper Noise', noisy_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
