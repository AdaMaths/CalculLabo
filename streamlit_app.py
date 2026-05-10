import warnings
warnings.filterwarnings("ignore")

import sys
import os
sys.path.append(os.path.dirname(__file__))

import streamlit as st

# Pages
from pages.gaussian import gaussian_page
from pages.laser_simulation import laser_page
from pages.cavity_losses import cavity_page
from pages.navier_stokes import navier_stokes_page
from pages.data_science import data_science_page
from pages.energy import energy_page
from pages.numerisation_hub import numerisation_hub_page

# Modules numériques
from pages.integration import integration_page
from pages.interpolation import interpolation_page
from pages.equ_diff import equ_diff_page
from pages.signal_analysis import signal_page
from pages.optimisation import optimisation_page
from pages.automatique import automatique_page

st.set_page_config(
    page_title="Calcul Scientifique PRO",
    page_icon="🔬",
    layout="wide"
)

def main():
    if "page" not in st.session_state:
        st.session_state["page"] = "🏠 Accueil"

    st.title("🔬 Application de Calcul Scientifique PRO")

    menu = [
        "🏠 Accueil",
        "📈 Profil Gaussien",
        "🔦 Simulation Laser",
        "🪞 Pertes de Cavité",
        "🌊 Navier-Stokes",
        "📊 Data Science",
        "⚡ Énergie",
        "🔢 Hub Numérisation",
        "⚙️ Optimisation",
        "🤖 Automatique",
        "Intégration",
        "Interpolation",
        "Éq. Diff",
        "Signal",
    ]

    page = st.sidebar.radio(
        "Menu",
        menu,
        index=menu.index(st.session_state["page"])
    )

    st.session_state["page"] = page

    page_map = {
        "🏠 Accueil": show_home,
        "📈 Profil Gaussien": gaussian_page,
        "🔦 Simulation Laser": laser_page,
        "🪞 Pertes de Cavité": cavity_page,
        "🌊 Navier-Stokes": navier_stokes_page,
        "📊 Data Science": data_science_page,
        "⚡ Énergie": energy_page,
        "🔢 Hub Numérisation": numerisation_hub_page,
        "⚙️ Optimisation": optimisation_page,
        "🤖 Automatique": automatique_page,
        "Intégration": integration_page,
        "Interpolation": interpolation_page,
        "Éq. Diff": equ_diff_page,
        "Signal": signal_page,
    }

    page_map[st.session_state["page"]]()

def show_home():
    st.markdown("## Bienvenue 👋")
    st.info("Application scientifique complète")

if __name__ == "__main__":
    main()