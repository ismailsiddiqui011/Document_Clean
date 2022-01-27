import numpy as np

def image_spoiler(img, brightness_factor = False, noise_factor = False):
    '''Brightness Factor: Range(0-0.80), put 0 to disable the random brightness reduction
       Noise Factor: Range(0-0.001), put 0 to disable the random noise'''
    if brightness_factor is False:
        brightness = np.random.uniform(0, 0.80)
    else:
        brightness = brightness_factor
    img = np.clip(img-brightness, 0, 1)
    
    if noise_factor is False:
        sd = np.random.uniform(0, 0.001)
        noise = np.random.normal(scale = sd, size = (img.shape))  
    else:
        noise = noise_factor
    
    img = img + noise
    img = np.clip(img, 0, 1)
    return img
