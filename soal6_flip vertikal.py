import cv2

# Membaca gambar
img = cv2.imread('gamabar.jpeg')

# Melakukan flip vertikal
flipped_img = cv2.flip(img, 0)

# Menampilkan gambar
cv2.imshow('Flip Vertikal', flipped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
