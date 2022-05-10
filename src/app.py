import io

import streamlit as st

from captcha_cracker import CaptchaCracker

cracker = CaptchaCracker()

with st.sidebar:
    st.title("Captcha cracker")
    uploaded_file = st.file_uploader(label='Déposez une image ci-dessous :', type=['.jpg', '.png'])

if uploaded_file:
    with st.spinner("Craquage en cours..."):
        print(type(uploaded_file.getvalue()))
        image_bytes = io.BytesIO(uploaded_file.getvalue())
        text, input_img, processed_img = cracker.crack(image_file=image_bytes)
        st.subheader(f'Résultat : {text}')
        st.pyplot(fig=cracker.plot(input_img, processed_img))
