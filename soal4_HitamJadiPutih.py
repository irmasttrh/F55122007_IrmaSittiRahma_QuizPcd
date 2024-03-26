import cv2

# Membaca gambar
img = cv2.imread('gamabar.jpeg')

# Mengubah gambar menjadi grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Menebinari gambar
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

# Menampilkan gambar
cv2.imshow('Hitam Jadi Putih', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
