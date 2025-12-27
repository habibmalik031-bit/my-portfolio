import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# 1. KONFIGURASI HALAMAN
st.set_page_config(
    page_title="Data Portfolio | Malik",
    page_icon="🚀",
    layout="wide"
)

# 2. SIDEBAR NAVIGASI
with st.sidebar:
    st.title("Navigation")
    page = st.radio("Go to:", ["About Me", "Projects", "Data Analysis", "Contact"])
    st.info("Aplikasi ini dibuat menggunakan Streamlit untuk memamerkan skill Data Science.")

# 3. KONTEN HALAMAN: ABOUT ME
if page == "About Me":
    col1, col2 = st.columns([1, 2], gap="large")
    
    with col1:
        # Mengambil gambar dari folder assets yang tadi dibuat
        # Pastikan kamu menaruh file foto asli di assets/profile_pic.png
        st.image("assets/profile_pic.png", caption="Malik - Data Enthusiast", width=250)
    
    with col2:
        st.title("Halo, Saya Malik 👋")
        st.subheader("Data Scientist & Analyst")
        st.write("""
        Selamat datang di portofolio saya. Saya merupakan seorang Enthusias Data yang berfokus pada pengolahan data 
        dan penyajian insight serta rekomendasi yang bermakna bagi bisnis. Dengan latar belakang sebagai student di Dibimbing.id, 
        saya mempelajari penggunaan programming leangue Python, SQL, dan visualisasi data Power BI.
        """)
        
        st.markdown("### Keahlian Utama:")
        col_a, col_b = st.columns(2)
        with col_a:
            st.success("- Python")
            st.success("- Data Visualization Power BI")
        with col_b:
            st.success("- Machine Learning")
            st.success("- SQL & Database Management")
# 4. KONTEN HALAMAN: PROJECTS
elif page == "Projects":
    st.title("📁 Proyek Pilihan")
    st.write("Berikut adalah beberapa proyek analisis data yang telah saya selesaikan:")
    
    tab1, tab2 = st.tabs(["E-Commerce Analysis", ""])
    
    with tab1:
        st.subheader("Proyek Analisis E-Commerce")
        st.image("assets/diagram.png", width=500)
        st.write("Analisis Customer Segmentation dataset publik retail online kaggle. Insight utama mencakup tren penjualan bulanan serta mengetahui segmentasi pelanggan.")
        with st.expander("Lihat Detail Proyek"):
            st.write("Proyek ini memberikan segmentasi pelanggan menggunakan metode RFM (Recency, Frequency, Monetary) untuk melakukan segmentasi pelanggan.")
            st.code("print('Hello Data Science!')", language='python')
    with tab2:
        st.subheader("Prediksi Keuangan")
        st.write("Membangun model regresi untuk memprediksi pendapatan kuartal berikutnya.")
        st.warning("Sedang dalam tahap pengembangan.")

    
# 5. KONTEN HALAMAN: DATA ANALYSIS (Visualisasi Interaktif)
#elif page == "Data Analysis":
    #st.title("📊 Data & Visualization")
    #st.write("Gunakan slider di bawah untuk berinteraksi dengan data simulasi.")

    # Membuat data sampel (Simulasi)
    #chart_data = pd.DataFrame(
        #np.random.randn(20, 3),
        #columns=['Product A', 'Product B', 'Product C']
    #)

    # Widget Interaktif
    #range_val = st.slider("Pilih rentang data:", 0, 20, (0, 10))
    #selected_data = chart_data.iloc[range_val[0]:range_val[1]]

    # Tata Letak Kolom untuk Visualisasi
    #c1, c2 = st.columns(2)
    
    #with c1:
        #st.write("### Tabel Ringkasan")
        #st.dataframe(selected_data, use_container_width=True)
    
    #with c2:
        #st.write("### Grafik Penjualan")
        #fig = px.line(selected_data, title="Tren Produk")
        #st.plotly_chart(fig, use_container_width=True)

# 6. KONTEN HALAMAN: CONTACT
elif page == "Contact":
    st.title("📬 Hubungi Saya")
    
    with st.form("contact_form"):
        name = st.text_input("Nama Anda")
        email = st.text_input("Email")
        message = st.text_area("Pesan")
        submit = st.form_submit_button("Kirim Pesan")
        
        if submit:
            st.success(f"Terima kasih {name}, pesan Anda telah terkirim!")

    st.write("---")
    st.write("🔗 [LinkedIn](https://linkedin.com/in/habibabdulmalik)")
    st.write("💻 [GitHub](https://github.com/habibmalik031-bit)")