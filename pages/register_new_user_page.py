import streamlit as st
import re

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
    "Scan the face of the person",
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
        bytes_data = image.getvalue()
        with open(f'saved_images/{email}.jpg', 'wb') as file:
            file.write(bytes_data)
    else:
        email_container.write(Error("Enter email above!"))

if picture:
    if email:
        bytes_data = picture.getvalue()
        with open(f'saved_images/{email}.jpg', 'wb') as file:
            file.write(bytes_data)
    else:
        email_container.write(Error("Enter email above!"))