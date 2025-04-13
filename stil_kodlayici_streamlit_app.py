import streamlit as st

st.title("🏛️ Stil Kodlayıcı – Mimari Üslup Tanıma")
st.write("📷 Lütfen bir mimari yapı görseli yükleyin.")

uploaded_file = st.file_uploader("Görsel Yükle", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Yüklenen Görsel", use_column_width=True)
    st.success("Tahmin: 🏰 Baroque (örnek)")
