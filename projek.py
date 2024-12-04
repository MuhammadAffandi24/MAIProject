# Import Required Libraries
import pandas as pd
import numpy as np
import time
import streamlit as st
from PIL import Image
import pickle


st.set_page_config(layout="wide", page_title="VitaPulse❤️‍🩹", page_icon=":stats:")
st.sidebar.title("Navigation")

# Navigasi menggunakan st.radio dengan ikon
menu = st.sidebar.selectbox(
    "Pilih menu",
    [
        "🏠Home", 
        "📊Dataset", 
        "🔍Exploratory Data Analysis", 
        "⚙️Modelling",  
        "📈Prediction", 
        "👤About"
    ]
)

# Load dataset
url = "https://storage.googleapis.com/dqlab-dataset/heart_disease.csv"
df = pd.read_csv(url)

import streamlit as st
import pandas as pd
import pickle
import time

def jantung():
    st.write("""
             Ini adalah aplikasi sederhana untuk memprediksi penyakit jantung.
             Data yang digunakan adalah data dari [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/heart+Disease)
             """)
    st.subheader("Mulai Input Data")
    st.write("**Input Otomatis**")

    uploaded_file = st.file_uploader("Upload File dengan jenis CSV", type=["csv"])
    if uploaded_file is not None:
        input_df = pd.read_csv(uploaded_file)
        # Menampilkan data setelah upload
        st.write("Data yang diupload:", input_df)

        # Membuat tombol prediksi
        if st.button("Predict"):
            df = input_df
            st.write(df)
            with open("model.pkl", "rb") as f:
                modelML = pickle.load(f)      
    #Prediction
            pred = modelML.predict(df)
            pred = modelML.predict(input_df)
            if pred[0] == 0:
                st.success("Pasien tidak memiliki penyakit jantung.")
            else:
                st.error("Pasien memiliki penyakit jantung, segera tangani dengan baik.")
    
    else:
        def user_input_manual():
            st.subheader("Input Manual")
            col1, col2, col3 = st.columns(3)
            with col1:
                cp = st.selectbox("Tipe Nyeri Dada", ["Nyeri Angina", "Nyeri tidak stabil", "Nyeri dada tidak stabil akut", "Nyeri tidak terkait dengan jantung"])
                if cp == "Nyeri Angina":
                    cp = 1
                elif cp == "Nyeri tidak stabil":
                    cp = 2
                elif cp == "Nyeri dada tidak stabil akut":
                    cp = 3
                elif cp == "Nyeri tidak terkait dengan jantung":
                    cp = 4
                thalach = st.slider("Detak Jantung Maksimum", 71, 202, 100)
                slope = st.slider("Kemiringan ST Segment", 0, 2, 1)
            
            with col2:
                exang = st.selectbox("Angina yang diinduksi oleh Olahraga", ("Yes", "No"))
                if exang == 'Yes':
                    exang = 1
                else:
                    exang = 0
                oldpeak = st.slider("ST Depression", 0.0, 6.2, 3.0)
                ca = st.slider("Jumlah Pembuluh Darah Utama", 0, 3, 1)
                
            with col3:
                thal = st.selectbox("Tes Thalium Scan", ["Normal", "Kekurangan Darah", "Kekurangan Darah Parah"])
                if thal == "Normal":
                    thal = 1
                elif thal == "Kekurangan Darah":
                    thal = 2
                elif thal == "Kekurangan Darah Parah":
                    thal = 3
                sex = st.selectbox("Jenis Kelamin", ("Pria", "Wanita"))
                if sex == "Pria":
                    sex = 1
                else:
                    sex = 0
                age = st.slider("Usia", 29, 77, 30)

            data = {'cp': cp,
                    'thalach': thalach,
                    'slope': slope,
                    'exang': exang,
                    'oldpeak': oldpeak,
                    'ca': ca,
                    'thal': thal,
                    'sex': sex,
                    'age': age}
            features = pd.DataFrame(data, index=[0])
            return features
        
        input_df = user_input_manual()
        if st.button("Predict"):
            df = input_df
            st.write(df)
            with open("model.pkl", "rb") as file:
                model = pickle.load(file)      
            prediksi = model.predict(df)
            prediksi = model.predict(input_df)
            if prediksi[0] == 0:
                st.success("Pasien tidak memiliki penyakit jantung.")
            else:
                st.error("Pasien memiliki penyakit jantung, segera tangani dengan baik.")
# Logika navigasi
if menu == "🏠Home":
    st.title("VitaPulse❤️‍🩹: Heart Disease Prediction")
    st.write("""
             **Machine Learning & AI for Heart Disease**
             
             Halo nama saya [Muhammad Muflih Affandi](https://www.linkedin.com/in/muflihaffandi/).
             Saya adalah seorang mahasiswa yang sedang belajar di Universitas Sebelas Maret dengan Jurusan Sains Data. Saya mengikuti
             kelas Machine Learning & AI di DQLab Academy. Dan ini adalah capstone project saya.
             
             """)
    st.markdown("""
    <div style="text-align: center;">
        <img src="https://krakataumedika.com/images/penyakit-jantung.jpg" alt="Gambar Jantung" style="width: 400px;">
        <br> </br>
    </div>
""", unsafe_allow_html=True)
    st.write("""
             **Overview**
             
             Menurut [WHO](https://www.who.int/health-topics/cardiovascular-diseases#tab=tab_1), diperkirakan 17,9 juta orang meninggal setiap tahun karena penyakit CVDs(Kardiovaskular). 
             Penyakit CVDs adalah sekolompok gangguan pada jantung dan pembuluh darah, termasuk jantung koroner, , penyakit serebrovaskular, penyakit jantung rematik, dan kondisi lainnya. 
             Lebih dari empat dari lima kematian akibat CVD disebabkan oleh serangan jantung dan stroke, dengan sepertiga dari kematian tersebut terjadi secara prematur pada orang di bawah usia 70 tahun.
             
             Project ini bertujuan untuk memprediksi apakah seseorang memiliki penyakit jantung atau tidak berdarkan beberapa kriteria yang telah ditentukan.
             Dataset yang digunakan adalah dataset penyakit jantung dari [UCI Machine Learning Repository]("https://archive.ics.uci.edu/ml/datasets/heart+Disease")
             
             Dataset ini berfokus pada diagnosis penyakit jantung menggunakan data klinis seperti usia, jenis kelamin, tekanan darah, 
             kadar kolesterol, hasil pemeriksaan elektrodiagram, detak jantung maksimum, dan data ini diambil setelah pasien berolahraga
             
             
             """)
    
elif menu == "📊Dataset":
    st.title("Dataset")
    st.write("""
             **DATASET OVERVIEW**
             
             Dataset yang digunakan adalah dataset yang menyajikan tentang penyakit jantung dari [UCI Machine Learning Repository]("https://archive.ics.uci.edu/ml/datasets/heart+Disease").
             Dataset ini berasal dari tahun 1988 dan terdiri dari 4 database: Cleveland, Hungaria, Swiss, dan Long Beach V. Dengan kolom 'target' mengacu adanya penyakit jantung pada pasien, direpresentasikan
             dengan angka 1 = ada penyakit jantung, dan 0 = tidak ada penyakit jantung.
            """)
    st.write("""
            **DATASET INFO**
              
            Dataset ini terdiri dari 1025 baris dan 14 kolom. Kolom-kolom tersebut adalah:
            1. `age` : usia dalam tahun (umur)
            2. `sex` : jenis kelamin (1 = laki-laki; 0 = perempuan)
            3. `cp` : tipe nyeri dada
                - 0: typical angina
                - 1: atypical angina
                - 2: non-anginal pain
                - 3: asymptomatic
            4. `trestbps` : tekanan darah istirahat (dalam mm Hg saat masuk ke rumah sakit)
            5. `chol` : serum kolestoral dalam mg/dl
            6. `fbs` : gula darah puasa > 120 mg/dl (1 = true; 0 = false)
            7. `restecg` : hasil elektrokardiografi istirahat
                - 0: normal
                - 1: memiliki ST-T wave abnormalitas (T wave inversions and/or ST elevation or depression of > 0.05 mV)
                - 2: menunjukkan kemungkinan atau pasti hipertrofi ventrikel kiri menurut kriteria Estes
            8. `thalach` : detak jantung maksimum yang dicapai
            9. `exang` : angina yang diinduksi oleh olahraga (1 = yes; 0 = no)
            10. `oldpeak` : ST depression yang disebabkan oleh olahraga relatif terhadap istirahat
            11. `slope` : kemiringan segmen ST latihan puncak
                - 1: naik
                - 2: datar
                - 3: turun
            12. `ca` : jumlah pembuluh darah utama (0-3) yang diwarnai dengan flourosopy
            13. `thal` : 3 = normal; 6 = cacat tetap; 7 = cacat yang dapat dibalik
            14. `target` : memiliki penyakit jantung atau tidak (1 = yes; 0 = no)
             """)
    st.write("""
             **DATA PREVIEW**
             """)
    st.dataframe(df.head())
    
    st.write(f"""
             DATA SHAPE:  
             {df.shape} 
             """)
    
    st.write("""
             **DATA DESCRIPTION**
             """)
    st.write(df.describe())
    
    # Visualisasi Data
    st.write("""
             **DATA VISUALIZATION**
             """)
    views = st.selectbox("Pilih Visualisasi", ["", "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal", "target"])
    if views == "age":
        st.write("Distribusi Usia")
        st.bar_chart(df["age"].value_counts())
        st.write("""Dari distribusi usia ini dapat dilihat bahwa pasien termuda adalah 29 tahun dan pasien tertua adalah 77 tahun dengan rerata pasien berada di umur 54 tahun. 
                 Dimana pasien dengan usia 58 tahun merupakan pasien terbanyak.""")
    elif views == "sex":
        st.write("Distribusi Jenis Kelamin")
        st.bar_chart(df["sex"].value_counts())
        st.write("""
                 Mayoritas pasien adalah laki-laki yang dinyatakan dengan nilai 1 dengan jumlah 713 pasien 
                 dan perempuan dengan jumlah 312 pasien dinyatakan dengan nilai 0.
                 """)
    elif views == "cp":
        st.write("Distribusi Nyeri Dada")
        st.bar_chart(df["cp"].value_counts())
        st.write("""
                 Dari distribusi nyeri dada ini dapat dilihat bahwa pasien dengan nyeri dada tipe 0 (typical angina) merupakan pasien terbanyak dengan jumlah 497 pasien.
                 """)
    elif views == "trestbps":
        st.write("Distribusi Tekanan Darah")
        st.bar_chart(df["trestbps"].value_counts())  
        st.write("""
                 Tekanan darah pasien berada di rentang 94-200 mm Hg dengan rerata tekanan darah pasien adalah 131 mm Hg. 
                 Dan pasien dengan tekanan darah 120 mm Hg merupakan pasien terbanyak dengan 128 pasien.
                 """) 
    elif views == "chol":
        st.write("Distribusi Serum Kolestoral")
        st.bar_chart(df["chol"].value_counts())
        st.write("""
                 Data kolestoral serum pasien berada di rentang 126-564 mg/dl dengan rerata kolestoral serum pasien adalah 246 mg/dl.
                 """)
    elif views == "fbs":
        st.write("Distribusi Gula Darah")
        st.bar_chart(df["fbs"].value_counts()) 
        st.write("""
                 Gula darah puasa pasien dinyatakan dengan nilai 1 jika gula darah puasa pasien > 120 mg/dl dan nilai 0 jika gula darah puasa pasien <= 120 mg/dl.
                 Dan dari grafik ini dapat dilihat bahwa mayoritas pasien memiliki gula darah puasa <= 120 mg/dl.
                 """)
    elif views == "restecg":
        st.write("Distribusi Elektrokardiografi saat Istirahat")
        st.bar_chart(df["restecg"].value_counts())
        st.write("""
                 Elektrokardiografi saat istirahat pasien dinyatakan dengan nilai 0 jika hasil elektrokardiografi pasien normal, 
                 nilai 1 jika hasil elektrokardiografi pasien memiliki ST-T wave abnormalitas, dan nilai 2 jika hasil elektrokaridografi pasien menunjukkan kemungkinan atau pasti hipertensi ventrikel kiri menurut kriteria Estes.
                 Dar grafik ini dapat dilihat bahwa pasien dengan hasil elektrokardiografi normal merupakan pasien *terbanyak*.
                 """)
    elif views == "thalach":
        st.write("Distribusi Detak Jantu Max")
        st.bar_chart(df["thalach"].value_counts())
        st.write("""
                 Detak jantung maksimum yang dicapai pasien berada di rentang 71-202 bpm dengan rerata detak jantung maksimum pasien adalah 149 bpm.
                 Pasien dengan detak jantung maksimum 162 bpm merupakan pasien terbanyak.
                 dengan rerata detak jantung maksimum pasien adalah 149 bpm.
                 """)
    elif views == "exang":
        st.write("Distribusi Angina yang diinduksi oleh Olahraga")
        st.bar_chart(df["exang"].value_counts())
        st.write("""
                 Angina yang diinduksi oleh olahraga pasien dinyatakan dengan nilai 1 jika pasien memiliki angina yang diinduksi oleh olahraga
                 dan nilai 0 jika pasien tidak memiliki angina yang diinduksi oleh olahraga. Data ini menunjukkan bahwa mayoritas pasien tidak memiliki angina yang diinduksi oleh olahraga.
                 """)
    elif views == "oldpeak":
        st.write("Distribusi ST Depression")
        st.bar_chart(df["oldpeak"].value_counts())
        st.write("""
                ST depression yang disebabkan oleh olahraga relatif terhadap istirahat pasien berada di rentang 0-6.2 dengan rerata ST depression pasien adalah 1.1.
                Pasien dengan ST depression 0 merupakan pasien terbanyak. 
                """)
    elif views == "slope":
        st.write("Distribusi Kemiringan Segmen ST")
        st.bar_chart(df["slope"].value_counts())
        st.write("""
                 Kemiringan segmen ST latihan puncak pasien dinyatakan dengan nilai 1 jika segmen ST naik, nilai 2 jika segmen ST datar, dan nilai 3 jika segmen ST turun.
                 Pasien dengan kemiringan segmen ST naik merupakan pasien terbanyak. 
                 """)
    elif views == "ca":
        st.write("Distribusi Jumlah Pembuluh Darah Utama")
        st.bar_chart(df["ca"].value_counts())
        st.write("""
                 Jumlah pembuluh darah utama dibagi menjadi 0-3 yang diwarnai dengan flourosopy. Namun data ini memiliki nilai 4 yang tidak sesuai dengan kriteria.
                 Pasien dengan jumlah pembuluh darah utama 0 merupakan pasien terbanyak.
                """)
    elif views == "thal":
        st.write("Distribusi Tes Thalium Scan")
        st.bar_chart(df["thal"].value_counts())
        st.write("""
                 Tes Thalium Scan dibagi menjadi 3 kategori yaitu 1 = normal, 2 = cacat tetap, dan 3 = cacat yang dapat dibalik. Dan ada nilai 0 yang tidak sesuai dengan kriteria.
                 Pasien dengan tes thalium scan cacat tetap merupakan pasien terbanyak.
                 """)
    elif views == "target":
        st.write("Distribusi Target")
        st.bar_chart(df["target"].value_counts())
        st.write("""
                 Target dari dataset ini adalah memiliki penyakit jantung atau tidak. Pasien yang memiliki penyakit jantung dinyatakan dengan nilai 1 dan pasien yang tidak memiliki penyakit jantung dinyatakan dengan nilai 0.
                 Dari grafik ini dapat dilihat bahwa pasien yang memiliki penyakit jantung lebih banyak dibandingkan dengan pasien yang tidak memiliki penyakit jantung. 
                 Namun perbandingan pasien yang memiliki penyakit jantung dan tidak memiliki penyakit jantung tidak terlalu signifikan.
                 """)
        
        
            
elif menu == "🔍Exploratory Data Analysis":
    st.title("Exploratory Data Analysis")
    st.subheader("**DATA CLEANING**")
    st.write("""
             **Kesalahan penulisan 2 features**
             
             Pada features 'ca' dan 'thal' terdapat kesalahan penulisan, dimana nilai 4 pada 'ca' dan nilai 0 pada 'thal' tidak sesuai dengan kriteria.
             """)
    lihat = st.radio("Show Data", ("", "CA", "Thal"))
    if lihat == "CA":
        st.write('''
        **Feature CA**
        
        Feature CA memiliki 5 nilai dari rentang 0-4, oleh karena itu nilai 4 diubah menjadi NaN (karena seharusnya tidak ada)
        ''')
        st.dataframe(df.ca.value_counts().to_frame().transpose())
        st.write('''
        **Show Data After Cleaning**
        ''')
        st.dataframe(df.ca.replace(4, np.nan).value_counts().to_frame().transpose())
    elif lihat == "Thal":
        st.write('''
        **Feature Thal**
        
        Feature Thal memiliki 4 nilai dari rentang 0-3, oleh karena itu nilai 0 diubah menjadi NaN (karena seharusnya tidak ada)
        ''')
        st.dataframe(df.thal.value_counts().to_frame().transpose())
        st.write('''
        **Show Data After Cleaning**
        ''')
        st.dataframe(df.thal.replace(0, np.nan).value_counts().to_frame().transpose())
    st.write("""
             Karena mengubah suatu nilai menjadi NaN, maka kita perlu mengisi nilai NaN tersebut dengan nilai yang sesuai. Yaitu dengan nilai modus.
             Karena thal dan ca adalah data kategorikal maka modus lebih baik digunakan untuk mengisi nilai NaN. Karena modus tidak terpengaruh oleh outlier.""")
    
    
    st.subheader("**DATA DUPLICATES**")
    st.write("""
         **Mendeteksi Duplikasi Data**

         Duplikasi data adalah data yang sama persis pada semua kolomnya. Duplikasi data dapat mempengaruhi analisis data dan model machine learning.
         """)
    # Display the number of duplicates in the dataset
    st.dataframe(df.duplicated().value_counts().to_frame().transpose())

    # Removing duplicates
    df_cleaned = df.drop_duplicates()

    st.write("""
         Pada dataset ini terdapat data duplikat. Data duplikat ini bisa menyebabkan bias pada model machine learning. 
         Oleh karena itu, data duplikat perlu dihapus.
         """)
    
    st.subheader("**DATA OUTLIERS**")
    st.write("""
            Outliers adalah data yang berbeda dengan data lainnya. Outliers dapat mempengaruhi analisis data dan model machine learning.
            """)

    # Membuat pilihan untuk memilih fitur
    outliers = st.radio("Show Data", ("Age", "Trestbps", "Chol", "Thalach", "Oldpeak"))

    # Logika untuk mendeteksi dan menampilkan outliers
    if outliers == "Age":
        st.write('**Outliers pada Feature Age**')
        # Menghitung IQR untuk mendeteksi outliers
        Q1 = df_cleaned['age'].quantile(0.25)
        Q3 = df_cleaned['age'].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        outliers_age = df_cleaned[(df_cleaned['age'] < lower_bound) | (df_cleaned['age'] > upper_bound)]

        # Menampilkan boxplot
        st.image('age.png', width=400)
    
        st.write(f"Terdapat {len(outliers_age)} outliers pada feature 'Age'.")
        st.write(outliers_age)

    elif outliers == "Trestbps": 
        st.write('**Outliers pada Feature Trestbps (Blood Pressure)**')
        Q1_trestbps = df_cleaned['trestbps'].quantile(0.25)
        Q3_trestbps = df_cleaned['trestbps'].quantile(0.75)
        IQR_tresbps = Q3_trestbps - Q1_trestbps
        lower_bound_trestbps = Q1_trestbps - 1.5 * IQR_tresbps
        upper_bound_tresbps = Q3_trestbps + 1.5 * IQR_tresbps

        outliers_trestbps = df_cleaned[(df_cleaned['trestbps'] < lower_bound_trestbps) | (df_cleaned['trestbps'] > upper_bound_tresbps)]

        # Menampilkan boxplot
        st.image('trestbps.png', width=400)

        st.write(f"Terdapat {len(outliers_trestbps)} outliers pada feature 'Trestbps'.")
        st.write(outliers_trestbps)

    elif outliers == "Chol": 
        st.write('**Outliers pada Feature Serum Colestoral**')
        Q1_chol = df_cleaned['chol'].quantile(0.25)
        Q3_chol = df_cleaned['chol'].quantile(0.75)
        IQR_chol = Q3_chol - Q1_chol
        lower_bound_chol = Q1_chol - 1.5 * IQR_chol
        upper_boundchol = Q3_chol + 1.5 * IQR_chol

        outliers_chol = df_cleaned[(df_cleaned['chol'] < lower_bound_chol) | (df_cleaned['chol'] > upper_boundchol)]

        # Menampilkan boxplot
        st.image('chol.png', width=400)

        st.write(f"Terdapat {len(outliers_chol)} outliers pada feature 'chol'.")
        st.write(outliers_chol)

    elif outliers == "Thalach": 
        st.write('**Outliers pada Feature detak jantung maksimum**')
        Q1_thalach = df_cleaned['thalach'].quantile(0.25)
        Q3_thalach = df_cleaned['thalach'].quantile(0.75)
        IQR_thalach = Q3_thalach - Q1_thalach
        lower_bound_thalach = Q1_thalach - 1.5 * IQR_thalach
        upper_boundthalach = Q3_thalach + 1.5 * IQR_thalach

        outliers_thalach = df_cleaned[(df_cleaned['thalach'] < lower_bound_thalach) | (df_cleaned['thalach'] > upper_boundthalach)]
        # Menampilkan boxplot
        st.image('thalach.png', width=400)

        st.write(f"Terdapat {len(outliers_thalach)} outliers pada feature 'thalach'.")
        st.write(outliers_thalach)

    elif outliers == "Oldpeak":
        st.write('**Outliers pada Feature ST depression**')
        Q1_oldpeak = df_cleaned['oldpeak'].quantile(0.25)
        Q3_oldpeak = df_cleaned['oldpeak'].quantile(0.75)
        IQR_oldpeak = Q3_oldpeak - Q1_oldpeak
        lower_bound_oldpeak = Q1_oldpeak - 1.5 * IQR_oldpeak
        upper_boundoldpeak = Q3_oldpeak + 1.5 * IQR_oldpeak

        outliers_oldpeak = df_cleaned[(df_cleaned['oldpeak'] < lower_bound_oldpeak) | (df_cleaned['oldpeak'] > upper_boundoldpeak)]

        # Menampilkan boxplot
        st.image('oldpeak.png', width=400)

        st.write(f"Terdapat {len(outliers_oldpeak)} outliers pada feature 'oldpeak'.")
        st.write(outliers_oldpeak)

    st.write("""
             Outliers dapat mempengaruhi analisis data dan model machine learning. Oleh karena itu, outliers perlu dihapus.
             """)
    
    st.subheader("**KORELASI FITUR**")
    st.write("""
             Korelasi adalah hubungan antara dua variabel. Korelasi dapat membantu kita memahami hubungan antara fitur-fitur dalam dataset.
             """)
    st.dataframe(df_cleaned.corr())
    st.write("""
             Korelasi antara fitur-fitur dalam dataset ini tidak terlalu tinggi. Korelasi tertinggi adalah antara 'thalach' dan 'target' dengan nilai 0.42.
             """)
    
    st.subheader("**SELEKSI FITUR**")
    st.write("""
             Selekasi fitur adalah proses memilih fitur yang paling penting dalam dataset. Selekasi fitur dapat membantu meningkatkan kinerja model machine learning.
             """)
    st.dataframe(df_cleaned.corr()['target'].sort_values(ascending=False))
    st.write("""
             Dari tabel korelasi di atas, kita dapat melihat bahwa fitur 'ca', 'oldpeak', 'thal', 'exang', 'cp', 'thalach', 'slope', 'age', dan 'chol' memiliki korelasi tertinggi dengan target.
             """)
    
    st.write("**Scree Plot**")
    st.image("plotelbow.png")
    st.write("""
             Dapat dilihat bahwa setelah di titik ke-9, grafik mulai melandai. Oleh karena itu, kita memilih 9 fitur terbaik.
             """)
    st.write("""
             Dari plot di atas, kita dapat melihat bahwa jumlah fitur yang paling baik adalah 9 fitur yaitu:
             1. ca
             2. oldpeak
             3. thal
             4. exang
             5. cp
             6. thalach
             7. slope
             8. age
             9. chol
             """)
    
    st.subheader("**DATA NORMALIZATION**")
    st.write("""
             Normalisasi adalah proses mengubah nilai-nilai fitur ke skala yang sama. Normalisasi dapat membantu meningkatkan kinerja model machine learning. Dan bermanfaat
             untuk fitur-fitur yang memiliki skala yang berbeda.
             Data dinormalisasi menggunakan library **StandardScaler** yang ada di python.
             """)
    
    st.subheader("**DATA SPLITTING**")
    st.write("""
             Data splitting adalah proses membagi data menjadi data training dan data testing. Data training digunakan untuk melatih model machine learning dan data testing digunakan untuk menguji model machine learning.
             Data dibagi menjadi data training sebesar 80% dan data testing sebesar 20% menggunakan library **train_test_split** yang ada di python.
             """)
    
elif menu == "⚙️Modelling":
    st.title("Modelling")
    model = st.selectbox("Pilih Model", ["Before Tuning", "After Tuning", "ROC-AUC", "Kesimpulan"])
    if model == "Before Tuning":
        st.subheader("Before Tuning")
        st.write("""
             Sebelum melakukan tuning, kami melakukan pemodelan menggunakan 4 algoritma yaitu:
                1. Logistic Regression
                2. Decision Tree
                3. Random Forest
                4. Gradient Boosting
            dengan hasil sebagai berikut:
             """)
    # Data dictionary
        accuracy_score = {
            'Logistic Regression': [0.82,0.81, 0.81, 0.81, 0.84, 0.84, 0.84],
            'Decision Tree': [0.70, 0.66, 0.73, 0.69, 0.75, 0.68, 0.71],
            'Random Forest': [0.82, 0.83, 0.77, 0.80, 0.82, 0.87, 0.84],
            'MLP Classifier': [0.84, 0.90, 0.73, 0.81, 0.81, 0.94, 0.87]
        }

            # Buat DataFrame langsung dari dictionary
        akurasi = pd.DataFrame.from_dict(
        accuracy_score, 
            orient='index', 
            columns=[
                'Accuracy Score',
                'Precision Score No Disease',
                'Recall Score No Disease',
                'F1 Score No Disease',
                'Precision Score Disease',
                'Recall Score Disease',
                'F1 Score Disease'
                ]
        )

        # Tambahkan kolom nama model
        akurasi.insert(0, 'Model', akurasi.index)

        # Reset index
        akurasi.reset_index(drop=True, inplace=True)

        # Tampilkan di Streamlit
        st.write(akurasi)
        st.write("""
             Dari hasil di atas, Random Forest memiliki akurasi yang paling tinggi yaitu *0.87.* 
             Oleh karena itu, **Random Forest** dipilih sebagai **model terbaik sebelum tuning**. Namun recall nya masih sedikit rendah yaitu di angka *0.77*.
             Sehingga dapat menyebabkan false negative yang sedikit tinggi, maka diperlukan tunning agar prediksi menjadi lebih baik.
             """)
        st.subheader("Evaluasi Matrix")
        st.write("""
            1. Precision tinggi: Model memastikan bahwa semua pasien yang diprediksi memiliki penyakit benar-benar positif (minimalkan kesalahan positif palsu). Penting dalam situasi di mana salah prediksi akan menyebabkan pengobatan yang tidak perlu.
            2. Recall tinggi: Model memastikan semua pasien yang memiliki penyakit terdeteksi (minimalkan kesalahan negatif palsu). Penting dalam situasi di mana kegagalan mendeteksi kasus dapat berakibat fatal.
            3. F1 Score: Digunakan untuk keseimbangan antara Precision dan Recall, terutama ketika tidak jelas apakah kita lebih peduli dengan positif palsu atau negatif palsu.
             """)
        
        
    elif model == "After Tuning":
        st.subheader("After Tuning")
        st.write("""
                Saat Tuning, kami menggunakan hyperparameter tuning dengan GridSearchCV untuk meningkatkan kinerja model machine learning.
                Menurut [DQLab]("https://dqlab.id/konsep-hyperparameter-tuning-pada-machine-learning") Hyperparameter tuning adalah proses mencari nilai optimal untuk hyperparameter suatu model dalam machine learning atau deep learning.
                Hyperparameter ini dapat membantu meningkatkan kinerja model machine learning dengan menghindarkan model dari overfitting atau underfitting.
                Tuning ini dapat menyesuaikan model machine learning dengan data yang digunakan. 
                 """)
        st.write("""
                 Berikut adalah hasil setelah dilakukan tuning menggunakan hyperparameter tuning.
                 """)
        accuracy_hyper = {
            'Logistic Regression': [0.92 ,0.81, 0.81, 0.81, 0.84, 0.84, 0.84],
            'Decision Tree': [0.88, 0.83, 0.73, 0.78, 0.79, 0.87, 0.83],
            'Random Forest': [0.91, 0.80, 0.77, 0.78, 0.81, 0.84, 0.83],
            'MLP Classifier': [0.92, 0.79, 0.88, 0.84, 0.89, 0.81, 0.85]
        }
        akurasi_hyper = pd.DataFrame.from_dict(
            accuracy_hyper, 
            orient='index', 
            columns=[
                'Accuracy Score',
                'Precision Score No Disease',
                'Recall Score No Disease',
                'F1 Score No Disease',
                'Precision Score Disease',
                'Recall Score Disease',
                'F1 Score Disease'
            ]
        )
        akurasi_hyper.insert(0, 'Model', akurasi_hyper.index)
        akurasi_hyper.reset_index(drop=True, inplace=True)
        st.write(akurasi_hyper)
        st.write("""
            Setelah dilakukan tuning, model Logistic Regression dan MLP memiliki akurasi yang sama. Namun dapat dilihat untuk precisionnya lebih tinggi pada model Logistic Regression.
            Sehingga model Logistic Regression dipilih sebagai model terbaik setelah tuning.
            """)
        st.subheader("Evaluasi Matrix")
        st.write("""
            1. Precision tinggi: Model memastikan bahwa semua pasien yang diprediksi memiliki penyakit benar-benar positif (minimalkan kesalahan positif palsu). Penting dalam situasi di mana salah prediksi akan menyebabkan pengobatan yang tidak perlu.
            2. Recall tinggi: Model memastikan semua pasien yang memiliki penyakit terdeteksi (minimalkan kesalahan negatif palsu). Penting dalam situasi di mana kegagalan mendeteksi kasus dapat berakibat fatal.
            3. F1 Score: Digunakan untuk keseimbangan antara Precision dan Recall, terutama ketika tidak jelas apakah kita lebih peduli dengan positif palsu atau negatif palsu.
             """)
        
    elif model == 'ROC-AUC':
        st.subheader("ROC-AUC")
        st.write("""
            ROC-AUC adalah metrik evaluasi yang digunakan untuk mengukur kinerja model machine learning. ROC-AUC adalah singkatan dari Receiver Operating Characteristic - Area Under Curve.
            ROC-AUC mengukur kemampuan model untuk membedakan antara kelas positif dan kelas negatif. ROC-AUC adalah metrik evaluasi yang baik untuk mengukur kinerja model machine learning.
            """)
        st.write("""
            Berikut adalah hasil ROC-AUC dari model Random Forest dan MLP Classifier setelah dilakukan tuning.
            """)
        roc_auc = {
            'Model': ['Logistic Regression', 'Random Forest', 'Decision Tree', 'MLP'],
            'ROC-AUC': [0.87, 0.89, 0.84, 0.90]
        }
        roc_auc_df = pd.DataFrame(roc_auc)
        st.write(roc_auc_df)
        st.write("""
            Dari hasil di atas, model MLP memiliki ROC-AUC tertinggi yaitu 0.90. 
            ROC-AUC ini menunjukkan bahwa model MLP memiliki kemampuan yang baik untuk membedakan antara kelas positif dan kelas negatif.
            """)
        st.write("**ROC-AUC Curves**")
        st.image("ROC-AUC.png")
        st.write("""
                 ROC adalah kurva probabilitas dan AUC mewakili tingkat pemisahan. Ini menunjukan seberapa
                 baik model dalam membedakan kelas. Semakin tinggi AUC, semakin baik modelnya dalam memprediksi kelas 0 sebagai 0 dan kelas 1 sebagai 1.
                 Model yang sangat baik memiliki AUC mendekati 1, yang berarti memiliki ukuran pemisahan yang baik. Model yang buruk memiliki AUC mendekati 0, yang berarti memiliki ukuran pemisahan yang terburuk.
                 """)
        st.subheader("Threshold")
        st.write("""
            **Threshold** adalah nilai yang digunakan untuk membedakan antara kelas positif dan kelas negatif. 
            Nilai threshold default adalah 0.5. Namun, kita dapat mengubah nilai threshold sesuai dengan kebutuhan.
            Pada kali ini kita mencari threshold terbaik untuk tiap model dan dipatkan sebagai berikut:
            """)
        threshold = {
            'Model': ['Logistic Regression', 'Random Forest', 'Decision Tree', 'MLP'],
            'ROC-AUC': [0.47, 0.57, 0.61, 0.47]
        }
        threshold_df = pd.DataFrame(threshold)
        st.write(threshold_df)
        st.write("""
                 Pada classification report didapat random forest memiliki nilai tertinggi, namun pada ROC-AUC random forest kalah tipis dengan
                 MLP. Sehingga kita tetap memilih random forest sebagai model yang digunakan. Namun model dengan mempertimbangkan thresholdnya dimana MLP dan Random Forest memiliki jarak yang jauh maka bisa diambil MLP
                 karena semakin kecil threshold akan menurunkan FPR (Kasus negatif yang salah prediksi positif)""") 
        
    elif model == "Kesimpulan":
        st.subheader("Kesimpulan")
        st.write("""
                 Meskipun Random Forest tetap menjadi model yang sangat baik, hasil ROC-AUC dan threshold menunjukkan bahwa MLP dapat lebih optimal dalam beberapa kondisi, terutama dengan pertimbangan FPR. Oleh karena itu, MLP bisa dipertimbangkan sebagai alternatif terbaik untuk aplikasi yang lebih sensitif terhadap kesalahan prediksi negatif.
                 Data yang digunakan adalah data dari [UCI Machine Learning Repository]("https://archive.ics.uci.edu/ml/datasets/heart+Disease")
                 """)
        st.image("ROC-AUC.png")
        st.write("""
                 Bisa dilihat dari grafik ROC-AUC diatas, bahwa MLP Classifier memiliki nilai tertinggi yaitu 0.90. dan untuk thresholdnya berada di paling rendah sehingga dapat lebih optimal di berbagai kondisi.
                 """)
    
elif menu == "📈Prediction":
    st.title("Prediction")
    jantung()
elif menu == "👤About":
    st.title("About Me")
    st.image("Me.jpg", width=200)
    st.write("""
             **Muhammad Muflih Affandi**
             
             Saya adalah seorang mahasiswa aktif di Universitas Sebelas Maret Surakarta dengan Program Studi Sains Data Fakultas Teknologi Informasi dan Sains Data.
             Ketertarikan saya dalam dunia data mengantarkan saya untuk belajar di DQLab Academy pada kelas Machine Learning & AI.
             Ini merupakan capstone project saya yang mengimplementasikan pengetahuan yang saya dapatkan dari kelas Machine Learning & AI di DQLab Academy.
             """)
    
    st.write("""
             Proyek ini bertujuan untuk **memprediksi penyakit jantung** berdasarkan beberapa kriteria yang telah ditentukan, dan membantu tenaga medis serta pasien dalam mendeteksi penyakit jantung sehingga
             dapat dilakukan penanganan lebih dini dan mengurangi resiko kematian.
             """)
    
    st.write("""
             **Contact Me**     
            - [Linkedin]("https://www.linkedin.com/in/muhammad-muflih-affandi-707028287/")
            - [Github]("https://github.com/MuhammadAffandi24")
            - [Instagram]("https://www.instagram.com/affanmuhamd/?hl=en")    
             """)
