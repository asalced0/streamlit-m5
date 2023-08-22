# Import streamlit and pandas.
import streamlit as st

# Return a welcome message.
def bienvenida(nombre):
    mymensaje = 'Bienvenido: ' + nombre
    return mymensaje
    
# Read name.
myname = st.text_input('Nombre:')

if(myname):
    # Call function wwith myname parameter.
    mensaje = bienvenida(myname)
    st.write(mensaje)