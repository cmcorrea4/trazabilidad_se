import streamlit as st
from PIL import Image

st.title(" Sistema de Trazabilidad")

st.header("En este espacio podrás obtener información de tu ciudad.")

image = Image.open('Sistemaiot.png')

option = st.selectbox(
    'Seleccione la orden de trabajo',
    ('Mantenimiento 045666', 'Reparación 078655', 'Baja 092322'))
st.image(image)
genre = st.radio(
    "Seleccione el estado",
    ["En Proceso", "Terminado", "Descartado"],
    captions = ["La pieza está en proceso.", "La pieza esta lista para recolección", "La pieza esta desechada"])

