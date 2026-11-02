import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import io

st.set_page_config(
    page_title="🎨 Ruang Lukis & Analisis",
    page_icon="🎨",
    layout="wide"
)

st.title("🎨 Ruang Lukis & Analisis Saya")
st.markdown("---")

# Bahagian 1: Gambar Rujukan
st.subheader("📊 Gambar / Carta Rujukan")
gambar_lama = st.file_uploader("Muat naik gambar rujukan", type=['png','jpg','jpeg'], key="lama")
if gambar_lama:
    st.image(gambar_lama, caption="Gambar Rujukan — Lukis di bawah ikut ini", use_container_width=True)

st.markdown("---")

# Bahagian 2: Kanvas Lukis Kosong
st.subheader("✏️ Lukis Di Sini")

drawing_mode = st.selectbox(
    "Alat lukis:",
    ["freedraw", "line", "rect", "circle", "transform"],
    key="mode"
)

col1, col2 = st.columns(2)
with col1:
    lebar_pen = st.slider("Lebar pen:", 1, 25, 3)
with col2:
    warna_pen = st.color_picker("Warna pen:", "#FF0000")

st.info("💡 Lukis terus di atas kanvas putih ini")

canvas_result = st_canvas(
    stroke_width=lebar_pen,
    stroke_color=warna_pen,
    background_color="#FFFFFF",
    height=400,
    drawing_mode=drawing_mode,
    key="canvas_lukis"
)

st.markdown("---")

# Bahagian 3: Catatan
st.subheader("💬 Catatan")
catatan = st.text_area("Tulis apa yang anda perhatikan:", height=120,
                       placeholder="Contoh: Bandingkan gambar di atas dengan lukisan saya di bawah...")

if st.button("✅ Simpan Catatan", type="primary", use_container_width=True):
    st.success("✅ Catatan disimpan!")
