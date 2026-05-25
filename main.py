import streamlit as st
import time

# --- 1. SAYFA AYARLARI VE MODERN TASARIM (CSS) ---
st.set_page_config(page_title="Hantavirus Risk Analyzer", page_icon="🛡️", layout="wide", initial_sidebar_state="expanded")

# Streamlit'in standart görünümünü modern ve temiz bir hale getirmek için özel CSS
st.markdown("""
    <style>
    /* Üst menüyü ve altbilgiyi gizle */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Ana kapsayıcının boşluklarını ayarla */
    .block-container {
        padding-top: 2rem; 
        padding-bottom: 2rem;
        max-width: 1200px;
    }
    
    /* Butonları modernleştir */
    .stButton>button {
        width: 100%; 
        border-radius: 8px; 
        font-weight: 600; 
        padding: 0.6rem 1rem;
        transition: all 0.3s;
    }
    
    /* Özel Risk Rozetleri */
    .risk-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 6px 16px; 
        border-radius: 20px; 
        font-weight: 700; 
        font-size: 14px;
        margin-bottom: 15px;
        box-shadow: inset 0 1px 2px rgba(0,0,0,0.05);
    }
    .risk-low {background-color: #ecfdf5; color: #047857; border: 1px solid #a7f3d0;}
    .risk-medium {background-color: #fffbeb; color: #b45309; border: 1px solid #fde68a;}
    .risk-high {background-color: #fef2f2; color: #b91c1c; border: 1px solid #fecaca;}
    
    /* Kart görünümü oluşturma */
    .custom-card {
        background-color: white;
        padding: 24px;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    </style>
""", unsafe_allow_html=True)


# --- 2. SOL MENÜ (SIDEBAR) ---
with st.sidebar:
    st.markdown("### 🛡️ Hantavirus")
    st.markdown("<p style='color: #64748b; font-size: 14px; margin-top: -15px;'>Risk Analyzer</p>", unsafe_allow_html=True)
    st.divider()
    
    # Menü Seçenekleri
    menu = st.radio(
        "Navigasyon", 
        ["🔍 Analyzer", "🕒 History", "📊 Statistics"], 
        label_visibility="collapsed"
    )
    
    st.divider()
    # Profil Alanı
    st.markdown("""
        <div style='background-color: #f1f5f9; padding: 10px; border-radius: 8px; display: flex; align-items: center; gap: 10px;'>
            <div style='width: 32px; height: 32px; background-color: #cbd5e1; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; color: #475569;'>H</div>
            <div>
                <p style='margin: 0; font-size: 14px; font-weight: bold; color: #1e293b;'>Hantavirus Risk</p>
                <p style='margin: 0; font-size: 12px; color: #64748b;'>demo@workspace.com</p>
            </div>
        </div>
    """, unsafe_allow_html=True)


# --- 3. ANA SAYFALAR ---

if menu == "🔍 Analyzer":
    st.title("Risk Assessment")
    st.markdown("<p style='color: #64748b; font-size: 18px;'>Upload clinical or environmental photographs for AI-powered Hantavirus risk analysis.</p>", unsafe_allow_html=True)
    st.markdown("---")

    # İki Kolonlu Düzen
    col1, col2 = st.columns([1.1, 1], gap="large")

    with col1:
        st.markdown("### Image Upload")
        st.markdown("<p style='color: #64748b; font-size: 14px;'>Select a clear, well-lit photo of the environment or clinical signs.</p>", unsafe_allow_html=True)
        
        # Dosya Yükleyici
        uploaded_file = st.file_uploader("Upload Image", type=['png', 'jpg', 'jpeg'], label_visibility="collapsed")
        
        if uploaded_file is not None:
            st.image(uploaded_file, use_container_width=True, caption="Seçilen Görüntü")
        else:
            # Görsel bir yükleme alanı simülasyonu
            st.markdown("""
                <div style="border: 2px dashed #cbd5e1; border-radius: 12px; padding: 40px 20px; text-align: center; background-color: #f8fafc; margin-bottom: 15px;">
                    <h3 style="color: #94a3b8; margin-bottom: 5px;">📷 Fotoğraf Yükleyin</h3>
                    <p style="color: #94a3b8; font-size: 12px;">JPEG, PNG (Max 10MB)</p>
                </div>
            """, unsafe_allow_html=True)
        
        # Klinik Notlar
        notes = st.text_area("Clinical Notes (Optional)", placeholder="Add any clinical observations or context about the patient/environment...", height=100)
        
        # Analiz Butonu
        run_btn = st.button("🚀 Run Assessment", type="primary", use_container_width=True)

    with col2:
        if run_btn:
            if uploaded_file is None:
                st.error("⚠️ Lütfen analizi başlatmadan önce bir fotoğraf yükleyin.")
            else:
                # Yapay Zeka Bekleme Simülasyonu
                with st.spinner("Evaluating risk factors and extracting data..."):
                    time.sleep(2) # Burada gerçek yapay zeka kodun çalışacak
                
                # Başarılı Sonuç Ekranı
                st.markdown("### Assessment Complete")
                st.markdown("<p style='color: #64748b; font-size: 14px;'>Today</p>", unsafe_allow_html=True)
                
                st.markdown('<div class="risk-badge risk-low">✅ Low Risk</div>', unsafe_allow_html=True)
                
                st.markdown("#### Summary")
                st.info("No direct environmental indicators of recent rodent activity (fresh droppings, gnaw marks) were detected. The image quality is adequate for assessment. This indicates a very low immediate risk. Maintain standard environmental hygiene practices.")
                
                st.markdown("---")
                
                # Metrikler
                m1, m2 = st.columns(2)
                with m1:
                    st.markdown("<p style='font-size: 14px; font-weight: 600; color: #1e293b; margin-bottom: 0;'>Confidence Score</p>", unsafe_allow_html=True)
                    st.markdown("<p style='font-size: 32px; font-weight: 800; color: #2563eb;'>98%</p>", unsafe_allow_html=True)
                with m2:
                    st.markdown("<p style='font-size: 14px; font-weight: 600; color: #1e293b; margin-bottom: 0;'>Confidence Level</p>", unsafe_allow_html=True)
                    st.markdown("<p style='font-size: 24px; font-weight: 700; color: #047857;'>High</p>", unsafe_allow_html=True)
                
                # İlerleme Çubuğu
                st.markdown("**AI Confidence**")
                st.progress(98)
        else:
            # Boş Durum (Placeholder)
            st.markdown("### Assessment Complete")
            st.markdown("""
                <div style="padding: 50px 20px; text-align: center; border: 2px dashed #e2e8f0; border-radius: 12px; background-color: #f8fafc; margin-top: 20px;">
                    <h4 style="color: #64748b; margin-bottom: 10px;">Awaiting Input</h4>
                    <p style="color: #94a3b8; font-size: 14px;">Upload a photo and run the assessment to see detailed AI analysis results here.</p>
                </div>
            """, unsafe_allow_html=True)

elif menu == "🕒 History":
    st.title("Analysis History")
    st.markdown("<p style='color: #64748b; font-size: 18px;'>Review past hantavirus risk assessments.</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Geçmiş Tablosu
    st.dataframe(
        data=[
            {"ID": "#0042", "Date": "2026-05-25", "Summary": "No environmental indicators detected...", "Risk Level": "Low", "Confidence": "98%"},
            {"ID": "#0041", "Date": "2026-05-22", "Summary": "Rodent droppings observed in corner...", "Risk Level": "High", "Confidence": "85%"},
            {"ID": "#0040", "Date": "2026-05-20", "Summary": "Poor lighting, inconclusive signs...", "Risk Level": "Medium", "Confidence": "72%"}
        ],
        use_container_width=True,
        hide_index=True
    )

elif menu == "📊 Statistics":
    st.title("System Statistics")
    st.markdown("<p style='color: #64748b; font-size: 18px;'>Aggregate metrics and risk distribution from all assessments.</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Metrik Kartları
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Analyses", "145", "+3 bu hafta")
    col2.metric("Avg. Confidence", "92.4%", "+1.2%")
    col3.metric("High Risk Detected", "12", "-2")
    
    st.markdown("---")
    st.markdown("#### Risk Distribution")
    
    # Dağılım simülasyonu
    d1, d2, d3 = st.columns(3)
    with d1:
        st.markdown('<div class="risk-badge risk-high" style="width: 100%; justify-content: center;">High Risk: 12</div>', unsafe_allow_html=True)
    with d2:
        st.markdown('<div class="risk-badge risk-medium" style="width: 100%; justify-content: center;">Medium Risk: 38</div>', unsafe_allow_html=True)
    with d3:
        st.markdown('<div class="risk-badge risk-low" style="width: 100%; justify-content: center;">Low Risk: 95</div>', unsafe_allow_html=True)
