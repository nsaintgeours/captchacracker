import streamlit as st

from captcha_cracker_client import crack_captcha

with st.sidebar:
    st.title("Captcha cracker")
    uploaded_file = st.file_uploader(label='Déposez une image ci-dessous :', type=['.jpg', '.png'])

if uploaded_file:
    with st.spinner("Craquage en cours..."):
        text = crack_captcha(img_file=uploaded_file.getvalue())
        st.subheader(f'Résultat : {text}')
