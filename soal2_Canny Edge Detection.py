import cv2

# Membaca gambar
img = cv2.imread('gamabar.jpeg', cv2.IMREAD_GRAYSCALE)

# Canny edge detection
canny = cv2.Canny(img, 100, 200)

# Menampilkan gambar
cv2.imshow('Canny Edge Detection', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
