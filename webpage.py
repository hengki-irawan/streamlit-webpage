import streamlit as st
import streamlit_analytics
from streamlit_lottie import st_lottie
from PIL import Image
from content import *
from utilities import *


PAGE_ICON = 'images/icon.jpg'
LOTTIE_ANIMATION_ABOUTME = load_animation(lottie_aboutme_url)
color = st.color_picker('Pick A Color', '#FBBE5B')


# Main Header
st.set_page_config(page_title="Hengki's gallery", page_icon=Image.open(f"{PAGE_ICON}"))
st.subheader("Silent Frames")
st.title(":color[Capturing Quiet Moments: Through My Lens]")
local_css("style/form_style.css") #to hide streamlit brand


# Buttons
with st.container():
    photo_gallery_button, home_button = st.columns(2)

    # Define sections
    sections = [":technologist: About", ":camera: Photo Gallery"]

    # Display buttons
    for i, button in enumerate([photo_gallery_button, home_button]):
        if button.button(f"{sections[i]}", use_container_width=True):
            st.session_state.section_index = i


if "section_index" not in st.session_state:
    st.session_state.section_index = 0            

# Display content based on the selected section
if st.session_state.section_index == 0:
    with st.container():
        image_section, aboutme_section = st.columns((1, 3))
        with image_section:
            st_lottie(LOTTIE_ANIMATION_ABOUTME)
            st.markdown(f"""
            <div style="text-align: center;">
                <p style="font-weight: bold;"><a href="{linkedin_url}" target="_blank" rel="noopener noreferrer">LinkedIn</a></p>
            </div>
            """, unsafe_allow_html=True)

        with aboutme_section:
            st.markdown(f"""**<div style="color: rgb(251,190,91);">""" "About" """</div>**""",  unsafe_allow_html=True)
            st.markdown(f"""<div style="color: rgb(251,190,91);">{about}</div>""", unsafe_allow_html=True)
        
            

elif st.session_state.section_index == 1:
   with st.container():
        st.subheader("Photo Gallery")
        num_columns = 3
        num_rows = len(images) // num_columns + (len(images) % num_columns > 0)
        
        gallery_cols = st.columns(num_columns)

        for i, (image_path, description) in enumerate(images.items()):
            with gallery_cols[i % num_columns]:
                image_paths = f"{image_path}"
                image = Image.open(image_paths)
                st.image(image, caption=description, use_column_width=True) 
    
