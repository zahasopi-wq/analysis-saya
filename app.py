import streamlit as st

st.set_page_config(page_title="📊 Analisis Saya", page_icon="📊", layout="wide")
st.title("📊 Ruang Analisis Saya")
st.markdown("---")

# Gambar 1
st.subheader("📊 Gambar / Carta — Versi Lama")
gambar1 = st.file_uploader("Muat naik gambar pertama", type=['png','jpg','jpeg'])
if gambar1:
    st.image(gambar1, use_container_width=True)

st.markdown("---")

# Gambar 2
st.subheader("🎨 Gambar / Carta — Versi Baru")
gambar2 = st.file_uploader("Muat naik gambar kedua", type=['png','jpg','jpeg'])
if gambar2:
    st.image(gambar2, use_container_width=True)

st.markdown("---")

# Catatan
st.subheader("💬 Catatan & Analisis")
catatan = st.text_area("Tulis apa yang anda perhatikan:", height=150)
if catatan:
    st.download_button("💾 Simpan Catatan", data=catatan, file_name="catatan_analisis.txt")
