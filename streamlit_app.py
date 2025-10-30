# pip freeze > requirements.txt
import streamlit as st
import numpy as np

# st.title("Calcolo")

# --- Configurazione pagina ---
st.set_page_config(
    page_title="CameraClick",
    # page_icon="📊",
    layout="centered"
)


# --- Sidebar (opzionale) ---
# st.sidebar.header("Impostazioni")
# st.sidebar.info("Aggiungi qui i controlli o le opzioni globali.")

# --- Corpo principale ---
st.subheader("Caratteristiche macchina e obiettivo")

sensorType = st.radio("Scegliere il tipo di sensore",
                          ["FullFrame", "APS-C"],
                          index=1)
sensorSize = [22.3, 14.9]
sensorSize.append(np.sqrt(sensorSize[0]**2 + sensorSize[1]**2))

imgSize = [6000, 4000]
imgSize.append(np.sqrt(imgSize[0]**2 + imgSize[1]**2))
# st.write(imgSize[2])

lFOC = st.number_input("Lunghezza focale (mm)", value=50, min_value=1, step=5)
lFOCeff = lFOC
if sensorType == "APS-C":
    lFOCeff = lFOC *1.6
    st.markdown(f":gray[*Lunghezza focale effettiva: {lFOCeff}mm*]")




# --- Footer ---
# st.markdown("---")
# st.caption("Applicazione realizzata con [Streamlit](https://streamlit.io)")
