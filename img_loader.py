import cv2
from skimage.io import imread

def img_loader(file):
    '''File: Path to Image'''
    def image_resize(image, width = None):
        dim = None
        (h, w) = image.shape[:2]

        r = width / float(w)
        dim = (width, int(h * r))

        resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
        resized = cv2.resize(image, (640, 512), interpolation = cv2.INTER_AREA)
        return resized

    img = imread(file)
    img = image_resize(img, 512)/255    
    return img
