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
    page_title="SMEC",
    page_icon=":heartpulse:",
    initial_sidebar_state="expanded",
    layout="centered"
)

#llamamos el menú
util.generarMenu()

#título
st.title("TRAYECTORIAS EDUCATIVAS INSTITUCIONES OFICIALES ETC PEREIRA GRADOS 6 A 11")

df = pd.read_csv("data/resultado_comparacion_completa_valores.csv", index_col=0)

#selector de gráficos
st.header('Visualizador de Gráficos')
tipo = st.selectbox('Seleccione el tipo de gráfico',
                    ['Barras','Líneas','Dispersión'])
#selector de las variables a comparar
variable = st.selectbox('Seleccione la variable a comparar',
                        df.columns[1:].values)

#después de seleccionar
if tipo == 'Barras':
    fig = px.bar(df,x='Terminó la trayectoria escolar',
                 y=variable, barmode='group',
    title=f'Estudiante en el grado {variable}')
elif tipo == 'Líneas':
    fig = px.line(df,x='Terminó la trayectoria escolar',
                 y=variable,
    title=f'Estudiante en el grado {variable}')
elif tipo == 'Dispersión':
    fig = px.scatter(df,x='Terminó la trayectoria escolar',
                 y=variable,
    title=f'Estudiante en el grado {variable}')


st.plotly_chart(fig)

