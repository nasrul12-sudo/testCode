import cv2
import matplotlib.pyplot as plt

def engin_edge(img):
    # Memuat citra
    image = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    # Deteksi tepi menggunakan algoritma Canny
    edges = cv2.Canny(image, 100, 200)

    # Menampilkan citra asli dan hasil deteksi tepi
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Citra Asli')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(edges, cmap='gray')
    plt.title('Deteksi Tepi')
    plt.axis('off')

    plt.show()
