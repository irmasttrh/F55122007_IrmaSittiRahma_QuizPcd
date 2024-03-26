import cv2

# Membaca gambar
img = cv2.imread('gamabar.jpeg')

# Melakukan flip horizontal
flipped_img = cv2.flip(img, 1)

# Menampilkan gambar
cv2.imshow('Flip Horizontal', flipped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
