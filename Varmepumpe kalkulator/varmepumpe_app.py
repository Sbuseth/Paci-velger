import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Varmepumpekalkulator for næringsbygg", layout="wide")

st.image(r"C:\\Users\\sande\\OneDrive\\Skrivebord\\Varmepumpe kalkulator\\logo.png", width=400)

st.markdown("### Sander's VP kalkis")
st.title("Varmepumpekalkulator for næringsbygg")

# Panasonic modeller med riktige innedeler og koblet effekt/COP
panasonic_modeller = {
    "Elite": {
        "U-36PZH3E5": {
            "S-25PY3E": {"effekt": 4.0, "cop": 4.12},
	    "S-2545PK4E": {"effekt": 4.0, "cop": 4.26},	
            "S-36PY3E": {"effekt": 4.0, "cop": 4.12},
            "S-3650PU3E": {"effekt": 4.0, "cop": 5.41},
            "S-3650PT3E": {"effekt": 4.0, "cop": 5.00},
            "S-3650PF3E": {"effekt": 4.0, "cop": 4.17}
        },
        "U-50PZH3E5": {
            "S-50PY3E": {"effekt": 5.6, "cop": 3.37},
	    "S-5010PK4E": {"effekt": 5.6, "cop": 4.03},
            "S-3650PU3E": {"effekt": 5.6, "cop": 4.24},
            "S-3650PT3E": {"effekt": 5.6, "cop": 4.03},
            "S-3650PF3E": {"effekt": 5.6, "cop": 3.61}
        },
        "U-60PZH3E5": {
	    "S-5010PK4E": {"effekt": 7.0, "cop": 4.12}, 
            "S-60PY3E": {"effekt": 7.0, "cop": 3.35},
            "S-6071PU3E": {"effekt": 7.0, "cop": 4.02},
            "S-6071PT3E": {"effekt": 7.0, "cop": 4.14},
            "S-6071PF3E": {"effekt": 7.0, "cop": 3.74}
        },
        "U-71PZH4E5": {
	    "S-5010PK4E": {"effekt": 7.8, "cop": 4.00},
            "S-6071PU3E": {"effekt": 8.0, "cop": 4.30},
            "S-6071PT3E": {"effekt": 8.0, "cop": 3.96},
            "S-6071PF3E": {"effekt": 7.5, "cop": 4.03}
        },
        "U-100PZH4E5": {
	    "S-5010PK4E": {"effekt": 9.5, "cop": 3.89},
            "S-1014PU3E": {"effekt": 11.2, "cop": 5.00},
            "S-1014PT3E": {"effekt": 11.2, "cop": 4.00},
            "S-1014PF3E": {"effekt": 9.5, "cop": 3.89}
        },
        "U-125PZH4E5": {
            "S-1014PU3E": {"effekt": 14.0, "cop": 4.61},
            "S-1014PT3E": {"effekt": 14.0, "cop": 3.78},
            "S-1014PF3E": {"effekt": 13.5, "cop": 3.46}
        },
        "U-140PZH4E5": {
            "S-1014PT3E": {"effekt": 16.0, "cop": 3.38},
	    "S-1014PF3E": {"effekt": 15.5, "cop": 3.33},
	    "S-1014PU3E": {"effekt": 16.0, "cop": 4.3},
            "P-VTVF140MC5-PE": {"effekt": 14.0, "cop": 3.88}
            
        },
        "U-200PZH4E8": {
            "S-200PE4E": {"effekt": 22.4, "cop": 3.55}
            
        },
        "U-250PZH4E8": {
            "S-250PE4E": {"effekt": 24.0, "cop": 3.55},
            "P-VTVF250MC5-PE": {"effekt": 26.7, "cop": 3.74}
 
        }
    },
    "Standard": {
        "U-36PZ3E5": {
	    "S-2545PK4E": {"effekt": 3.6, "cop": 4.09},
            "S-36PY3E": {"effekt": 3.6, "cop": 4.29},
            "S-3650PU3E": {"effekt": 3.6, "cop": 5.07},
            "S-3650PT3E": {"effekt": 3.5, "cop": 4.61},
            "S-3650PF3E": {"effekt": 3.4, "cop": 4.15}
        },
        "U-50PZ3E5": {
	    "S-5010PK4E": {"effekt": 5.0, "cop": 4.20},
            "S-50PY3E": {"effekt": 5.0, "cop": 3.94},
            "S-3650PU3E": {"effekt": 5.0, "cop": 4.63},
            "S-3650PT3E": {"effekt": 5.0, "cop": 3.73},
            "S-3650PF3E": {"effekt": 5.0, "cop": 3.62}
        },
        "U-60PZ3E5A": {
	    "S-5010PK4E": {"effekt": 6.1, "cop": 4.27},
            "S-60PY3E": {"effekt": 6.0, "cop": 3.61},
            "S-6071PU3E": {"effekt": 6.0, "cop": 4.48},
            "S-6071PT3E": {"effekt": 6.0, "cop": 4.11},
            "S-6071PF3E": {"effekt": 5.7, "cop": 4.04}
        },
        "U-71PZ3E5A": {
	    "S-5010PK4E": {"effekt": 7.1, "cop": 4.10},
            "S-6071PU3E": {"effekt": 7.1, "cop": 4.23},
            "S-6071PT3E": {"effekt": 6.8, "cop": 4.20},
            "S-6071PF3E": {"effekt": 6.8, "cop": 4.00}
        },
        "U-100PZ3E5": {
	    "S-5010PK4E": {"effekt": 9.0, "cop": 3.81},
            "S-1014PU3E": {"effekt": 10.0, "cop": 4.93},
            "S-1014PT3E": {"effekt": 10.0, "cop": 4.24},
            "S-1014PF3E": {"effekt": 9.5, "cop": 4.09},
        },
        "U-125PZ3E5": {
            "S-1014PU3E": {"effekt": 12.5, "cop": 4.43},
            "S-1014PT3E": {"effekt": 12.5, "cop": 3.89},
            "S-1014PF3E": {"effekt": 12.1, "cop": 3.56}
        },
        "U-140PZ3E5": {
            "S-1014PT3E": {"effekt": 14.0, "cop": 3.70},
	    "S-1014PF3E": {"effekt": 13.4, "cop": 3.76},
	    "S-1014PU3E": {"effekt": 14.0, "cop": 4.18}
            
        }
    }
}

# Brukervalg i sidebar
st.sidebar.header("1. Nåværende situasjon")
forbruk_i_dag = st.sidebar.number_input("Totalt strømforbruk i dag (kWh/år)", min_value=0, value=100_000, step=1000)
prosent_varme = st.sidebar.slider("Prosentandel av strøm som går til oppvarming (%)", min_value=0, max_value=100, value=60)

st.sidebar.header("2. Varmepumpevalg")
valgt_kategori = st.sidebar.selectbox("Velg type Panasonic-modell", list(panasonic_modeller.keys()))
valgt_utedel = st.sidebar.selectbox("Velg utedel", list(panasonic_modeller[valgt_kategori].keys()))
valgt_innedele = st.sidebar.selectbox("Velg innedel", list(panasonic_modeller[valgt_kategori][valgt_utedel].keys()))

data = panasonic_modeller[valgt_kategori][valgt_utedel][valgt_innedele]
cop = data["cop"]
effekt_vp = data["effekt"]

st.sidebar.header("3. Økonomiske parametere")
vedlikehold = st.sidebar.number_input("Årlig vedlikeholdskostnad (kr)", min_value=0, value=2000, step=100)
levetid = st.sidebar.number_input("Levetid på varmepumpe (år)", min_value=1, value=15, step=1)
investering = st.sidebar.number_input("Investeringskostnad (kr)", min_value=0, value=200000, step=1000)
strompris = st.sidebar.number_input("Strømpris (kr/kWh)", min_value=0.0, value=1.20, step=0.01)

# Beregninger
forbruk_varme_dag = forbruk_i_dag * (prosent_varme / 100)
forbruk_varme_etter = forbruk_varme_dag / cop
forbruk_etter = forbruk_i_dag - forbruk_varme_dag + forbruk_varme_etter

besparelse_kwh = forbruk_i_dag - forbruk_etter
besparelse_prosent = (besparelse_kwh / forbruk_i_dag * 100) if forbruk_i_dag > 0 else 0
besparelse_kr = besparelse_kwh * strompris
npv = sum([(besparelse_kr - vedlikehold) / ((1 + 0.04) ** year) for year in range(1, levetid + 1)]) - investering

# Resultater
st.markdown("---")
st.subheader("Resultater med valgt modell")
st.write(f"Valgt segment: {valgt_kategori}")
st.write(f"Valgt utedel: {valgt_utedel}")
st.write(f"Valgt innedel: {valgt_innedele}")
st.write(f"Effekt: {effekt_vp:,.1f} kW")
st.write(f"COP: {cop:.2f}")

st.markdown("---")
st.subheader("Energiberegninger")
st.write(f"Strømforbruk til oppvarming i dag: {forbruk_varme_dag:,.0f} kWh/år")
st.write(f"Strømforbruk til oppvarming etter installasjon: {forbruk_varme_etter:,.0f} kWh/år")
st.write(f"Totalt strømforbruk etter installasjon: {forbruk_etter:,.0f} kWh/år")

st.markdown("---")
st.subheader("Besparelser og økonomi")
st.write(f"Årlig besparelse i kWh: {besparelse_kwh:,.0f} kWh ({besparelse_prosent:.1f} %)")
st.write(f"Årlig besparelse i kroner: {besparelse_kr:,.0f} kr")
st.write(f"Investering: {investering:,.0f} kr")
st.write(f"Årlig vedlikehold: {vedlikehold:,.0f} kr")
st.write(f"Levetid: {levetid} år")
st.write(f"Netto nåverdi (NPV): {npv:,.0f} kr")

st.caption("Utviklet av Sander Buseth")






