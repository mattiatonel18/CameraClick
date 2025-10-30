import streamlit as st
import math

st.title("Calcolo")
st.write(
    ""
)

# --- Configurazione pagina ---
st.set_page_config(
    page_title="CameraClick",
    page_icon="📊",
    layout="centered"
)


# --- Sidebar (opzionale) ---
# st.sidebar.header("Impostazioni")
# st.sidebar.info("Aggiungi qui i controlli o le opzioni globali.")

# --- Corpo principale ---
st.subheader("Sezione principale")
st.write("Qui potrai inserire i tuoi componenti: input, grafici, tabelle, ecc.")

# --- Footer ---
st.markdown("---")
st.caption("Applicazione realizzata con [Streamlit](https://streamlit.io)")
