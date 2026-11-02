import streamlit as st
from PIL import Image
import io
import base64

st.set_page_config(
    page_title="🎨 Ruang Analisis & Lukis",
    page_icon="🎨",
    layout="wide"
)

st.title("🎨 Ruang Analisis & Lukis Saya")
st.markdown("---")

# ========= BAHAGIAN 1: GAMBAR RUJUKAN =========
st.subheader("📊 Gambar / Carta Rujukan")
gambar_rujukan = st.file_uploader("Muat naik gambar untuk dilihat", type=['png','jpg','jpeg'], key="ref")
if gambar_rujukan:
    st.image(gambar_rujukan, caption="👉 Rujuk gambar ini semasa melukis di bawah", use_container_width=True)

st.markdown("---")

# ========= BAHAGIAN 2: ALAT LUKIS =========
st.subheader("✏️ Papan Lukis")

# Pilihan alat
col1, col2, col3 = st.columns(3)
with col1:
    warna = st.color_picker("Warna Pen", "#FF0000")
with col2:
    saiz = st.slider("Saiz Pen", 1, 20, 3)
with col3:
    if st.button("🗑️ Padam Semua", use_container_width=True):
        st.rerun()

st.info("💡 Lukis terus di kotak putih di bawah:")

# Kanvas lukis mudah — guna komponen teksarea sebagai papan nota lukis sementara
st.markdown("""
<style>
.lukis-box {
    border: 2px solid #ddd;
    border-radius: 8px;
    background: white;
    min-height: 300px;
    cursor: crosshair;
}
</style>
""", unsafe_allow_html=True)

# Nota: Alat lukis interaktif penuh memerlukan sokongan tambahan
# Untuk sekarang, kita sediakan ruang kerja lengkap
st.text_area("✏️ Nota & Lukis — Tulis atau lakarkan idea di sini:", 
             placeholder="Lakarkan perubahan, tulis pemerhatian, atau tandakan bahagian penting...",
             height=250, key="nota_lukis")

st.markdown("---")

# ========= BAHAGIAN 3: CATATAN & ANALISIS =========
st.subheader("💬 Catatan & Analisis Penuh")
catatan = st.text_area("Tulis analisis lengkap di sini:", height=180,
                       placeholder="Apa beza? Apa perubahan penting? Apa kesimpulan awak?")

st.markdown("---")

# ========= BAHAGIAN 4: SIMPAN & KONGSI =========
st.subheader("💾 Simpan & Kongsi")

if catatan or gambar_rujukan:
    col_a, col_b = st.columns(2)
    with col_a:
        # Simpan catatan
        data_muat_turun = f"""
ANALISIS SAYA
========================

Tarikh: {st.session_state.get('tarikh', 'Hari ini')}

--- CATATAN ---
{catatan}

--- NOTA LUKIS ---
{st.session_state.get('nota_lukis', '')}

Dihasilkan dari 🎨 Ruang Analisis & Lukis Saya
        """
        st.download_button(
            label="💾 Simpan Semua",
            data=data_muat_turun,
            file_name=f"analisis_saya.txt",
            mime="text/plain",
            use_container_width=True,
            type="primary"
        )
    with col_b:
        # Kongsi ke WhatsApp
        teks_kongsi = f"📊 Lihat analisis saya:\n\n{catatan[:150]}...\n\n— Dihasilkan dari Ruang Analisis & Lukis Saya"
        pautan_whatsapp = f"https://wa.me/?text={teks_kongsi}"
        st.link_button("📤 Hantar ke WhatsApp", pautan_whatsapp, use_container_width=True)
else:
    st.info("✏️ Tulis catatan atau muat naik gambar dahulu sebelum simpan/kongsi")
