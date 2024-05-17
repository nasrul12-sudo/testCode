from TugasKelompok.edge import engin_edge
from TugasKelompok.blur import engin_blur
from TugasKelompok.maching import engin_matching

def blur(img):
    return engin_blur(img)
def egde(img):
    return engin_edge(img)
def match(img):
    return engin_matching(img)

if __name__ == "__main__":
    img = "./Freya.jpeg"

    blur(img)
    egde(img)
    match(img)
