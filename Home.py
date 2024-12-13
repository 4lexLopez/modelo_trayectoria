import pandas as pd
import streamlit as st
import utilidades as util



#Congigurar la página principal
st.set_page_config(
    page_title="TRAYECTORIAS EDUCATIVAS PEREIRA",
    page_icon="📊",
    initial_sidebar_state="expanded",
    layout="centered"
)
#llamamos el menú
util.generarMenu()

st.title("TRAYECTORIAS EDUCATIVAS INSTITUCIONES OFICIALES ETC PEREIRA GRADOS 6 A 11")

st.write("""
El presente informe tiene como objetivo proporcionar un análisis exhaustivo de las trayectorias escolares de los estudiantes de las instituciones educativas de Pereira, identificando patrones y desafíos clave que afectan la continuidad y calidad del proceso educativo.
A través del estudio de indicadores críticos como la tasa de permanencia escolar, la distribución socioeconómica, la representación por género y las necesidades especiales, se busca comprender las barreras y oportunidades existentes en el sistema educativo.om Forest).

Los datos del desarrollo del proyecto se encuentran en la carpeta en linea:\n\n https://drive.google.com/drive/folders/1k3iyfL6nrD63zOpN1jH6d3R2ARqXgo4h?usp=sharing
"""
         )

#Ponemos una imagen a nuestra página
from PIL import Image
#abrimos la imagen
imagen = Image.open("media/pereira.jpg")
#incrustamos la imagen
st.image(imagen, caption="Pereira",
         use_container_width=False,width=500)



st.header("1.1	Objetivo general")
st.write("""
	
Realizar un análisis detallado de las trayectorias escolares de los estudiantes de las instituciones educativas de Pereira, con el fin de identificar patrones y desafíos que afecten la continuidad y calidad del proceso educativo, y ofrecer recomendaciones informadas para mejorar el rendimiento, retención, y éxito escolar.
""")
st.header("1.2	Objetivos específicos.")
st.markdown("""
         
●	Realizar el análisis completo de las trayectorias escolares en todas las instituciones educativas oficiales de Pereira de los grados 6 a 11.
         """)
st.markdown("""
●	Identificar al menos cinco patrones comunes y tres desafíos principales en las trayectorias escolares.
         """)
st.markdown("""
●	Elaborar un conjunto de recomendaciones específicas para mejorar la retención y rendimiento escolar.

""")

hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style> 
        """

st.markdown(hide_streamlit_style, unsafe_allow_html=True)