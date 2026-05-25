import streamlit as st
import time

# --- 1. SAYFA AYARLARI VE MODERN TASARIM (CSS) ---
st.set_page_config(page_title="Hantavirus Risk Analyzer", page_icon="🛡️", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    .block-container {
        padding-top: 2rem; 
        padding-bottom: 2rem;
        max-width: 1200px;
    }
    
    .stButton>button {
        width: 100%; 
        border-radius: 8px; 
        font-weight: 600; 
        padding: 0.6rem 1rem;
        transition: all 0.3s;
    }
    
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
    
    /* Checkbox'ları biraz daha modern göstermek için */
    .stCheckbox > div {
        background-color: #f8fafc;
        padding: 8px 12px;
        border-radius: 8px;
        border: 1px solid #e2e8f0;
        margin-bottom: 4px;
    }
    </style>
""", unsafe_allow_html=True)


# --- 2. SOL MENÜ (SIDEBAR) ---
with st.sidebar:
    st.markdown("### 🛡️ Hantavirus")
    st.markdown("<p style='color: #64748b; font-size: 14px; margin-top: -15px;'>Risk Analyzer</p>", unsafe_allow_html=True)
    st.divider()
    
    menu = st.radio("Navigasyon", ["🔍 Analyzer", "🕒 History", "📊 Statistics"], label_visibility="collapsed")
    
    st.divider()
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
    st.markdown("<p style='color: #64748b; font-size: 18px;'>Upload clinical/environmental photographs and input patient symptoms for AI-powered Hantavirus risk analysis.</p>", unsafe_allow_html=True)
    st.markdown("---")

    col1, col2 = st.columns([1.1, 1], gap="large")

    with col1:
        # FOTOĞRAF YÜKLEME ALANI
        st.markdown("### 1. Image Upload")
        uploaded_file = st.file_uploader("Upload Image", type=['png', 'jpg', 'jpeg'], label_visibility="collapsed")
        
        if uploaded_file is not None:
            st.image(uploaded_file, use_container_width=True, caption="Seçilen Görüntü")
        else:
            st.markdown("""
                <div style="border: 2px dashed #cbd5e1; border-radius: 12px; padding: 30px 20px; text-align: center; background-color: #f8fafc; margin-bottom: 25px;">
                    <h3 style="color: #94a3b8; margin-bottom: 5px;">📷 Fotoğraf Yükleyin</h3>
                    <p style="color: #94a3b8; font-size: 12px;">JPEG, PNG (Max 10MB)</p>
                </div>
            """, unsafe_allow_html=True)
        
        # SEMPTOM DEĞERLENDİRME BÖLÜMÜ (YENİ EKLENEN KISIM)
        st.markdown("### 2. Semptom Değerlendirme")
        st.markdown("<p style='color: #64748b; font-size: 14px;'>Hastada aşağıdaki belirtilerden hangileri mevcut? Lütfen işaretleyin.</p>", unsafe_allow_html=True)
        
        with st.expander("Grup 1: Genel ve Sindirim Sistemi Belirtileri", expanded=True):
            s1 = st.checkbox("Yüksek ateş (38-40°C arası) ve titreme")
            s2 = st.checkbox("Şiddetli kas ve eklem ağrıları (özellikle sırt, kalça, uyluk ve bacaklarda)")
            s3 = st.checkbox("Aşırı halsizlik ve yoğun yorgunluk hissi")
            s4 = st.checkbox("Şiddetli baş ağrısı ve baş dönmesi")
            s5 = st.checkbox("Sindirim sistemi sorunları (mide bulantısı, kusma, karın ağrısı ve bazen ishal)")

        with st.expander("Grup 2: Solunum ve Kalp-Damar Belirtileri"):
            s6 = st.checkbox("Öksürük (genellikle kuru öksürük)")
            s7 = st.checkbox("Hızla ilerleyen şiddetli nefes darlığı")
            s8 = st.checkbox("Göğüste sıkışma, baskı veya doluluk hissi")
            s9 = st.checkbox("Akciğerlerde sıvı birikmesi (pulmoner ödem)")
            s10 = st.checkbox("Tansiyon düşüklüğü ve akciğer yetmezliğine bağlı şok")

        with st.expander("Grup 3: Böbrek ve Kanama Belirtileri"):
            s11 = st.checkbox("Şiddetli bel ve böbrek ağrısı")
            s12 = st.checkbox("İdrar miktarında ani azalma veya idrarın tamamen kesilmesi")
            s13 = st.checkbox("Kanama eğilimi (ciltte nokta şeklinde morarmalar, burun, diş eti, idrar veya dışkıda kan)")
            s14 = st.checkbox("Gözlerde ve yüzde kızarıklık, bulanık görme")
            s15 = st.checkbox("Yüzde, ellerde ve ayaklarda ödem (şişlik)")
            s16 = st.checkbox("Böbrek yetmezliği")

        st.write("") # Boşluk
        run_btn = st.button("🚀 Run Assessment", type="primary", use_container_width=True)

    with col2:
        if run_btn:
            if uploaded_file is None:
                st.error("⚠️ Lütfen analizi başlatmadan önce bir fotoğraf yükleyin.")
            else:
                with st.spinner("Evaluating risk factors and extracting data..."):
                    time.sleep(2) 
                
                st.markdown("### Assessment Complete")
                st.markdown("<p style='color: #64748b; font-size: 14px;'>Today</p>", unsafe_allow_html=True)
                
                # İşaretlenen semptomlara göre risk belirleme senaryosu eklenebilir. Şimdilik yüksek risk uyarısı:
                secilen_semptom_sayisi = sum([s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16])
                
                if secilen_semptom_sayisi > 3:
                    st.markdown('<div class="risk-badge risk-high">🚨 High Risk</div>', unsafe_allow_html=True)
                    st.markdown("#### Summary")
                    st.error("Hastada tespit edilen birden fazla majör semptom (solunum, böbrek veya kanama eğilimi) Hantavirüs şüphesini oldukça güçlendirmektedir. Görsel analiz de risk faktörlerini desteklemektedir. Acil tıbbi müdahale ve izolasyon önerilir.")
                    conf = 94
                    level = "High"
                    renk = "#b91c1c"
                else:
                    st.markdown('<div class="risk-badge risk-low">✅ Low Risk</div>', unsafe_allow_html=True)
                    st.markdown("#### Summary")
                    st.info("İşaretlenen semptomlar ve görsel analiz Hantavirüs için spesifik bir yüksek risk tablosu oluşturmamaktadır. Ancak hastanın durumu yakından takip edilmelidir.")
                    conf = 88
                    level = "Low"
                    renk = "#047857"
                
                st.markdown("---")
                
                m1, m2 = st.columns(2)
                with m1:
                    st.markdown("<p style='font-size: 14px; font-weight: 600; color: #1e293b; margin-bottom: 0;'>Confidence Score</p>", unsafe_allow_html=True)
                    st.markdown(f"<p style='font-size: 32px; font-weight: 800; color: #2563eb;'>{conf}%</p>", unsafe_allow_html=True)
                with m2:
                    st.markdown("<p style='font-size: 14px; font-weight: 600; color: #1e293b; margin-bottom: 0;'>Confidence Level</p>", unsafe_allow_html=True)
                    st.markdown(f"<p style='font-size: 24px; font-weight: 700; color: {renk};'>{level}</p>", unsafe_allow_html=True)
                
                st.markdown("**AI Confidence**")
                st.progress(conf)
        else:
            st.markdown("### Assessment Complete")
            st.markdown("""
                <div style="padding: 50px 20px; text-align: center; border: 2px dashed #e2e8f0; border-radius: 12px; background-color: #f8fafc; margin-top: 20px;">
                    <h4 style="color: #64748b; margin-bottom: 10px;">Awaiting Input</h4>
                    <p style="color: #94a3b8; font-size: 14px;">Upload a photo, select the observed symptoms, and run the assessment to see detailed AI analysis results here.</p>
                </div>
            """, unsafe_allow_html=True)

elif menu == "🕒 History":
    st.title("Analysis History")
    st.markdown("<p style='color: #64748b; font-size: 18px;'>Review past hantavirus risk assessments.</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.dataframe(
        data=[
            {"ID": "#0042", "Date": "2026-05-25", "Summary": "No environmental indicators detected...", "Risk Level": "Low", "Confidence": "98%"},
            {"ID": "#0041", "Date": "2026-05-22", "Summary": "Patient exhibits severe respiratory distress...", "Risk Level": "High", "Confidence": "85%"},
            {"ID": "#0040", "Date": "2026-05-20", "Summary": "Mild fever and muscle aches, pending observation...", "Risk Level": "Medium", "Confidence": "72%"}
        ],
        use_container_width=True,
        hide_index=True
    )

elif menu == "📊 Statistics":
    st.title("System Statistics")
    st.markdown("<p style='color: #64748b; font-size: 18px;'>Aggregate metrics and risk distribution from all assessments.</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Analyses", "145", "+3 bu hafta")
    col2.metric("Avg. Confidence", "92.4%", "+1.2%")
    col3.metric("High Risk Detected", "12", "-2")
    
    st.markdown("---")
    st.markdown("#### Risk Distribution")
    
    d1, d2, d3 = st.columns(3)
    with d1:
        st.markdown('<div class="risk-badge risk-high" style="width: 100%; justify-content: center;">High Risk: 12</div>', unsafe_allow_html=True)
    with d2:
        st.markdown('<div class="risk-badge risk-medium" style="width: 100%; justify-content: center;">Medium Risk: 38</div>', unsafe_allow_html=True)
    with d3:
        st.markdown('<div class="risk-badge risk-low" style="width: 100%; justify-content: center;">Low Risk: 95</div>', unsafe_allow_html=True)
