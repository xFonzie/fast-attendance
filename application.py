import streamlit as sl
from st_pages import Page, show_pages, add_page_title

add_page_title("Home page")

sl.write("""
This is a project made in Innopolis University for increase and accurate a speed of checking attendance!
""")

show_pages(
    [
        Page("application.py", "Home"),
        Page("pages/register_new_user_page.py", "Register a new student"),
        Page("pages/scan_photo_page.py", "Scan the room for attendance")
    ]
)