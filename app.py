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

# Bahagian 1: Gambar Lama
st.subheader("📊 Gambar / Carta Asal")
gambar_lama = st.file_uploader("Muat naik gambar asal", type=['png','jpg','jpeg'], key="lama")
if gambar_lama:
    st.image(gambar_lama, use_container_width=True)

st.markdown("---")

# Bahagian 2: Kanvas Lukis
st.subheader("✏️ Sedang Dilukis")

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

canvas_result = st_canvas(
    stroke_width=lebar_pen,
    stroke_color=warna_pen,
    background_color="#FFFFFF",
    height=400,
    drawing_mode=drawing_mode,
    key="canvas_lukis"
)

if canvas_result.image_data is not None:
    st.markdown("---")
    st.subheader("💾 Simpan Hasil")
    
    img = Image.fromarray(canvas_result.image_data)
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    
    butang1, butang2 = st.columns(2)
    with butang1:
        st.download_button(
            label="💾 Simpan ke Telefon",
            data=byte_im,
            file_name="hasil_lukis.png",
            mime="image/png",
            use_container_width=True
        )
    with butang2:
        st.link_button("📤 Hantar ke WhatsApp", "https://wa.me/?text=Lihat hasil analisis saya!", use_container_width=True)

st.markdown("---")

# Bahagian 3: Catatan
st.subheader("💬 Catatan")
catatan = st.text_area("Tulis apa yang anda perhatikan:", height=120, 
                       placeholder="Contoh: Apa beza kedua-dua carta ini? Apa perubahan penting...")

if st.button("✅ Simpan Catatan", type="primary", use_container_width=True):
    st.success("✅ Catatan disimpan!")
