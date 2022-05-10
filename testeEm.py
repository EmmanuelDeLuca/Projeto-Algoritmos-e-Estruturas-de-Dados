from PIL import Image
import streamlit as st
image = Image.open('foto.png')

st.image(image, caption='Sunrise by the mountains')