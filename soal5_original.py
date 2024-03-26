import cv2

# Membaca gambar
img = cv2.imread('gamabar.jpeg')

# Menampilkan gambar
cv2.imshow('Gambar Original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
