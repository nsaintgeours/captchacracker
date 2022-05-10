import streamlit as st

from captcha_cracker import CaptchaCracker

cracker = CaptchaCracker()

with st.sidebar:
    st.title("Captcha cracker")
    uploaded_file = st.file_uploader(label='Déposez une image ci-dessous :', type=['.jpg', '.png'])

if uploaded_file:
    with st.spinner("Craquage en cours..."):
        text, input_img, processed_img = cracker.crack(image_bytes=uploaded_file.getvalue())
        st.subheader(f'Résultat : {text}')
        st.pyplot(fig=cracker.plot(input_img, processed_img))
