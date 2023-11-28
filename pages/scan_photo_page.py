import streamlit as st
import cv2
import numpy as np
from PIL import Image
from detect_v2 import detect
from siamese_network import recognize
import pandas as pd


@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')


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
            result = recognize(img)
            best_match, best_prob = '', 0
            for k, v in result.items():
                if best_prob < v and 0.6 < v:
                    best_match = k
                    best_prob = v
            if best_prob > 0:
                recognized_names.append(best_match)
                st.write(recognized_names[-1])
    if len(recognized_names) > 0:
        df = pd.DataFrame(recognized_names)
        csv = convert_df(df)
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name="attendance.csv",
            mime='text/csv'
        )
    else:
        st.write("The model did not recognize any person. ☹")
    
