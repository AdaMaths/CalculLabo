import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def data_science_page():
    st.markdown("## 📊 Outils Data Science")

    tab1, tab2, tab3 = st.tabs(["📁 Charger", "📈 Visualiser", "📊 Stats"])

    # ================= TAB 1 =================
    with tab1:
        uploaded_file = st.file_uploader("Charger CSV", type="csv")

        if uploaded_file:
            try:
                df = pd.read_csv(uploaded_file)
                st.session_state["df"] = df
                st.success("Fichier chargé")
            except:
                st.error("Erreur lecture fichier")

        if st.button("Charger exemple"):
            df = pd.DataFrame({
                "x": np.arange(10),
                "y": np.random.randn(10)
            })
            st.session_state["df"] = df
            st.success("Exemple chargé")

    # ================= TAB 2 =================
    with tab2:
        if "df" in st.session_state:
            df = st.session_state["df"]

            st.dataframe(df.head(), use_container_width=True)

            num_cols = df.select_dtypes(include=np.number).columns.tolist()

            if num_cols:
                col = st.selectbox("Colonne", num_cols)

                fig = px.line(df, y=col)
                st.plotly_chart(fig, use_container_width=True)

                fig2 = px.histogram(df, x=col)
                st.plotly_chart(fig2, use_container_width=True)

        else:
            st.warning("Charge un dataset")

    # ================= TAB 3 =================
    with tab3:
        if "df" in st.session_state:
            df = st.session_state["df"]

            st.dataframe(df.describe(), use_container_width=True)

            num_df = df.select_dtypes(include=np.number)

            if num_df.shape[1] > 1:
                corr = num_df.corr()
                fig = px.imshow(corr, text_auto=True)
                st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("Charge un dataset")