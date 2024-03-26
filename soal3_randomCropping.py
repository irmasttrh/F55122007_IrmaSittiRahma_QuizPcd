import cv2
import numpy as np

# Membaca gambar
img = cv2.imread('gamabar.jpeg')

# Menentukan tinggi dan lebar gambar
tinggi, lebar = img.shape[:2]

# Menentukan dimensi cropping
min_crop_size = 100
max_crop_size = 200

# Menghasilkan koordinat cropping acak
x = np.random.randint(0, lebar - min_crop_size)
y = np.random.randint(0, tinggi - min_crop_size)
w = np.random.randint(min_crop_size, max_crop_size)
h = np.random.randint(min_crop_size, max_crop_size)

# Melakukan cropping
cropped_img = img[y:y+h, x:x+w]

# Menampilkan gambar
cv2.imshow('Random Cropping', cropped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
