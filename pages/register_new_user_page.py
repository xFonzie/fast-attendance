import streamlit as st
import re
import os
from uuid import uuid4
from detect_v2 import detect
from PIL import Image

class Error(Exception):
    pass

st.title("Registration")

# Layout
email_container = st.container()
email = email_container.text_input(
    "Enter Innopolis email",
    autocomplete='email',
    placeholder='example@example.com',

)

image_container = st.container()
image = image_container.camera_input(
    "Scan the face of the person from multiple angles",
)
picture = image_container.file_uploader("Or upload jpg file here",
                           type=['jpg'],
                           )

# Logic

if email:
    # Validates the email 
    pattern = re.compile('^[-\w\.]+@([\w-]+\.)+[\w-]{2,}$')
    if not re.fullmatch(pattern, email):
        email_container.write(Error("Wrong email format!"))
        email = None

if image:
    if email:
        detected = detect(image)
        st.image(detected)
        top_conf = detected[0].astype('uint8')
        if not os.path.exists(f'verification_data'):
            os.mkdir(f'verification_data')
        if not os.path.exists(f'verification_data/{email}'):
            os.mkdir(f'verification_data/{email}')
        im = Image.fromarray(top_conf)
        im.save(f"verification_data/{email}/{uuid4()}.jpg")
    else:
        email_container.write(Error("Enter email above!"))

if picture:
    if email:
        detected = detect(picture)
        st.image(detected)
        top_conf = detected[0].astype('uint8')
        if not os.path.exists(f'verification_data'):
            os.mkdir(f'verification_data')
        if not os.path.exists(f'verification_data/{email}'):
            os.mkdir(f'verification_data/{email}')
        im = Image.fromarray(top_conf)
        im.save(f"verification_data/{email}/{uuid4()}.jpg")
    else:
        email_container.write(Error("Enter email above!"))
