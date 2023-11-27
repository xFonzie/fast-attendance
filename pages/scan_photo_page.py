import streamlit as st
from detect import get_photo, detect_faces
import cv2
import numpy as np
from PIL import Image


# TODO:
# - Remove this ↓ and make it in detect.py
def convert_jpg_to_numpy(image_buffer):
    img = Image.open(image_buffer)
    img = np.array(img)
    st.write(img.shape)
    return img

image_container = st.container()
image = image_container.camera_input(
    "Scan the room",
)
picture = image_container.file_uploader("Or upload jpg file here",
                           type=['jpg'],
                           )


inp = None

if image:
    inp = image

if picture:
    inp = picture

if inp:
    # Remove after debugging
    st.image(inp)
    # -------------

    # array = convert_jpg_to_numpy(inp)
    faces = detect_faces(inp)
    print(len(faces))
    for img in faces:
        st.image(img)
        # im = Image.fromarray(img)
        # im.save("your_file.jpeg")
    inp = None