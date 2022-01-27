import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array
from tensorflow.keras.models import load_model
import os, pickle
from skimage.io import imread
from PIL import Image
import image_spoiler
import img_loader
from skimage.transform import resize
import brute_force

model = load_model('model.h5', compile = False)

st.title('Document Image Cleaner')
st.image('front.png', width = 500)

choice = st.selectbox('Choose one of the following', ('URL', 'Upload Image'))
choice2 = st.selectbox('Choose the method', ('Brute Force', 'Deep Learning'))

brightness = st.text_input('Enter a brightness reduction factor range(0-0.80), 0 means image is already ruined or leave the field to use random value...')
try:
    brightness = float(brightness)
except:
    brightness = False
    st.markdown('Enter a valid value, using random values now...')
    
noise = st.text_input('Enter a noise factor range(0-0.001), 0 means image is already ruined or leave the field to use random value...')
try:
    noise = float(noise)
except:
    noise = False
    st.markdown('Enter a valid value, using random values now...')
    
try:
  if choice == 'URL':
    image_path = st.text_input('Enter image URL...')
    try:
      img = img_loader.img_loader(image_path)
    except:
      st.markdown('Enter a URL')

  if choice == 'Upload Image':
   try:
      img = st.file_uploader('Upload an Image')
      img = img_loader.img_loader(img)
   except:
      st.markdown('Upload a valid image')
  img_c = image_spoiler.image_spoiler(img, brightness, noise)

  if choice2 == 'Brute Force':
      img = array_to_img(img_c)
      pred, _, _ = brute_force.brute_force(img)
      pred = img_to_array(pred)
  else:
      pred = model.predict(np.expand_dims(img_c, 0)/255)[0]
      pred = np.clip(pred, 0, 1)

  st.image([img, pred], caption = ['Input', 'Prediction'], width = 512)
except:
      pass
