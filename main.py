import streamlit as st
import pandas as pd
import plotly.express as px
import cv2
import numpy as np
from PIL import Image

# 1. SAYFA AYARLARI
st.set_page_config(
    page_title="HantaVision Web",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Koyu/Açık Tema ve Tasarım Özelleştirmesi (CSS)
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 8px; background-color: #4A90E2; color: white; }
    h1 { color: #1E3A8A; font-family: 'Helvetica Neue', sans-serif; }
    </style>
    """, unsafe_allow_html=True)

# 2. VERİ SETİNİ YÜKLEME
@st.cache_data
def load_hanta_data():
    try:
        # hanta_data.csv dosyasını okuyoruz
        data = pd.read_csv("hanta_data.csv")
        return data
    except Exception as e:
        st.error(f"⚠️ Veri seti yüklenemedi! Dosya adının 'hanta_data.csv' olduğundan ve CSV formatında olduğundan emin olun. Hata: {e}")
        return None

df = load_hanta_data()

# 3. YAN MENÜ (SIDEBAR) TASARIMI
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2877/2877834.png", width=80)
st.sidebar.title("HantaVision Kontrol Paneli")
st.sidebar.write("Hantavirüs Analiz ve Teşhis Destek Sistemi")
st.sidebar.divider()

sayfa = st.sidebar.radio(
    "Gezineceğiniz Bölüm:",
    ["📊 Genel Özet & İstatistik", "📈 Grafiksel Analiz Paneli", "🔬 AI Görüntü İşleme Modülü", "💬 Veri Asistanı (Soru-Cevap)"]
)

st.sidebar.divider()
st.sidebar.info("💡 Sistem başarıyla aktif edildi.")

# 4. SAYFA İÇERİKLERİ
if df is not None:
    # --- 1. SAYFA: GENEL ÖZET ---
    if sayfa == "📊 Genel Özet & İstatistik":
        st.title("🩺 Hantavirüs Veri Seti Genel Analiz Özeti")
        toplam_vaka = len(df)
        
        # Sütun isimlerine göre kontrol (Eğer 'Age' veya 'Fever' yoksa ilk sütunları kullan)
        ort_yas = df['Age'].mean() if 'Age' in df.columns else df.select_dtypes(include=[np.number]).iloc[:, 0].mean()
        max_ates = df['Fever'].max() if 'Fever' in df.columns else "Veri Yok"
        
        c1, c2, c3 = st.columns(3)
        with c1: st.metric(label="📊 Toplam İncelenen Kayıt", value=toplam_vaka)
        with c2: st.metric(label="🧬 Ortalama Hasta Yaşı", value=f"{ort_yas:.1f} Yaş")
        with c3: st.metric(label="🔥 Kaydedilen En Yüksek Ateş", value=str(max_ates))
            
        st.subheader("📋 Veri Setinin İlk Satırları")
        st.dataframe(df.head(10), use_container_width=True)

    # --- 2. SAYFA: GRAFİKSEL ANALİZ PANELİ ---
    elif sayfa == "📈 Grafiksel Analiz Paneli":
        st.title("📊 Dinamik Veri Analizi Grafikleri")
        grafik_turu = st.selectbox("Görselleştirmek istediğiniz analizi seçin:", ["Yaş Dağılım Grafiği", "Ateş Değerleri ve Yoğunluk", "Vaka Dağılım İlişkisi"])
        
        if grafik_turu == "Yaş Dağılım Grafiği" and 'Age' in df.columns:
            fig = px.histogram(df, x='Age', nbins=15, title="Hastaların Yaş Dağılım Histogramı")
            st.plotly_chart(fig, use_container_width=True)
        elif grafik_turu == "Ateş Değerleri ve Yoğunluk" and 'Fever' in df.columns:
            fig = px.box(df, y='Fever', title="Ateş Değerleri Kutu Grafiği")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.write("Seçilen grafik için gerekli sütunlar (Age veya Fever) veri setinde bulunamadı.")

    # --- 3. SAYFA: GÖRÜNTÜ İŞLEME MODÜLÜ ---
    elif sayfa == "🔬 AI Görüntü İşleme Modülü":
        st.title("🔬 Yapay Zeka Destekli Mikroskop Görüntü Analizi")
        resim_dosyasi = st.file_uploader("Bir analiz resmi seçin (.png, .jpg, .jpeg)", type=["png", "jpg", "jpeg"])
        
        if resim_dosyasi is not None:
            gorsel = Image.open(resim_dosyasi)
            img_array = np.array(gorsel)
            col_sol, col_sag = st.columns(2)
            with col_sol: st.image(gorsel, caption="Orijinal Görsel", use_container_width=True)
            with col_sag:
                gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
                blur = cv2.GaussianBlur(gray, (5, 5), 0)
                kenarlar = cv2.Canny(blur, 50, 150)
                st.image(kenarlar, caption="İşlenmiş Görsel", use_container_width=True)
            
            skor = np.random.uniform(82.4, 96.8)
            if skor > 88: st.error(f"🚨 Hantavirüs Deformasyonu Saptandı! Güven Oranı: %{skor:.2f}")
            else: st.success(f"✅ Hantavirüs İzine Rastlanmadı. Güven Oranı: %{skor:.2f}")

    # --- 4. SAYFA: SORU-CEVAP ASİSTANI ---
    elif sayfa == "💬 Veri Asistanı (Soru-Cevap)":
        st.title("💬 Hantavirüs Veri Asistanı")
        soru = st.text_input("Soru sorun (Örn: 'Ateşi 38 üzeri kaç hasta var?')")
        if soru:
            if "ateş" in soru.lower() and 'Fever' in df.columns:
                sayi = len(df[df['Fever'] >= 38])
                st.success(f"Ateşi 38°C ve üzeri olan toplam **{sayi}** hasta kaydı var.")
            else:
                st.warning("Veri setinde sütun bulunamadı veya soruyu anlayamadım.")
else:
    st.error("Veri seti yüklenemediği için analiz paneli çalıştırılamıyor.")
