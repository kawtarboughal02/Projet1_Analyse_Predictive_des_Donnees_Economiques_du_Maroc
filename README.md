# 📊 Analyse prédictive des données économiques du Maroc

# Predictive Analysis of Morocco's Economic Data

*[Français](#français) — [English](#english)*

---

<a name="français"></a>
## 🇫🇷 Français

### Présentation :

Ce projet analyse l'évolution des principales variables macroéconomiques du Maroc entre 2000 et 2024 — PIB, inflation et chômage — puis teste la capacité de modèles prédictifs simples à anticiper le taux de chômage à court terme.

Il s'inscrit dans une logique de projet Data Science et IA appliquée, avec une démarche complète : collecte de données réelles, nettoyage, fusion, analyse exploratoire, visualisation, feature engineering, modélisation, évaluation critique et documentation reproductible.

Le rapport complet est disponible dans [outputs/rapport_final.md](outputs/rapport_final.md).

### Contexte :

Le Maroc publie régulièrement des indicateurs économiques via la Banque Mondiale et les institutions officielles, mais ces données restent souvent dispersées et peu exploitées de manière intégrée. Ce projet vise à les structurer, les analyser, puis les mettre en perspective avec une modélisation prédictive simple et honnête.

### Problématique :

Comment évoluent les principaux indicateurs macroéconomiques marocains entre 2000 et 2024, et dans quelle mesure peut-on prédire le chômage à court terme à partir d'informations économiques disponibles l'année précédente ?

### Structure du projet :

```text
.
├── data/
│   ├── raw/                     # Données brutes World Bank
│   └── processed/               # Données nettoyées et fusionnées
├── notebooks/
│   ├── 01_exploration.ipynb
│   ├── 02_nettoyage.ipynb
│   ├── 03_analyse_visualisation.ipynb
│   └── 04_modelisation.ipynb
├── src/
│   ├── cleaning.py
│   ├── data_loader.py
│   └── visualization.py
├── images/
│   ├── correlation.png
│   ├── evolution_indicateurs.png
│   ├── feature_importance.png
│   ├── inflation_interactive.html
│   ├── inflation_interactive.png
│   └── predictions_comparaison.png
├── outputs/
│   └── rapport_final.md
├── .gitignore
├── requirements.txt
├── README.md
├── check_model.py
└── validate_project.py
```

### Méthodologie :

1. **Collecte** des données macroéconomiques (PIB, inflation, chômage) auprès de la Banque Mondiale.
2. **Nettoyage et structuration** avec Pandas : filtrage du Maroc, transposition en série temporelle.
3. **Fusion** des trois séries annuelles sur l'axe temporel commun.
4. **Analyse exploratoire** : statistiques descriptives, repérage des années extrêmes, corrélations.
5. **Visualisation** : courbes d'évolution, heatmap de corrélation, graphique interactif Plotly.
6. **Feature engineering** : variables décalées d'un an (lag), moyennes mobiles sur 3 ans.
7. **Modélisation** : Régression Linéaire vs Random Forest, cible = taux de chômage.
8. **Validation chronologique** (train sur les années anciennes, test sur 2020-2024) et interprétation critique des limites.

### Résultats clés :

**Corrélation entre indicateurs (2000-2024) :**

| Indicateur | PIB | Inflation | Chômage |
|---|---:|---:|---:|
| PIB | 1.00 | 0.15 | -0.74 |
| Inflation | 0.15 | 1.00 | -0.15 |
| Chômage | -0.74 | -0.15 | 1.00 |

- **PIB / chômage : -0,74** — corrélation forte et négative, cohérente avec la loi d'Okun : la croissance s'accompagne globalement d'une baisse du chômage.
- **PIB / inflation : 0,15** — lien faible ; l'inflation récente est surtout tirée par des chocs externes (énergie, guerre en Ukraine).
- **Inflation / chômage : -0,15** — faible, ne confirme pas clairement la courbe de Phillips sur cette période.

**Modélisation du chômage (test 2020-2024) :**

| Modèle | MAE (pts de %) | RMSE (pts de %) | R² |
|---|---:|---:|---:|
| Régression Linéaire | 1.370 | 1.545 | -2.029 |
| Random Forest | 0.736 | 0.984 | -0.229 |

Les deux modèles ne généralisent pas parfaitement sur la période 2020-2024, qui correspond à un choc économique mondial inédit dans l'historique d'entraînement. Le Random Forest se dégrade nettement moins que la Régression Linéaire. Ce résultat est interprété de manière critique dans le rapport final — un vrai signe de maturité scientifique, pas une faiblesse cachée.

Le graphique interactif de l'inflation est disponible dans [images/inflation_interactive.html](images/inflation_interactive.html) (version statique : [images/inflation_interactive.png](images/inflation_interactive.png)).

### Points forts de ce projet :

Ce projet est un bon support de candidature en Data Science / Intelligence Artificielle, à condition d'être présenté avec une documentation honnête qui démontre :

- une logique de travail complète et reproductible ;
- une compréhension du problème économique et de la série temporelle ;
- une méthodologie propre, sans fuite d'information (data leakage) ;
- une évaluation critique des limites du dataset et des modèles ;
- une capacité à expliquer les résultats, même quand le modèle ne performe pas parfaitement.

### Limites du projet :

- Taille d'échantillon limitée (25 observations annuelles, 23 après feature engineering).
- Période de test atypique (choc Covid-19, 2020-2024).
- Peu de variables explicatives (3 indicateurs macroéconomiques).
- Modèles volontairement simples, adaptés à un aussi petit volume de données.

### Installation :

```bash
git clone https://github.com/kawtarboughal02/Projet1_Analyse_Prédictive_des_Données_Économiques_du_Maroc.git
cd Projet1_Analyse_Prédictive_des_Données_Économiques_du_Maroc
python -m venv venv
source venv/bin/activate   # Windows : venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook
```

### Lancer les notebooks :

Exécuter dans l'ordre : `01_exploration.ipynb` → `02_nettoyage.ipynb` → `03_analyse_visualisation.ipynb` → `04_modelisation.ipynb`

### Scripts complémentaires :

- `validate_project.py` : relance automatiquement les 4 notebooks pour vérifier qu'ils fonctionnent sans erreur (`python validate_project.py`).
- `check_model.py` : refait les calculs du modèle dans un seul script, sans passer par Jupyter — pratique pour une démonstration rapide (`python check_model.py`).

### Technologies :

Python · Pandas · NumPy · Matplotlib · Seaborn · Plotly · Scikit-learn · Jupyter Notebook

### Auteur :

**Kawtar Boughal**
[GitHub](https://github.com/kawtarboughal02) · [LinkedIn](https://www.linkedin.com/in/kawtar-boughal02)

Voir aussi le rapport détaillé : [outputs/rapport_final.md](outputs/rapport_final.md)

---

<a name="english"></a>
## 🇬🇧 English

### Overview :

This project analyzes the evolution of Morocco's main macroeconomic indicators between 2000 and 2024 — GDP, inflation, and unemployment — and tests whether simple predictive models can forecast the unemployment rate in the short term.

It follows a complete Data Science / applied AI workflow: real-data collection, cleaning, merging, exploratory analysis, visualization, feature engineering, modeling, critical evaluation, and reproducible documentation.

The full report is available in [outputs/rapport_final.md](outputs/rapport_final.md) (French).

### Context :

Morocco regularly publishes economic indicators through the World Bank and official institutions, but this data remains scattered and rarely analyzed in an integrated way. This project structures it, analyzes it, and puts it in perspective through simple, honestly-evaluated predictive modeling.

### Research question :

How have Morocco's main macroeconomic indicators evolved between 2000 and 2024, and to what extent can unemployment be predicted in the short term using the previous year's economic information?

### Methodology :

1. **Collection** of GDP, inflation, and unemployment data from the World Bank.
2. **Cleaning and structuring** with Pandas: filtering Morocco, reshaping into a time series.
3. **Merging** the three annual series on a common year index.
4. **Exploratory analysis**: descriptive statistics, extreme-year detection, correlations.
5. **Visualization**: trend charts, correlation heatmap, interactive Plotly chart.
6. **Feature engineering**: one-year lag variables, 3-year rolling averages.
7. **Modeling**: Linear Regression vs. Random Forest, target = unemployment rate.
8. **Chronological validation** (training on earlier years, testing on 2020-2024) and critical interpretation of limitations.

### Key results :

**Correlation between indicators (2000-2024):**
- **GDP / unemployment: -0.74** — strong negative correlation, consistent with Okun's law: economic growth is broadly associated with falling unemployment.
- **GDP / inflation: 0.15** — weak link; recent Moroccan inflation is mainly driven by external shocks (energy prices, the war in Ukraine).
- **Inflation / unemployment: -0.15** — weak, does not clearly confirm the classic Phillips curve over this period.

**Unemployment modeling (2020-2024 test set):**

| Model | MAE (pp) | RMSE (pp) | R² |
|---|---:|---:|---:|
| Linear Regression | 1.370 | 1.545 | -2.029 |
| Random Forest | 0.736 | 0.984 | -0.229 |

Both models fail to fully generalize on the 2020-2024 test period, which coincides with a global economic shock unprecedented in the training data. Random Forest degrades noticeably less than Linear Regression. This negative result is interpreted in detail in the full report rather than hidden — a sign of methodological maturity, not a weakness.

### Why this project matters :

This project is a solid portfolio piece for Data Science / AI applications, when presented with honest documentation that demonstrates:

- a complete, reproducible end-to-end workflow;
- a real understanding of the economic problem and of time-series constraints;
- a clean methodology with no data leakage (predictions rely only on prior-year information);
- critical awareness of the dataset's and models' limitations;
- the ability to explain results even when the model does not perform perfectly.

### Limitations :

- Limited sample size (25 annual observations, 23 after feature engineering).
- An atypical test period (the Covid-19 shock, 2020-2024).
- Few explanatory variables (3 macroeconomic indicators).
- Deliberately simple models, appropriate for such a small dataset.

### Setup :

```bash
git clone https://github.com/kawtarboughal02/Projet1_Analyse_Prédictive_des_Données_Économiques_du_Maroc.git
cd Projet1_Analyse_Prédictive_des_Données_Économiques_du_Maroc
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook
```

Run the notebooks in order: `01_exploration.ipynb` → `02_nettoyage.ipynb` → `03_analyse_visualisation.ipynb` → `04_modelisation.ipynb`

### Supporting scripts :

- `validate_project.py`: automatically re-runs all 4 notebooks end-to-end to catch any error.
- `check_model.py`: reproduces the modeling pipeline in a single standalone script, useful for a quick demo.

### Tech stack :

Python · Pandas · NumPy · Matplotlib · Seaborn · Plotly · Scikit-learn · Jupyter Notebook

### Author :

**Kawtar Boughal**
[GitHub](https://github.com/kawtarboughal02) · [LinkedIn](https://www.linkedin.com/in/kawtar-boughal02)

See also the detailed report: [outputs/rapport_final.md](outputs/rapport_final.md) (French)