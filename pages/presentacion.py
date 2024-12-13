import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, mean_squared_error, r2_score, confusion_matrix, ConfusionMatrixDisplay
import utilidades as util
from pickle import dump
from pickle import load
import numpy as np
import plotly.express as px

#Congigurar la página principal
st.set_page_config(
    page_title="TRAYECTORIAS EDUCATIVAS PEREIRA - presentación",
    page_icon=":school:",
    initial_sidebar_state="expanded",
    layout="centered"
)

#llamamos el menú
util.generarMenu()

#título
st.title("TRAYECTORIAS EDUCATIVAS INSTITUCIONES OFICIALES ETC PEREIRA GRADOS 6 A 11")

df = pd.read_csv("data/DatosFinales_Trayectoria_Estudiante.csv", index_col=0)

st.markdown("""
    <iframe width="800" height="806" src="https://app.powerbi.com/view?r=eyJrIjoiM2Y1ZmRlMGMtOWUxYS00ZmE3LWE4NjQtZTE3ZTViYjBiODUzIiwidCI6Ijk4YWVmN2VkLWMxYjAtNGY0MS1iODI4LTU0M2RiMWRlMjVmYSIsImMiOjR9" frameborder="0" style="border:0" allowfullscreen></iframe>
    """, unsafe_allow_html=True)

# #selector de gráficos
# st.header('Visualizador de Gráficos')
# tipo = st.selectbox('Seleccione el tipo de gráfico',
#                     ['Barras','Líneas','Dispersión'])
# #selector de las variables a comparar
# variable = st.selectbox('Seleccione la variable a comparar',
#                         df.columns[1:23].values)

# #después de seleccionar
# if tipo == 'Barras':
#     fig = px.bar(df,x='Id_genero',
#                  y=variable, barmode='group',
#     title=f'Estudiante en el {variable}')
# elif tipo == 'Líneas':
#     fig = px.line(df,x='mensaje_1',
#                  y=variable,
#     title=f'Estudiante en el {variable}')
# elif tipo == 'Dispersión':
#     fig = px.scatter(df,x='mensaje_1',
#                  y=variable,
#     title=f'Estudiante en el {variable}')


# st.plotly_chart(fig)

