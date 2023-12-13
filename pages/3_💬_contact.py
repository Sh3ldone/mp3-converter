import streamlit as st

st.header(":mailbox: Get In Touch With Me!")

contact_form = """
<form action="https://formsubmit.co/sdacuya@ssct.edu.ph" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="your name" required>
    <input type="email" name="email" placeholder="your email" required>
    <textarea name="message" placeholder="your message here"></textarea>
    <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("pages/style/style.css")
  
with st.container():
    st.write("---")
 
