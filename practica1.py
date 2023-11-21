import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#st.write("Creación de una tabla")
#df = pd.DataFrame({
#    "primera columna":[1,2,3,4],
#    "segunda columna" : [10,20,30,40]
#    })
#df

#st.write("Creación de una tabla")
#df = pd.DataFrame({[-19.82,99.19]})
#map_data = pd.DataFrame({
#    "latitude" : [19.5032347],
#    "longitude" : [-99.1501528]})
#st.map(map_data)


# Título de la aplicación
st.title("Explorador de Datos Iris con Streamlit")

# Cargar el conjunto de datos Iris
iris = sns.load_dataset('iris')

# Mostrar el conjunto de datos en la barra lateral
st.sidebar.subheader("Datos de Iris")
st.sidebar.write(iris.head())

# Selección del tipo de gráfico
chart_type = st.sidebar.selectbox("Selecciona el tipo de gráfico", ["Histograma", "Diagrama de dispersión"])

# Visualización de datos según la selección
if chart_type == "Histograma":
    # Histograma de características
    # feature = st.sidebar.selectbox("Selecciona la característica", iris.columns)
    # plt.figure(figsize=(8, 6))
    # sns.histplot(iris[feature], kde=True)
    # st.pyplot()
    feature = st.sidebar.selectbox("Selecciona la característica", iris.columns)
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.histplot(iris[feature], kde=True, ax=ax)
    st.pyplot(fig)

else:
    # Diagrama de dispersión entre características
    # feature_x = st.sidebar.selectbox("Selecciona la característica en el eje X", iris.columns)
    # feature_y = st.sidebar.selectbox("Selecciona la característica en el eje Y", iris.columns)
    # plt.figure(figsize=(8, 6))
    # sns.scatterplot(x=feature_x, y=feature_y, data=iris, hue='species')
    # st.pyplot()
    feature_x = st.sidebar.selectbox("Selecciona la característica en el eje X", iris.columns)
    feature_y = st.sidebar.selectbox("Selecciona la característica en el eje Y", iris.columns)

    # Crear una figura y ejes
    fig, ax = plt.subplots(figsize=(8, 6))

    # Diagrama de dispersión
    sns.scatterplot(x=feature_x, y=feature_y, data=iris, hue='species', ax=ax)

    # Mostrar la figura en Streamlit
    st.pyplot(fig)