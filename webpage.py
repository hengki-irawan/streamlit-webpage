import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
from content import *
from utilities import *

PAGE_ICON = 'streamlit-webpage/images/icon.jpg'
LOTTIE_ANIMATION_ABOUTME = load_animation(lottie_aboutme_url)
LOTTIE_ANIMATION_SKILL = load_animation(lottie_skill_url)


# Main Header
st.set_page_config(page_title="Hengki's Portofolio", page_icon=Image.open(f"{PAGE_ICON}"))

st.subheader("Data Wanderer")
st.title("Exploring the World of Data and Beyond")
local_css("streamlit-webpage/style/form_style.css") #to hide streamlit brand



# Buttons
with st.container():
    home_button, portfolio_button, skill_button, photo_gallery_button = st.columns(4)

    # Define sections
    sections = [":technologist: About me", ":open_file_folder: Portofolio", ":hammer_and_wrench: Skills & Expertise", ":camera: Photo Gallery"]

    # Display buttons
    for i, button in enumerate([home_button, portfolio_button, skill_button, photo_gallery_button]):
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
                <p style="font-weight: bold;"><a href="{github_url}" target="_blank" rel="noopener noreferrer">Github</a></p>
                <p style="font-weight: bold;"><a href="{tableau_url}" target="_blank" rel="noopener noreferrer">Tableau Public</a></p>
            </div>
            """, unsafe_allow_html=True)

        with aboutme_section:
            st.markdown("**About Me**")
            st.markdown(f"{about_me}", unsafe_allow_html=True)
            

elif st.session_state.section_index == 1:
    with st.container():
        st.subheader("Portfolio")

    selected_option = st.radio("Select a project you'd like to explore", portfolio.keys())
    st.write('---')
   
    # vid_section, desc_section = st.columns((1, 2))
    # with desc_section:
    display_content(selected_option)
    # with vid_section:
    #     display_videos(selected_option)


elif st.session_state.section_index == 2:
    with st.container():
        st.subheader("Skills and Expertise")
        l_column_skill, r_column_skill, image_column = st.columns(3)
        length_skill = len(skills_n_expertise)
        first_half_skill = length_skill // 2

        for n in skills_n_expertise[:first_half_skill+1]:
            with l_column_skill:
                st.markdown(f"{n}")

        for n in skills_n_expertise[first_half_skill+1:]:
            with r_column_skill:
                st.markdown(f"{n}")
        
        with image_column:
          st.lottie(LOTTIE_ANIMATION_SKILL)
        st.write("---")
         

elif st.session_state.section_index == 3:
    with st.container():
        st.subheader("Photo Gallery")
        num_columns = 3
        num_rows = len(image_descriptions) // num_columns + (len(image_descriptions) % num_columns > 0)

        gallery_cols = st.columns(num_columns)

        for i, (image_filename, description) in enumerate(image_descriptions.items()):
            with gallery_cols[i % num_columns]:
                image_path = f"streamlit-webpage/images/{image_filename}"
                image = Image.open(image_path)
                st.image(image, caption=description, use_column_width=True) 
