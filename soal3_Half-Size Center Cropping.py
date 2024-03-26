import cv2

# Membaca gambar
img = cv2.imread('gamabar.jpeg')

# Menentukan tinggi dan lebar gambar
tinggi, lebar = img.shape[:2]

# Menghitung dimensi cropping
crop_size = int(min(tinggi, lebar) / 2)

# Menghitung koordinat cropping
x = int((lebar - crop_size) / 2)
y = int((tinggi - crop_size) / 2)

# Melakukan cropping
cropped_img = img[y:y+crop_size, x:x+crop_size]

# Menampilkan gambar
cv2.imshow('Half-Size Center Cropping', cropped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
