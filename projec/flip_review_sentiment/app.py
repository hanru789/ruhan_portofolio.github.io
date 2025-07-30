import streamlit as st

st.title("Review Sentiment Analysis")

review = st.text_area("Review")

if st.button("Kirim"):
    st.success(f"Terima kasih, {name}! Pesan Anda telah diterima.")




