import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator, array_to_img 
from tensorflow.keras.models import load_model
import os, pickle
from skimage.io import imread
from PIL import Image
import image_spoiler
import img_loader
from skimage.transform import resize

model = load_model('model.h5', compile = False)

st.title('Document Image Cleaner')
st.image('front.png', width = 500)

choice = st.selectbox('Choose one of the following', ('URL', 'Upload Image'))
try:
  if choice == 'URL':
    image_path = st.text_input('Enter image URL...')
    try:
      img = img_loader.img_loader(image_path)
    except:
      st.markdown('Enter a URL')

  if choice == 'Upload Image':
    img = st.file_uploader('Upload an Image')
    try:
      img = img_loader.img_loader(image_path)
    except:
        st.markdown('Upload a valid image')

  pred = model.predict(np.expand_dims(img, 0))[0]
  pred = np.clip(pred, 0, 1)
  st.image([img, pred], caption = ['Input', 'Prediction'], width = 256)
except:
  pass
