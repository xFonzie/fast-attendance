import streamlit as st
from detect import get_photo, detect_faces
import cv2
import numpy as np
from PIL import Image
from detect_v2 import detect
from siamese_network import recognize



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
    # array = convert_jpg_to_numpy(inp)
    faces = detect(inp)
    recognized_names = []
    for img in faces:
        with st.container():
            st.image(img)
            recognized_names.append(recognize(img))
            st.write(recognized_names[-1])
    # st.write(recognized_names)