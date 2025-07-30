import streamlit as st

st.title("Form Kontak")

name = st.text_input("Nama Anda")
email = st.text_input("Email")
message = st.text_area("Pesan")

if st.button("Kirim"):
    st.success(f"Terima kasih, {name}! Pesan Anda telah diterima.")
