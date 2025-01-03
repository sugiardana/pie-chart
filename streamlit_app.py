import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Visualisasi Data Menggunakan matplotlib")
st.write(
    "Contoh Penggunaan Visualisasi Data [docs.streamlit.io](https://docs.streamlit.io/)."
)

#df = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/HousingData.csv')
df = pd.read_csv('HousingData.csv')
df = df.dropna()

# Tampilkan histogram plot pada kolom AGE menggunakan library seaborn
sns.histplot(df['AGE'])
plt.show()
st.pyplot(plt.gcf())

#Tampilkan juga histogram plot pada kolom AGE menggunakan library matplotlib, kemudian tambahkan xlabel (Umur) dan ylabel (Jumlah) dengan title (Sebaran Umur Rumah)
plt.hist(df['AGE'])
plt.xlabel('Umur')
plt.ylabel('Jumlah')
plt.title('Sebaran Umur Rumah')
plt.show()
st.pyplot(plt.gcf())

#Tampilkan pie chart pada kolom "CHAS" menggunakan library matplotlib dengan melakukan perhitungan jumlahnya terlebih dahulu
count_chas = df.groupby('CHAS').agg(chas_count=('CHAS', 'count')).reset_index()
plt.pie(count_chas['chas_count'], labels=count_chas['CHAS'], autopct='%1.1f%%')
plt.show()
st.pyplot(plt.gcf())


#st.title("🎈 My new app")
#st.write(
#    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
#)

