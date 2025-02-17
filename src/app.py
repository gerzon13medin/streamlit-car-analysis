import streamlit as st
import pandas as pd
import requests

from utils.data_processing import clean_data
from utils.visualization import plot_price_distribution, plot_fuel_type_count


# Cargar datos

url = 'https://raw.githubusercontent.com/anfagudelogo-tpt/datasets/refs/heads/main/car_price_dataset.csv'

response = requests.get(url, verify=False)  # Desactiva la verificación SSL temporalmente
open('car_price_dataset.csv', 'wb').write(response.content)

df = pd.read_csv('car_price_dataset.csv')


df = clean_data(df)


# Titulo y dscripcion de la app
st.title("Análisis Descriptivo de Vehículos")
st.write("Esta aplicación permite explorar un dataset de vehículos, proporcionando estadísticas y visualizaciones interáctivas")


# Mostrar el resumen estadístico
tabla_resumen = df.describe()
st.write("### Resumen estadístico de los datos")
st.dataframe(tabla_resumen)


# Generar y mostrar gráficos
fig1 = plot_price_distribution(df)
st.pyplot(fig1)


fig2 = plot_fuel_type_count(df)
st.pyplot(fig2)


# Input para seleccionar una marca de vehiculo
selected_brand = st.text_input("Ingrese una marca de vehiculos para filtrar datos:")

if st.button("Generar analisis"):
    df_filtered = df[df["brand"] == selected_brand]


    if df_filtered.empty:
        st.write("Ingrese un valor adecuado")
    else:
        st.write(f"### Datos filtrados para la marca: {selected_brand}")
        st.dataframe(df_filtered.describe())
        fig_filtered = plot_price_distribution(df_filtered)
        st.pyplot(fig_filtered)