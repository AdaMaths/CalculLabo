# Application de Calcul Scientifique Streamlit

Application web Streamlit pour effectuer des calculs scientifiques et des simulations en physique et mathématiques.

## Installation

1. Créer un environnement virtuel:
```bash
python -m venv venv
# Sur macOS / Linux
source venv/bin/activate
# Sur Windows
venv\Scripts\activate
```

2. Installer les dépendances:
```bash
pip install -r requirements.txt
```

3. Lancer l'application:
```bash
streamlit run streamlit_app.py
```

L'application s'ouvrira ensuite dans votre navigateur à `http://localhost:8510/`.

> Si le port `8510` est occupé, utilisez un autre port, par exemple :
>
> ```bash
> #8512, 8513, 850514......
> ```

## Fonctionnalités

- **Profil Gaussien**: génération et visualisation de courbes gaussiennes
- **Simulation Laser**: modélisation de la dynamique laser
- **Pertes de Cavité**: analyse des pertes optiques dans une cavité
- **Optimisation**: minimisation et optimisation de fonctions
- **Automatique**: analyse de systèmes et contrôle
- **Navier-Stokes**: simulation de fluides et écoulements
- **Data Science**: exploration de données et visualisations
- **Énergie**: calculs et représentations autour de l'énergie
- **Numérisation Hub**: options de numérisation et export de données
- **Intégration**: calculs d'intégrales numériques
- **Interpolation**: interpolation et approximation de données
- **Équations différentielles**: résolution et visualisation
- **Signal**: traitement et affichage de signaux

## Structure du projet

project_TUTOR/
├── streamlit_app.py          # Application principale Streamlit
├── pages/
│   ├── __init__.py
│   ├── automatique.py
│   ├── cavity_losses.py
│   ├── data_science.py
│   ├── energy.py
│   ├── equ_diff.py
│   ├── gaussian.py
│   ├── integration.py
│   ├── interpolation.py
│   ├── laser_simulation.py
│   ├── navier_stokes.py
│   ├── numerisation_hub.py
│   ├── optimisation.py
│   └── signal.py
├── requirements.txt          # Dépendances Python
└── README.md                 # Documentation
```

## Dépendances

Les packages utilisés dans ce projet sont :

- streamlit==1.28.1
- numpy==1.26.3
- scipy==1.11.4
- matplotlib==3.8.2
- plotly==5.17.0
- pandas==2.1.0
- python-dotenv==1.0.0
- pillow==10.0.0

## Commandes utiles

```bash
# Lancer l'application
python -m streamlit run streamlit_app.py

# Lancer sur un port spécifique
streamlit run streamlit_app.py --server.port=8502

# Activer le mode debug de Streamlit
streamlit run streamlit_app.py --logger.level=debug
```

## Notes

- L'application est modulaire et chaque page est indépendante
- Les pages sont hébergées dans le dossier `pages/`
- Si Streamlit indique qu'un port est occupé, changez le port avec `--server.port`
- Vérifiez que l'environnement Pythostreamlit run streamlit_app.py --server.port=8511n actif contient toutes les dépendances requises

## ⚡ Page Énergie — guide rapide

- Ouvrez la page **⚡ Énergie** dans la barre latérale.
- Vous pouvez **charger votre fichier Excel/CSV** contenant les colonnes `Ch 1`..`Ch 7` (optionnellement `Heure`).
- Ou cochez **"Utiliser un jeu d'exemple"** pour charger un dataset synthétique et lancer l'entraînement.
- Après l'entraînement, vous pouvez **télécharger le meilleur modèle** au format pickle depuis l'interface.

Fichier d'exemple disponible : `assets/energy_sample.csv`.



