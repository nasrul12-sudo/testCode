import cv2
import matplotlib.pyplot as plt

def engin_blur(img):
    # Memuat citra
    image = cv2.imread(img)

    # Pengaburan dengan Gaussian Blur
    blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

    # Menampilkan citra asli dan hasil pengaburan
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Citra Asli')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB))
    plt.title('Pengaburan Gambar')
    plt.axis('off')

    plt.show()
