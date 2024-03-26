import cv2

# Membaca gambar
img = cv2.imread('gamabar.jpeg')

# Menentukan sudut rotasi
angle = 45

# Menghitung matriks rotasi
M = cv2.getRotationMatrix2D((img.shape[1] / 2, img.shape[0] / 2), angle, 1.0)

# Memutar gambar
rotated_img = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

# Menampilkan gambar
cv2.imshow('Rotasi', rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
