import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# ==========================================================
# PAGE ÉNERGIE
# ==========================================================

def energy_page():

    st.title("⚡ Analyse Énergétique")

    st.markdown("""
    ### Analyse de données énergétiques
    Cette page permet :
    - l'analyse des consommations,
    - les statistiques énergétiques,
    - la visualisation,
    - les prédictions simples.
    """)

    # ======================================================
    # UPLOAD
    # ======================================================

    uploaded_file = st.file_uploader(
        "Importer fichier CSV ou Excel",
        type=["csv", "xlsx"]
    )

    if uploaded_file is not None:

        try:

            # ==================================================
            # LECTURE DONNÉES
            # ==================================================

            # IMPORTANT :
            # PAS DE index_col=0

            if uploaded_file.name.endswith(".csv"):

                df = pd.read_csv(uploaded_file)

            else:

                df = pd.read_excel(uploaded_file)

            # ==================================================
            # SUPPRESSION AUTOMATIQUE
            # COLONNES UNNAMED
            # ==================================================

            df = df.loc[
                :,
                ~df.columns.str.contains("^Unnamed")
            ]

            st.success("✅ Données chargées avec succès")

            # ==================================================
            # APERÇU
            # ==================================================

            st.subheader("📋 Aperçu des données")

            st.dataframe(
                df,
                use_container_width=True
            )

            # ==================================================
            # INFORMATIONS
            # ==================================================

            st.subheader("📌 Informations générales")

            col1, col2, col3, col4 = st.columns(4)

            with col1:

                st.metric(
                    "Lignes",
                    df.shape[0]
                )

            with col2:

                st.metric(
                    "Colonnes",
                    df.shape[1]
                )

            with col3:

                st.metric(
                    "Valeurs nulles",
                    int(df.isnull().sum().sum())
                )

            with col4:

                numeric_count = len(
                    df.select_dtypes(
                        include=np.number
                    ).columns
                )

                st.metric(
                    "Variables numériques",
                    numeric_count
                )

            # ==================================================
            # TYPES DES DONNÉES
            # ==================================================

            st.subheader("🧾 Types des colonnes")

            dtype_df = pd.DataFrame({

                "Colonne": df.columns,

                "Type": df.dtypes.astype(str)

            })

            st.dataframe(
                dtype_df,
                use_container_width=True
            )

            # ==================================================
            # VALEURS MANQUANTES
            # ==================================================

            st.subheader("⚠️ Valeurs manquantes")

            missing_df = pd.DataFrame({

                "Colonne": df.columns,

                "Valeurs manquantes": df.isnull().sum()

            })

            st.dataframe(
                missing_df,
                use_container_width=True
            )

            # ==================================================
            # STATISTIQUES
            # ==================================================

            st.subheader("📈 Statistiques descriptives")

            st.dataframe(
                df.describe(),
                use_container_width=True
            )

            # ==================================================
            # VARIABLES NUMÉRIQUES
            # ==================================================

            numeric_cols = list(
                df.select_dtypes(
                    include=np.number
                ).columns
            )

            if len(numeric_cols) == 0:

                st.warning(
                    "❌ Aucune donnée numérique détectée"
                )

                return

            # ==================================================
            # VISUALISATIONS
            # ==================================================

            st.subheader("📊 Visualisations énergétiques")

            graph_type = st.selectbox(
                "Type de graphique",
                [
                    "Courbe",
                    "Scatter",
                    "Histogramme",
                    "Boxplot"
                ]
            )

            # ==================================================
            # CHOIX VARIABLES
            # ==================================================

            colx, coly = st.columns(2)

            with colx:

                x_col = st.selectbox(
                    "Variable X",
                    numeric_cols,
                    index=0
                )

            with coly:

                y_col = st.selectbox(
                    "Variable Y",
                    numeric_cols,
                    index=min(
                        1,
                        len(numeric_cols)-1
                    )
                )

            # ==================================================
            # COURBE
            # ==================================================

            if graph_type == "Courbe":

                fig = px.line(
                    df,
                    x=x_col,
                    y=y_col,
                    markers=True,
                    title=f"{x_col} vs {y_col}"
                )

            # ==================================================
            # SCATTER
            # ==================================================

            elif graph_type == "Scatter":

                fig = px.scatter(
                    df,
                    x=x_col,
                    y=y_col,
                    trendline="ols",
                    title=f"{x_col} vs {y_col}",
                    color=y_col
                )

            # ==================================================
            # HISTOGRAMME
            # ==================================================

            elif graph_type == "Histogramme":

                fig = px.histogram(
                    df,
                    x=x_col,
                    nbins=30,
                    title=f"Distribution de {x_col}",
                    color_discrete_sequence=["orange"]
                )

            # ==================================================
            # BOXPLOT
            # ==================================================

            else:

                fig = px.box(
                    df,
                    y=y_col,
                    title=f"Boxplot de {y_col}",
                    color_discrete_sequence=["green"]
                )

            fig.update_layout(
                template="plotly_white",
                height=600
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            # ==================================================
            # INDICATEURS ÉNERGÉTIQUES
            # ==================================================

            st.subheader("⚡ Indicateurs énergétiques")

            mean_val = df[y_col].mean()

            max_val = df[y_col].max()

            min_val = df[y_col].min()

            std_val = df[y_col].std()

            c1, c2, c3, c4 = st.columns(4)

            with c1:

                st.metric(
                    "Moyenne",
                    f"{mean_val:.2f}"
                )

            with c2:

                st.metric(
                    "Maximum",
                    f"{max_val:.2f}"
                )

            with c3:

                st.metric(
                    "Minimum",
                    f"{min_val:.2f}"
                )

            with c4:

                st.metric(
                    "Écart-type",
                    f"{std_val:.2f}"
                )

            # ==================================================
            # MATRICE CORRÉLATION
            # ==================================================

            st.subheader("🔥 Corrélations")

            corr = df[numeric_cols].corr()

            fig_corr = px.imshow(
                corr,
                text_auto=True,
                aspect="auto",
                title="Matrice de corrélation"
            )

            fig_corr.update_layout(
                height=700
            )

            st.plotly_chart(
                fig_corr,
                use_container_width=True
            )

            # ==================================================
            # MODÈLE PRÉDICTIF
            # ==================================================

            st.subheader("🤖 Modèle prédictif")

            target = st.selectbox(
                "Variable cible",
                numeric_cols
            )

            features = st.multiselect(
                "Variables explicatives",
                [
                    c for c in numeric_cols
                    if c != target
                ],
                default=[
                    c for c in numeric_cols
                    if c != target
                ]
            )

            if len(features) > 0:

                X = df[features]

                y = df[target]

                # ==============================================
                # SPLIT
                # ==============================================

                X_train, X_test, y_train, y_test = train_test_split(
                    X,
                    y,
                    test_size=0.2,
                    random_state=42
                )

                # ==============================================
                # MODEL
                # ==============================================

                model = LinearRegression()

                model.fit(
                    X_train,
                    y_train
                )

                predictions = model.predict(
                    X_test
                )

                r2 = r2_score(
                    y_test,
                    predictions
                )

                st.metric(
                    "Score R²",
                    f"{r2:.4f}"
                )

                # ==============================================
                # COEFFICIENTS
                # ==============================================

                st.subheader("📌 Coefficients")

                coef_df = pd.DataFrame({

                    "Variable": features,

                    "Coefficient": model.coef_

                })

                st.dataframe(
                    coef_df,
                    use_container_width=True
                )

                # ==============================================
                # EQUATION
                # ==============================================

                equation = (
                    f"y = {model.intercept_:.3f}"
                )

                for i, col in enumerate(features):

                    equation += (
                        f" + ({model.coef_[i]:.3f})×{col}"
                    )

                st.subheader(
                    "🧮 Équation du modèle"
                )

                st.code(equation)

                # ==============================================
                # RÉEL VS PRÉDIT
                # ==============================================

                fig_pred = go.Figure()

                fig_pred.add_trace(
                    go.Scatter(
                        x=y_test,
                        y=predictions,
                        mode='markers',
                        name='Prédictions'
                    )
                )

                fig_pred.add_trace(
                    go.Scatter(
                        x=[
                            y_test.min(),
                            y_test.max()
                        ],
                        y=[
                            y_test.min(),
                            y_test.max()
                        ],
                        mode='lines',
                        name='Idéal'
                    )
                )

                fig_pred.update_layout(
                    title="Valeurs réelles vs prédites",
                    xaxis_title="Réel",
                    yaxis_title="Prédit",
                    height=600,
                    template="plotly_white"
                )

                st.plotly_chart(
                    fig_pred,
                    use_container_width=True
                )

                # ==============================================
                # PREDICTION UTILISATEUR
                # ==============================================

                st.subheader("🔮 Faire une prédiction")

                input_data = {}

                cols = st.columns(2)

                for i, feature in enumerate(features):

                    with cols[i % 2]:

                        input_data[feature] = st.number_input(
                            feature,
                            value=float(
                                df[feature].mean()
                            ),
                            step=0.1
                        )

                if st.button("🚀 Prédire"):

                    input_df = pd.DataFrame(
                        [input_data]
                    )

                    prediction = model.predict(
                        input_df
                    )[0]

                    st.success(
                        f"✅ Valeur prédite : {prediction:.4f}"
                    )

            # ==================================================
            # EXPORT
            # ==================================================

            st.subheader("💾 Export des données")

            csv = df.to_csv(
                index=False
            ).encode("utf-8")

            st.download_button(
                "📥 Télécharger CSV",
                csv,
                "energy_export.csv",
                "text/csv"
            )

        except Exception as e:

            st.error(f"❌ Erreur : {e}")

    else:

        st.info("""
        👆 Importez un fichier CSV ou Excel contenant des données énergétiques.
        """)