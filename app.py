import streamlit as st

st.set_page_config(
    page_title="📊 Ruang Analisis Saya",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Ruang Analisis Saya")
st.markdown("---")

# Bahagian 1: Gambar Pertama
st.subheader("📊 Gambar / Carta — Versi Lama")
gambar1 = st.file_uploader("Muat naik gambar pertama", type=['png','jpg','jpeg'], key="gambar1")
if gambar1:
    st.image(gambar1, use_container_width=True)

st.markdown("---")

# Bahagian 2: Gambar Kedua
st.subheader("🎨 Gambar / Carta — Versi Baru")
gambar2 = st.file_uploader("Muat naik gambar kedua", type=['png','jpg','jpeg'], key="gambar2")
if gambar2:
    st.image(gambar2, use_container_width=True)

st.markdown("---")

# Bahagian 3: Catatan
st.subheader("💬 Catatan & Analisis")
catatan = st.text_area("Tulis apa yang anda perhatikan:", height=150,
                       placeholder="Contoh: Apa beza kedua-dua gambar ini? Perubahan apa yang penting?")

if catatan:
    st.download_button(
        label="💾 Simpan Catatan",
        data=catatan,
        file_name="catatan_analisis.txt",
        mime="text/plain"
    )
