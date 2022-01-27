import PIL
from tensorflow.keras.preprocessing.image import img_to_array 
from numpy.linalg import norm
import numpy as np
def brightness_(img): # Function to estimate the brightness ofcourse it may not be accurate but it will give a good estimation
    if len(img.shape) == 3:
        return np.average(norm(img, axis=2)) / np.sqrt(3)
    else:
        return np.average(img)

def brute_force(img, epoch = 20):
    res = {}
    for i in range(1, epoch+1):
        factor = ((1 - brightness_(img_to_array(img)/255))*i)+0.1
        pred = PIL.ImageEnhance.Brightness(img).enhance(factor)
        pred = PIL.ImageOps.autocontrast(pred)
        score = brightness_(img_to_array(pred)/255)
        if score <= 0.95:
            res[score] = factor, pred

    res = dict(sorted(res.items(), reverse = True))
    score, temp = list(res.items())[0]
    factor, pred = temp
    return pred, score, factor
