import cv2
import matplotlib.pyplot as plt

def engin_matching(img):
    # Memuat citra dan template
    image = cv2.imread(img)
    template = cv2.imread(img, 0)
    template_height, template_width = template.shape

    # Konversi citra utama ke grayscale
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Pencocokan template menggunakan metode TM_CCOEFF_NORMED
    result = cv2.matchTemplate(image_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Menandai lokasi pencocokan pada citra
    top_left = max_loc
    bottom_right = (top_left[0] + template_width, top_left[1] + template_height)
    cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)

    # Menampilkan citra asli dan hasil pencocokan pola
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image_gray, cv2.COLOR_BGR2RGB))
    plt.title('Citra Asli')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Pencocokan Pola')
    plt.axis('off')

    plt.show()
