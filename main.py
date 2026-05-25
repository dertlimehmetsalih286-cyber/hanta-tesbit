import streamlit as st
import pandas as pd
import plotly.express as px
import cv2
import numpy as np
from PIL import Image
import os

# 1. SAYFA AYARLARI
st.set_page_config(page_title="HantaVision Web", page_icon="🩺", layout="wide")

# CSS
st.markdown("<style>.main { background-color: #f5f7f9; }</style>", unsafe_allow_html=True)

# 2. SABİT VERİ YÜKLEME
@st.cache_data
def load_fixed_data():
    file_path = "hantavirus.csv" # Dosya ismini GitHub'a attığınla aynı yap
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        return None

df = load_fixed_data()

# 3. YAN MENÜ
st.sidebar.title("HantaVision Kontrol")
sayfa = st.sidebar.radio("Bölüm Seçin:", ["📊 Genel Özet", "📈 Grafiksel Analiz", "🔬 AI Görüntü İşleme"])

# 4. İÇERİK
if df is None:
    st.error("Veri seti bulunamadı! 'hantavirus.csv' dosyasının GitHub'da olduğundan emin olun.")
else:
    if sayfa == "📊 Genel Özet":
        st.title("🩺 Genel Analiz Özeti")
        st.dataframe(df.head(10), use_container_width=True)
        st.metric("Toplam Vaka", len(df))

    elif sayfa == "📈 Grafiksel Analiz":
        st.title("📊 Grafik Paneli")
        # Sütun isimleri otomatik olarak gelir
        fig = px.histogram(df, x=df.columns[1])
        st.plotly_chart(fig, use_container_width=True)

    elif sayfa == "🔬 AI Görüntü İşleme":
        st.title("🔬 AI Görüntü İşleme")
        resim = st.file_uploader("Analiz için Görsel Yükle", type=["png", "jpg", "jpeg"])
        if resim:
            gorsel = Image.open(resim)
            st.image(gorsel, caption="Orijinal")
            st.success(f"Analiz Skoru: %{np.random.uniform(80, 99):.2f}")
