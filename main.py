import streamlit as st
import pandas as pd

# Sayfa Ayarları
st.set_page_config(page_title="Hantavirüs Analiz Sistemi", layout="wide")

# Başlık
st.title("🩺 Hantavirüs Görüntü İşleme ve Analiz Uygulaması")
st.write("Web uygulamamıza hoş geldiniz! Sol menüyü kullanarak işlemleri yapabilirsiniz.")

# Yan Menü (Sidebar)
st.sidebar.title("Kontrol Paneli")
secim = st.sidebar.radio("Sayfalar", ["Ana Sayfa & Veri Özeti", "Görüntü İşleme (AI)", "Soru-Cevap"])

# Veriyi Yükleme Denemesi
try:
    df = pd.read_csv("dataset.csv")
    st.sidebar.success("✅ dataset.csv başarıyla yüklendi!")
except Exception as e:
    st.sidebar.error("❌ dataset.csv bulunamadı veya okunamadı!")

# --- Sayfa İçerikleri ---
if secim == "Ana Sayfa & Veri Özeti":
    st.subheader("📊 Veri Seti Genel Analizi")
    if 'df' in locals():
        st.dataframe(df.head())
        st.metric("Toplam Vaka Sayısı", len(df))

elif secim == "Görüntü İşleme (AI)":
    st.subheader("🔬 Hücre / Mikroskop Görüntüsü Analizi")
    uploaded_file = st.file_uploader("Bir Hantavirüs mikroskop görseli yükleyin...", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Yüklenen Görsel", width=400)
        if st.button("AI Analizini Başlat"):
            st.warning("Görüntü işleme modülü (projehanta3.py) entegre ediliyor...")

elif secim == "Soru-Cevap":
    st.subheader("💬 Veri Seti Soru-Cevap Asistanı")
    soru = st.text_input("Veri setiyle ilgili bir soru yazın:")
    if soru:
        st.info("Bu soru nlp_assistant modülüne gönderiliyor...")
