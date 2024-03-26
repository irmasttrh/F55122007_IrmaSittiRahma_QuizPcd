import cv2

# Membaca gambar
img = cv2.imread('gamabar.jpeg')

# Mengubah gambar menjadi grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Menginversi gambar
inverted = 255 - gray

# Menampilkan gambar
cv2.imshow('Putih Jadi Hitam', inverted)
cv2.waitKey(0)
cv2.destroyAllWindows()
