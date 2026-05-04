import streamlit as st

def numerisation_hub_page():
    st.title("🔢 Hub Numérisation")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("⚙️ Optimisation", use_container_width=True):
            st.session_state["page"] = "⚙️ Optimisation"
            st.experimental_rerun()

        if st.button("🤖 Automatique", use_container_width=True):
            st.session_state["page"] = "🤖 Automatique"
            st.experimental_rerun()
    
    with col2:
        if st.button("📈 Intégration", use_container_width=True):
            st.session_state["page"] = "Intégration"
            st.experimental_rerun()

        if st.button("🔄 Interpolation", use_container_width=True):
            st.session_state["page"] = "Interpolation"
            st.experimental_rerun()
    
    with col3:
        if st.button("📐 Éq. Différentielles", use_container_width=True):
            st.session_state["page"] = "Éq. Diff"
            st.experimental_rerun()

        if st.button("📡 Signal", use_container_width=True):
            st.session_state["page"] = "Signal"
            st.experimental_rerun()