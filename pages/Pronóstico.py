import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, mean_squared_error, r2_score, confusion_matrix, ConfusionMatrixDisplay
import utilidades as util
from pickle import dump
from pickle import load
import numpy as np


#Configuramos la página
st.set_page_config(
    page_title="SMEC",
    page_icon=":heartpulse:",
    initial_sidebar_state="expanded",
    layout="centered"
)

#llamamos el menú
util.generarMenu()

#Título
st.title('TRAYECTORIAS EDUCATIVAS INSTITUCIONES OFICIALES ETC PEREIRA GRADOS 6 A 11')
#subtítulo
st.header('Datos')
#leo los datos
df = pd.read_csv('data/resultado_comparacion_completa_valores.csv', index_col=0)
st.markdown('**Datos de las trayectorias de los estudiantes')
st.write(df)

#Mostramos el modelo
st.markdown('**Resultado del modelo Random Forest para los datos históricos')
util.modelo_rf(df)


#Generamos los objetos necesarios para ingresar datos
with st.sidebar:
    grado2019 = st.selectbox('Grado Escolar 2019',(999,6,7,8,9,10,11))
    grado2020 = st.selectbox('Grado Escolar 2020',(999,6,7,8,9,10,11))
    grado2021 = st.selectbox('Grado Escolar 2021',(999,6,7,8,9,10,11))
    grado2022 = st.selectbox('Grado Escolar 2022',(999,6,7,8,9,10,11))
    grado2023 = st.selectbox('Grado Escolar 2023',(999,6,7,8,9,10,11))
    grado2024 = st.selectbox('Grado Escolar 2024',(999,6,7,8,9,10,11))
    btn_ejecutar = st.button('Predecir')

# lógica de la predicción
# lista = [6,7,8,999,999,999]
lista = [grado2019,grado2020,grado2021,grado2022,grado2023,grado2024]
# lista2 = [6,7,8,9,10,11]
st.write(lista)

# convertimos los strings en enteros
integer_list = []

for s in lista:
    integer_list.append(int(s))


if btn_ejecutar == True:
    arr = np.array([lista])
    # arr = np.array([lista])
    st.write(arr)
    util.prueba_modelo(arr)
