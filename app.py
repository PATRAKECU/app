import streamlit as st
import pandas as pd
import lasio
st.title("Aplicación para Registro de Pozos")
st.sidebar.title("Menú")
archivo_las=lasio.read("LGAE-040.las")
df=archivo_las.df()


opciones_inicio=st.sidebar.radio("Seleccione una opción",["Inicio","Datos","Cálculos"])
if opciones_inicio=="Inicio":
	st.write("Sección Inicio")
	barra_deslizadora=st.slider("Seleccione un valor",1,100,30)
	st.write(barra_deslizadora)
	ingreso_numero=st.number_input("Ingrese un valor",min_value=0.00,max_value=1000.00,value=100.00)
	st.write(ingreso_numero)
	seleccion=st.selectbox("Seleccione una opción",["a","b","c"])
if opciones_inicio=="Datos":
	st.write("Sección Datos")
	st.write(df)
if opciones_inicio=="Cálculos":
	st.write("Sección Cálculos")
archivo_las2=st.sidebar.file_uploader("Cargar archivo LAS" , type=['.las', '.LAS'], key=None)

