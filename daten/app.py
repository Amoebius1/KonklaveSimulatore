import streamlit as st
import pandas as pd
import json

# ==== Daten laden ====
@st.cache_data
def lade_kardinaele():
    return pd.read_csv("daten/kardinaele.csv")

@st.cache_data
def lade_papst():
    return pd.read_csv("daten/papst.csv")

@st.cache_data
def lade_einstellungen():
    with open("daten/einstellungen.json") as f:
        return json.load(f)

# ==== Daten anzeigen ====
st.set_page_config(page_title="Konklave-Simulator", page_icon="🕊️")
st.title("🕊️ Konklave-Simulator")

einstellungen = lade_einstellungen()
st.sidebar.markdown(f"📆 Aktuelles Jahr: **{einstellungen['jahr']}**")

st.subheader("👑 Aktueller Papst")
papst = lade_papst()
if papst.empty:
    st.info("Noch kein Papst gewählt.")
else:
    st.success(f"**Papst {papst.iloc[0]['Papstname']}**, ehemals {papst.iloc[0]['Vorname']} {papst.iloc[0]['Nachname']}")

st.subheader("🧑‍🦳 Kardinäle")
df = lade_kardinaele()
st.dataframe(df)
