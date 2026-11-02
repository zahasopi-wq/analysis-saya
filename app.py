import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import io

st.set_page_config(page_title="📊 Carta & Lukis", layout="wide")
st.title("📊 Carta & Lukis Saya")
st.markdown("---")

# === BAHAGIAN 1: MUAT NAIK GAMBAR ===
st.subheader("📊 Carta Rujukan")
gambar_carta = st.file_uploader("Muat naik carta awak", type=['png','jpg','jpeg'])
if gambar_carta:
    st.image(gambar_carta, use_container_width=True)

st.markdown("---")

# === BAHAGIAN 2: KANVAS LUKIS ===
st.subheader("✏️ Lukis & Tanda Di Sini")

col1, col2 = st.columns(2)
with col1:
    warna = st.color_picker("Warna", "#FF0000")
with col2:
    saiz = st.slider("Saiz Pen", 1, 15, 3)

canvas = st_canvas(
    stroke_width=saiz,
    stroke_color=warna,
    background_color="#FFFFFF",
    height=350,
    drawing_mode="freedraw",
    key="lukis"
)

# === SIMPAN HASIL ===
if canvas.image_data is not None:
    st.markdown("---")
    st.subheader("💾 Simpan Hasil")
    
    img = Image.fromarray(canvas.image_data.astype('uint8'), 'RGBA')
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    fail = buf.getvalue()
    
    st.download_button(
        label="💾 Simpan Gambar Lukis",
        data=fail,
        file_name="carta_saya.png",
        mime="image/png",
        use_container_width=True
    )

st.markdown("---")

# === CATATAN ===
st.subheader("📝 Catatan")
st.text_area("Tulis nota di sini...", height=120, key="catatan")
