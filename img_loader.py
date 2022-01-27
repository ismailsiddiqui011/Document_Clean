def img_loader(file):
    '''File: Path to Image'''
    def image_resize(image, width = None):
        dim = None
        (h, w) = image.shape[:2]

        r = width / float(w)
        dim = (width, int(h * r))

        resized = resize(image, (640, 512), preserve_range = True)
        return resized

    img = imread(file)
    img = image_resize(img, 512)/255    
    return img
