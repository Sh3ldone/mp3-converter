from PIL import Image
import streamlit as st

st.title("📖Projects")

# Assuming img_contact_form is an image file, you need to load it with Image.open
img_contact_form = Image.open("images/me.png")
img_me = Image.open("images/me.png")

with st.container():
    st.write("---")
    st.header("My Project")
    st.write("##")
    
    image_column, text_column = st.columns((1, 2))
    
    with image_column:
        st.image(img_contact_form)
    
    with text_column:
        st.subheader("I'm a musician, that's why I created this project so that I can easily convert our band's performance into music MP3.")

st.write("If you wish to convert video into mp3 just click here👇")
st.write("[convert here ](https://6a3detmwvyutciekoywziu.streamlit.app/)")

st.subheader("Thank you for visiting my page😉")
