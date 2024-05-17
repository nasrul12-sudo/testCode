import cv2
import numpy as np
import matplotlib.pyplot as plt

# Memuat citra hitam-putih
image_path = 'Freya.jpeg'  # Ganti dengan path citra Anda
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Menampilkan citra asli
plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Citra Asli')
plt.axis('off')

# Mendefinisikan kernel untuk operasi morfologi
kernel = np.ones((5, 5), np.uint8)

# Operasi Erosi
erosion = cv2.erode(image, kernel, iterations=1)

# Menampilkan hasil erosi
plt.subplot(1, 3, 2)
plt.imshow(erosion, cmap='gray')
plt.title('Hasil Erosi')
plt.axis('off')

# Operasi Dilasi
dilation = cv2.dilate(erosion, kernel, iterations=1)

# Menampilkan hasil dilasi
plt.subplot(1, 3, 3)
plt.imshow(dilation, cmap='gray')
plt.title('Hasil Dilasi')
plt.axis('off')

# Menampilkan semua citra
plt.show()
