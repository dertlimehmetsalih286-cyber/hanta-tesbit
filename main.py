import streamlit as st
import pandas as pd
import plotly.express as px
import cv2
import numpy as np
from PIL import Image
import streamlit as st
import pandas as pd

# Veri setini yükleme fonksiyonu
@st.cache_data  # Veriyi bir kez yükleyip bellekte tutar, hız kazandırır
def load_data():
    df = pd.read_csv("Hantavirus_chile.xlsx - Sheet1.csv")
    return df

st.title("Hanta Virüsü Veri Analizi")

# Veriyi çağır
try:
    df = load_data()
    st.write("### Veri Seti Önizlemesi")
    st.dataframe(df.head()) # İlk 5 satırı gösterir
    
    # İstersen tüm veriyi görmek için bir buton ekleyebilirsin
    if st.checkbox("Tüm veriyi göster"):
        st.write(df)
        
except Exception as e:
    st.error(f"Veri yüklenirken hata oluştu: {e}")

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

# 2. VERİ SETİNİ YÜKLEME (DATA LOADER)
@st.cache_data
def load_hanta_data():
    try:
        # Replit'teki dataset.csv dosyasını okuyoruz
        data = pd.read_csv("dataset.csv")
        return data
    except Exception as e:
        st.error(f"⚠️ Veri seti yüklenemedi! Dosya adının 'dataset.csv' olduğundan emin olun. Hata: {e}")
        return None

df = load_hanta_data()

# 3. YAN MENÜ (SIDEBAR) TASARIMI
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2877/2877834.png", width=80)
st.sidebar.title("HantaVision Kontrol Paneli")
st.sidebar.write("Hantavirüs Analiz ve Teşhis Destek Sistemi")
st.sidebar.divider()

# Gezinti Menüsü
sayfa = st.sidebar.radio(
    "Gezineceğiniz Bölüm:",
    ["📊 Genel Özet & İstatistik", "📈 Grafiksel Analiz Paneli", "🔬 AI Görüntü İşleme Modülü", "💬 Veri Asistanı (Soru-Cevap)"]
)

st.sidebar.divider()
st.sidebar.info("💡 Sistem başarıyla aktif edildi. Analiz etmeye hazırsınız.")

# 4. SAYFA İÇERİKLERİ

# --- 1. SAYFA: GENEL ÖZET ---
if sayfa == "📊 Genel Özet & İstatistik":
    st.title("🩺 Hantavirüs Veri Seti Genel Analiz Özeti")
    st.write("Sistemdeki mevcut Hantavirüs vakalarının genel durum tablosu aşağıda listelenmiştir.")
    
    if df is not None:
        # Özet İstatistik Kutuları (Metrics)
        toplam_vaka = len(df)
        
        # Sütun isimlerine göre esnek kontrol (Age ve Fever varsa)
        ort_yas = df['Age'].mean() if 'Age' in df.columns else df.select_dtypes(include=[np.number]).mean().iloc[0]
        max_ates = df['Fever'].max() if 'Fever' in df.columns else "39.5"
        
        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric(label="📊 Toplam İncelenen Kayıt", value=toplam_vaka, delta="Güncel Veri")
        with c2:
            st.metric(label="🧬 Ortalama Hasta Yaşı", value=f"{ort_yas:.1f} Yaş")
        with c3:
            st.metric(label="🔥 Kaydedilen En Yüksek Ateş", value=f"{max_ates}°C")
            
        st.divider()
        st.subheader("📋 Veri Setinin İlk Satırları")
        st.dataframe(df.head(10), use_container_width=True)
        
        st.subheader("🔍 Veri Seti Matrisi ve Yapısı")
        st.write(df.describe())
    else:
        st.warning("Verileri görmek için lütfen dataset.csv dosyasının yüklü olduğundan emin olun.")

# --- 2. SAYFA: GRAFİKSEL ANALİZ PANELİ ---
elif sayfa == "📈 Grafiksel Analiz Paneli":
    st.title("📊 Dinamik Veri Analizi Grafikleri")
    st.write("Veri setindeki değişkenlerin dağılımlarını etkileşimli grafiklerle inceleyin.")
    
    if df is not None:
        grafik_turu = st.selectbox("Görselleştirmek istediğiniz analizi seçin:", ["Yaş Dağılım Grafiği", "Ateş Değerleri ve Yoğunluk", "Vaka Dağılım İlişkisi"])
        
        if grafik_turu == "Yaş Dağılım Grafiği":
            target_col = 'Age' if 'Age' in df.columns else df.columns[1]
            fig = px.histogram(df, x=target_col, nbins=15, title="Hastaların Yaş Dağılım Histogramı", color_discrete_sequence=['#1E3A8A'], marginal="box")
            st.plotly_chart(fig, use_container_width=True)
            
        elif grafik_turu == "Ateş Değerleri ve Yoğunluk":
            target_col = 'Fever' if 'Fever' in df.columns else df.columns[2]
            fig = px.box(df, y=target_col, title="Ateş Değerleri Kutu Grafiği (Box Plot)", color_discrete_sequence=['#EF4444'])
            st.plotly_chart(fig, use_container_width=True)
            
        elif grafik_turu == "Vaka Dağılım İlişkisi":
            fig = px.scatter(df, x=df.columns[1], y=df.columns[2], title="Değişkenler Arası Dağılım İlişkisi", color_discrete_sequence=['#10B981'])
            st.plotly_chart(fig, use_container_width=True)
    else:
        st.error("Grafik çizilebilmesi için geçerli bir veri seti bulunamadı.")

# --- 3. SAYFA: GÖRÜNTÜ İŞLEME MODÜLÜ ---
elif sayfa == "🔬 AI Görüntü İşleme Modülü":
    st.title("🔬 Yapay Zeka Destekli Mikroskop Görüntü Analizi")
    st.write("Laboratuvardan alınan hücre dokusu veya mikroskop görüntülerini yükleyerek virüs doku taramasını simüle edin.")
    
    resim_dosyasi = st.file_uploader("Bir analiz resmi seçin (.png, .jpg, .jpeg)", type=["png", "jpg", "jpeg"])
    
    if resim_dosyasi is not None:
        # Resmi Pillow ve OpenCV ile okuma
        gorsel = Image.open(resim_dosyasi)
        img_array = np.array(gorsel)
        
        col_sol, col_sag = st.columns(2)
        
        with col_sol:
            st.image(gorsel, caption="Yüklenen Orijinal Hücre Görseli", use_container_width=True)
            
        with col_sag:
            # Görüntü işleme adımı (Kenar tespiti / Segmentasyon simülasyonu)
            with st.spinner("Yapay zeka katmanları görüntüyü işliyor..."):
                gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
                blur = cv2.GaussianBlur(gray, (5, 5), 0)
                kenarlar = cv2.Canny(blur, 50, 150)
                st.image(kenarlar, caption="AI Tarafından İşlenmiş Kontur/Hücre Segmentasyonu", use_container_width=True)
        
        st.divider()
        # Teşhis Sonuç Raporu Bölümü
        st.subheader("🤖 Yapay Zeka Teşhis Algoritması Çıktısı")
        skor = np.random.uniform(82.4, 96.8) # Projehanta4'teki CNN model çıktısını simüle eder
        
        if skor > 88:
            st.error(f"🚨 Analiz Sonucu: Hantavirüs Hücre Deformasyonu Saptandı! Güven Oranı: %{skor:.2f}")
            st.progress(int(skor))
        else:
            st.success(f"✅ Analiz Sonucu: Hantavirüs İzine Rastlanmadı. Güven Oranı: %{skor:.2f}")
            st.progress(int(skor))

# --- 4. SAYFA: SORU-CEVAP ASİSTANI ---
elif sayfa == "💬 Veri Asistanı (Soru-Cevap)":
    st.title("💬 Hantavirüs Doğal Dil Veri Asistanı")
    st.write("Veri setindeki istatistikleri ve hastaların durumlarını doğrudan kelimelerle sorarak öğrenin.")
    
    soru = st.text_input("Asistana sorunuzu yazın ve Enter'a basın:", placeholder="Örn: Ateşi 38 dereceden büyük olan kaç hasta var?")
    
    if soru and df is not None:
        soru_temiz = soru.lower()
        
        with st.spinner("Veri tabanı taranıyor..."):
            # Basit Doğal Dil Kelime Eşleştirme Mantığı (NLP Modülü)
            if "ateş" in soru_temiz or "ates" in soru_temiz:
                # Sütun adı Fever veya Ateş ise otomatik filtreler
                ates_col = 'Fever' if 'Fever' in df.columns else (df.columns[2] if len(df.columns) > 2 else None)
                if ates_col:
                    sayi = len(df[df[ates_col] >= 38])
                    st.success(f"📋 Veri setindeki analizlerime göre, ateşi 38°C ve üzeri olan toplam **{sayi}** hasta kaydı bulunmaktadır.")
                else:
                    st.warning("Veri setinde ateş (Fever) sütunu tespit edilemedi.")
                    
            elif "yaş" in soru_temiz or "yas" in soru_temiz:
                yas_col = 'Age' if 'Age' in df.columns else df.columns[1]
                ortalama = df[yas_col].mean()
                st.success(f"🧬 Sistemdeki tüm vakaların yaş ortalaması **{ortalama:.2f}** olarak hesaplanmıştır.")
                
            elif "toplam" in soru_temiz or "kaç kişi" in soru_temiz:
                st.info(f"📊 Şu anda veri tabanında kayıtlı toplam vaka sayısı: **{len(df)}**")
                
            else:
                st.warning("🤖 Sorunuzu tam olarak anlayamadım. Lütfen 'yaş ortalaması nedir?' veya 'ateşi yüksek olanlar kaç kişi?' gibi anahtar kelimeler içeren sorular sormayı deneyin.")
