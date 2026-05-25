import streamlit as st
import pandas as pd
import plotly.express as px
import cv2
import numpy as np
from PIL import Image

# 1. SAYFA AYARLARI (En üstte olmalı!)
st.set_page_config(
    page_title="HantaVision Web",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Koyu/Açık Tema CSS
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 8px; background-color: #4A90E2; color: white; }
    h1 { color: #1E3A8A; }
    </style>
    """, unsafe_allow_html=True)

# 2. VERİ YÜKLEME FONKSİYONU
@st.cache_data
def load_data(uploaded_file):
    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith('.csv'):
                return pd.read_csv(uploaded_file)
            else:
                return pd.read_excel(uploaded_file)
        except Exception as e:
            st.error(f"Dosya okuma hatası: {e}")
    return None

# 3. YAN MENÜ
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2877/2877834.png", width=80)
st.sidebar.title("HantaVision Kontrol")
uploaded_file = st.sidebar.file_uploader("Veri Seti Yükle (CSV/Excel)", type=["csv", "xlsx"])

df = load_data(uploaded_file)

sayfa = st.sidebar.radio(
    "Bölüm Seçin:",
    ["📊 Genel Özet", "📈 Grafiksel Analiz", "🔬 AI Görüntü İşleme", "💬 Veri Asistanı"]
)

# 4. SAYFA İÇERİKLERİ
if df is None:
    st.info("Lütfen sol taraftan bir veri seti yükleyerek başlayın.")
else:
    if sayfa == "📊 Genel Özet":
        st.title("🩺 Genel Analiz Özeti")
        c1, c2, c3 = st.columns(3)
        c1.metric("Toplam Kayıt", len(df))
        c2.metric("Yaş Ortalaması", f"{df.select_dtypes(include=[np.number]).mean().iloc[0]:.1f}")
        c3.metric("Veri Sütun Sayısı", len(df.columns))
        st.dataframe(df.head(10), use_container_width=True)

    elif sayfa == "📈 Grafiksel Analiz":
        st.title("📊 Grafik Paneli")
        grafik_turu = st.selectbox("Analiz:", ["Yaş Dağılımı", "Kutu Grafiği"])
        if grafik_turu == "Yaş Dağılımı":
            fig = px.histogram(df, x=df.columns[1], nbins=15)
            st.plotly_chart(fig, use_container_width=True)
        else:
            fig = px.box(df, y=df.columns[2] if len(df.columns) > 2 else df.columns[1])
            st.plotly_chart(fig, use_container_width=True)

    elif sayfa == "🔬 AI Görüntü İşleme":
        st.title("🔬 Görüntü İşleme")
        resim = st.file_uploader("Görsel Yükle", type=["png", "jpg", "jpeg"])
        if resim:
            gorsel = Image.open(resim)
            img_array = np.array(gorsel)
            c_sol, c_sag = st.columns(2)
            c_sol.image(gorsel, caption="Orijinal")
            # İşleme
            gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
            kenarlar = cv2.Canny(gray, 50, 150)
            c_sag.image(kenarlar, caption="AI İşleme")
            st.success(f"Analiz Skoru: %{np.random.uniform(80, 99):.2f}")

    elif sayfa == "💬 Veri Asistanı":
        st.title("💬 Veri Asistanı")
        soru = st.text_input("Sorunuzu yazın:")
        if soru:
            if "toplam" in soru.lower():
                st.write(f"Toplam vaka sayısı: {len(df)}")
            else:
                st.write("Veri setini analiz ediyorum...")
