import requests as rq
import streamlit as st
from content import *


def load_animation(url):
    """
    Load a Lottie animation from a URL.
    Parameters: url (str): The URL of the Lottie animation JSON.
    Returns: dict or None: The JSON representation of the animation or None if the request fails.
    """
    response = rq.get(url)
    if response.status_code != 200:
        return None
    return response.json()


def local_css(file_name):
    """
    Inject local CSS styles into a Streamlit app.
    Parameters: file_name (str): The path to the CSS file.
    Example usage: local_css("path/to/your/style.css")
    """
    with open(file_name, "r") as file:
        css = file.read()
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


def display_content(selected_option):
    for key, project_details in portfolio.items():
        if selected_option == key:
            st.markdown(project_details[0], unsafe_allow_html=True)


