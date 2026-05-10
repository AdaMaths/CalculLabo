import warnings
warnings.filterwarnings("ignore")

import sys
import os
sys.path.append(os.path.dirname(__file__))

import streamlit as st

# Pages
from modules.gaussian import gaussian_page
from modules.laser_simulation import laser_page
from modules.cavity_losses import cavity_page
from modules.navier_stokes import navier_stokes_page
from modules.data_science import data_science_page
from modules.energy import energy_page
from modules.numerisation_hub import numerisation_hub_page

# Modules numériques
from modules.integration import integration_page
from modules.interpolation import interpolation_page
from modules.equ_diff import equ_diff_page
from modules.signal_analysis import signal_page
from modules.optimisation import optimisation_page
from modules.automatique import automatique_page

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