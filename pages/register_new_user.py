import streamlit as st
import re

class Error(Exception):
    pass

email = st.text_input(
    "Enter Innopolis email",
    autocomplete='email',
    placeholder='example@example.com',

)
image = st.camera_input(
    "Scan the face of the person",
)

if email:
        pattern = re.compile('^[-\w\.]+@([\w-]+\.)+[\w-]{2,}$')
        if not re.fullmatch(pattern, email):
            st.write(Error("Wrong email format!"))

if image:
    if email:
        bytes_data = image.getvalue()
        with open(f'saved_images/{email}.bytes', 'wb') as file:
            file.write(bytes_data)
    else:
        st.write(Error("Enter email above!"))
    