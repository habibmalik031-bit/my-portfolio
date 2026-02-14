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
    st.title("📁 Projects")
    st.write("Berikut adalah beberapa proyek analisis data yang telah saya selesaikan:")
    
    tab1, tab2, tab3 = st.tabs(["E-Commerce Analysis", "HR Attrition Analysis", "Logistics & Delivery Performance Analysis"])
    
    with tab1:
        st.subheader("E-Commerce Analysis")
        st.image("assets/diagram.png", width=500)
        st.write("Analisis Customer Segmentation dataset publik retail online kaggle. Insight utama mencakup tren penjualan bulanan serta mengetahui segmentasi pelanggan.")
        with st.expander("Lihat Detail Proyek"):
            st.write("Proyek ini memberikan segmentasi pelanggan menggunakan metode RFM (Recency, Frequency, Monetary) untuk melakukan segmentasi pelanggan.")
            st.code("print('Hello Data Science!')", language='python')
    with tab2:
        st.subheader("HR Attrition Analysis")
        st.write("Analisis ini bertujuan untuk memahami faktor-faktor yang menyebabkan karyawan meninggalkan perusahaan (attrition).")
        st.warning("")
        try:
            st.image("assets/hr_dashboard.png", caption="Dashboard Analisis Attrisi Karyawan", use_container_width=True)
        except:
            st.error("File 'hr_dashboard.png' tidak ditemukan. Pastikan file ada di folder 'assets/'.")

        st.markdown("#### Key Performance Indicators (KPI)")
        kpi1, kpi2, kpi3, kpi4 = st.columns(4)
        kpi1.metric("Total Employee", "237")
        kpi2.metric("Avg Salary", "4,833")
        kpi3.metric("Avg Age", "34")
        kpi4.metric("Attrition Rate", "16%")

        with st.expander("Lihat Detail & Insight Proyek"):
            st.write("""
            **Deskripsi Proyek:**
            Analisis ini bertujuan untuk memahami faktor-faktor yang menyebabkan karyawan meninggalkan perusahaan (attrition).
            
            **Insight Utama:**
            * **Departemen:** Sektor **Sales** memiliki tingkat atrisi tertinggi (21%), disusul oleh HR (19%).
            * **Pendidikan:** Karyawan dengan latar belakang pendidikan **Human Resources** memiliki atrisi paling tinggi (26%).
            * **Business Travel:** Karyawan yang **sering bepergian** (Travel Frequently) memiliki tingkat atrisi 25%, jauh lebih tinggi dibanding yang jarang travel.
            * **Demografi:** Kelompok usia muda (20-an tahun) menunjukkan tren atrisi yang sangat fluktuatif dan tinggi.
            """)
    with tab3:
        st.subheader("Logistics & Delivery Performance Analysis")
        try:
            st.image("assets/logistics_dashboard.png", caption="Dashboard Performa Pengiriman Logistik", use_container_width=True)
        except:
            st.error("File 'logistics_dashboard.png' tidak ditemukan di folder 'assets/'.")
        st.markdown("#### Delivery Performance Metrics")
        m1, m2, m3, m4, m5 = st.columns(5)
        m1.metric("Total Orders", "1,000")
        m2.metric("Avg Distance", "906 km")
        m3.metric("Avg Deliv Time", "57 min")
        m4.metric("Avg Total Time", "73.71 min")
        m5.metric("Courier Exp", "46")

        with st.expander("Lihat Detail & Insight Proyek Logistik"):
            st.write("""
            **Analisis Performa Pengiriman:**
            * **Weather Impact:** Cuaca 'Clear' menyumbang pesanan tertinggi (500 pesanan/50%), sedangkan cuaca buruk seperti 'Stormy' atau 'Windy' menurunkan volume pesanan secara signifikan.
            * **Traffic Level:** Mayoritas pesanan diproses pada tingkat kemacetan 'Medium' (420) dan 'Low' (383).
            * **Vehicle Type:** Sepeda motor (Bike) adalah armada yang paling banyak digunakan (503 pesanan), diikuti oleh Scooter (302).
            * **Time of Day:** Aktivitas pesanan mencapai puncaknya pada waktu pagi hari (338 pesanan).
            """)


elif page == "Data Analysis":
    st.title("📊 Data & Visualization")
    st.write("Gunakan kontrol di bawah untuk berinteraksi dengan analisis HR dan Logistik.")

    # --- BAGIAN 1: ANALISIS HR (DARI KODE PERTAMA ANDA) ---
    st.header("1. HR Attrition Insights")
    attrition_data = pd.DataFrame({
        'Department': ['HR', 'R&D', 'Sales'],
        'Attrition Rate (%)': [19, 14, 21]
    })

    col1, col2 = st.columns(2)
    with col1:
        st.write("### Ringkasan Data Attrition")
        st.dataframe(attrition_data, use_container_width=True)
    with col2:
        st.write("### Perbandingan Departemen")
        fig_hr = px.bar(attrition_data, x='Department', y='Attrition Rate (%)', color='Department')
        st.plotly_chart(fig_hr, use_container_width=True)

    st.divider() # Garis pembatas

    # --- BAGIAN 2: SIMULASI PRODUK & LOGISTIK (DARI KODE KEDUA ANDA) ---
    st.header("2. Logistics & Product Simulation")
    
    # Simulasi Produk
    st.subheader("Product Sales Simulation")
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['Product A', 'Product B', 'Product C']
    )
    range_val = st.slider("Pilih rentang data produk:", 0, 20, (0, 10))
    selected_data = chart_data.iloc[range_val[0]:range_val[1]]
    st.line_chart(selected_data)

    # Simulasi Logistik
    st.subheader("🚚 Logistics Simulation Tool")
    logistics_data = pd.DataFrame({
        'Weather': ['Clear', 'Rainy', 'Foggy', 'Snowy', 'Windy'],
        'Orders': [500, 204, 103, 97, 96]
    })
    
    selected_weather = st.multiselect(
        "Filter Cuaca (Sesuai Dashboard):", 
        logistics_data['Weather'].unique(), 
        default=['Clear', 'Rainy']
    )
    
    filtered_logistics = logistics_data[logistics_data['Weather'].isin(selected_weather)]
    
    if not filtered_logistics.empty:
        fig_log = px.bar(filtered_logistics, x='Weather', y='Orders', color='Weather', text_auto=True)
        st.plotly_chart(fig_log, use_container_width=True)
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
    