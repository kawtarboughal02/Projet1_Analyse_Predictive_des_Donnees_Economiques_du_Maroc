# Rapport final — Analyse prédictive des données économiques du Maroc

## 1. Résumé exécutif :

Ce projet consiste en une analyse macroéconomique du Maroc sur la période 2000-2024, à partir de trois séries officielles et comparables : PIB, inflation et chômage. L’objectif est double : comprendre les dynamiques structurelles de l’économie marocaine et tester si une modélisation prédictive simple peut anticiper le taux de chômage à court terme.

Le pipeline suit l’approche standard d’un projet Data Science de qualité : collecte, nettoyage, exploration, visualisation, feature engineering, modélisation comparée, évaluation et interprétation. Le point clé n’est pas seulement d’obtenir un score élevé, mais surtout de montrer une vraie compréhension du problème, de la série temporelle et des limites du jeu de données.

Les résultats indiquent une relation forte entre croissance économique et baisse du chômage sur la période étudiée, avec toutefois une modélisation qui ne généralise pas parfaitement sur la période 2020-2024, justement la période la plus atypique du fait du choc mondial lié à la pandémie. Ce résultat est présenté comme un enseignement scientifique, pas comme un échec caché.

---

## 2. Contexte et objectif :

Le Maroc est un pays dont les indicateurs macroéconomiques sont régulièrement publiés par la Banque Mondiale et les institutions statistiques nationales. Ces données, bien que souvent disponibles, restent peu exploitées de manière intégrée et visuellement claire. Le projet vise donc à transformer ces informations en une lecture utile, structurée et reproductible.

L’objectif principal est de construire une analyse complète du contexte économique marocain et d’évaluer si des variables macroéconomiques passées permettent de prédire le chômage. Cette démarche est particulièrement intéressante pour une candidature en Data Science, car elle montre à la fois :

- la maîtrise de la manipulation de données réelles ;
- la capacité à travailler sur des séries temporelles ;
- la compréhension économique du problème ;
- la capacité à évaluer objectivement les limites d’un modèle ;
- une démarche de recherche appliquée, à la fois scientifique et professionnelle.

---

## 3. Données et sources :

Les données proviennent de la Banque Mondiale, sous forme de fichiers CSV. Les indicateurs sélectionnés sont :

- PIB (valeur nominale en dollars US courants) ;
- inflation (taux d’inflation annuel en %) ;
- chômage (taux de chômage total en %).

Période étudiée : 2000-2024.

Le dataset contient 25 observations annuelles. Cette dimension est limitée, ce qui est un point crucial à mentionner dans ce type de projet : le volume est trop petit pour espérer des modèles très complexes ou des performances lisses sur toutes les périodes.

---

## 4. Méthodologie détaillée :

### 4.1 Étape 1 — collecte des données :

Le projet part de trois fichiers bruts téléchargés sur le site de la Banque Mondiale :

- inflation.csv
- chomage.csv
- pib.csv

Ces fichiers contiennent un grand nombre de pays et de colonnes annuelles, ainsi que des métadonnées au début du fichier. Le travail a consisté à filtrer les données relatives au Maroc puis à les restructurer en série temporelle.

### 4.2 Étape 2 — nettoyage et fusion :

Les opérations principales ont été :

- suppression des lignes de métadonnées inutiles ;
- sélection de la ligne du Maroc ;
- sélection des années 2000-2024 ;
- transposition des données pour avoir une ligne par année ;
- renommage des variables ;
- conversion des indices en entiers ;
- tri chronologique ;
- fusion des trois séries sur l’axe des années ;
- vérification de la présence de valeurs manquantes ;
- interpolation linéaire des trous, lorsqu’ils étaient justifiés par la continuité de la série.

Cette étape est essentielle car elle garantit la qualité de la base exploitable sans faire de “manipulation magique” sur les données.

### 4.3 Étape 3 — analyse exploratoire des données :

L’analyse exploratoire a porté sur :

- statistique descriptive ;
- repérage des dates extrêmes ;
- corrélations entre indicateurs ;
- lecture de l’évolution temporelle.

Les principales conclusions sont les suivantes :

- le PIB et le chômage évoluent en sens opposé sur la période ;
- le PIB et l’inflation n’ont pas de relation forte et stable ;
- l’inflation a connu un pic notable en 2022, cohérent avec une perturbation mondiale des prix ;
- la série de chômage est globalement décroissante sur le long terme, mais elle reste volatile lors des périodes de choc.

### 4.4 Étape 4 — visualisation :

Le projet produit des visualisations de qualité permettant de comprendre le contexte de manière rapide et claire :

- évolution du PIB, de l’inflation et du chômage ;
- heatmap de corrélation ;
- graphique interactif de l’inflation ;
- visualisation des prédictions et de l’importance des variables.

Les graphiques sont utiles à deux niveaux :

1. pour la compréhension scientifique ;
2. pour le storytelling de la candidature ou de la soutenance.

### 4.5 Étape 5 — feature engineering :

Pour rendre la prédiction réaliste, les variables ne doivent pas inclure des informations qui ne sont pas connues au moment de la prédiction. C’est pourquoi le modèle a été construit sur des caractéristiques décalées d’un an ou calculées à partir du passé.

Les variables créées sont :

- pib_lag1 : PIB de l’année précédente ;
- inflation_lag1 : inflation de l’année précédente ;
- chomage_lag1 : chômage de l’année précédente ;
- pib_rolling3 : moyenne mobile sur 3 ans du PIB ;
- inflation_rolling3 : moyenne mobile sur 3 ans de l’inflation.

La suppression des premières lignes incomplètes est une étape normale en séries temporelles et ne doit pas être considérée comme une faiblesse du projet, mais comme une caractéristique méthodologique légitime.

### 4.6 Étape 6 — modélisation prédictive :

Le modèle cible est le taux de chômage, puisque c’est un indicateur central de la situation économique et un objectif pertinent à court terme.

Le découpage est chronologique et non aléatoire :

- période d’entraînement : années anciennes ;
- période de test : 5 dernières années, 2020-2024.

Cette décision est fondamentale en série temporelle. Un train/test aléatoire introduirait une fuite d’information : le modèle apprendrait sur des observations futures tout en évaluant sur des observations passées, ce qui est totalement invalide.

Les modèles comparés sont :

- Régression Linéaire : référence simple et interprétable ;
- Random Forest Regressor : modèle non linéaire, plus flexible, plus adapté à des relations complexes, mais également plus sensible au faible volume de données.

### 4.7 Étape 7 — évaluation des modèles :

Les métriques utilisées sont :

- MAE : erreur absolue moyenne ;
- RMSE : racine carrée de la moyenne des erreurs au carré ;
- R² : qualité globale de l’ajustement.

Le point le plus important est que l’évaluation n’est pas seulement chiffrée : elle doit être interprétée. Ici, l’interprétation est immédiatement claire : la période de test est un contexte atypique, et le modèle n’a pas le volume d’information suffisant pour anticiper un choc inédit de cette nature.

---

## 5. Résultats et interprétation :

### 5.1 Corrélation entre indicateurs :

| Indicateur | PIB | Inflation | Chômage |
|---|---:|---:|---:|
| PIB | 1.00 | 0.15 | -0.74 |
| Inflation | 0.15 | 1.00 | -0.15 |
| Chômage | -0.74 | -0.15 | 1.00 |

### Interprétation économique :

Le coefficient le plus marquant est la corrélation négative forte entre PIB et chômage (-0,74). Cela est cohérent avec la loi d’Okun : lorsque la croissance économique s’accélère, le marché du travail se tend généralement et le chômage baisse.

Le lien entre PIB et inflation est faible (0,15). Ce résultat comporte une logique économique claire : la hausse des prix observée sur ces dernières années est fortement influencée par des chocs externes, notamment l’augmentation mondiale des prix de l’énergie et des matières premières, ainsi que les effets de la pandémie et de la guerre en Ukraine.

La relation inflation-chômage est très faible (-0,15). Cela ne confirme pas clairement la courbe de Phillips classique sur cette période. L’explication la plus raisonnée est que le Maroc a connu un environnement économique particulier, et que le volume de données est trop limité pour conclure de manière robuste sur une relation macroéconomique stable à court terme.

---

## 6. Résultats de modélisation :

| Modèle | MAE (pts de %) | RMSE (pts de %) | R² |
|---|---:|---:|---:|
| Régression Linéaire | 1.370 | 1.545 | -2.029 |
| Random Forest | 0.736 | 0.984 | -0.229 |

### Interprétation honnête :

L’erreur la plus instructive n’est pas la plus petite, mais la plus explicable.

Voici la logique scientifique :

1. La période de test (2020-2024) est atypique.
2. Les modèles ont été entraînés sur une période plus stable, avant le choc majeur de la pandémie.
3. Le faible nombre d’années observées limite fortement la capacité de généralisation.
4. Le Random Forest est clairement meilleur que la Régression Linéaire, mais reste insuffisant sur cette période de crise.

Un R² négatif signifie que le modèle est moins performant qu’une simple moyenne constante. Ce résultat est important à exposer, car il montre que le projet ne masque pas une faiblesse méthodologique : il la décrit, la comprend et l’explique.

Pour ce type de dossier, cette honnêteté est un atout. Une candidature qui prétend “tout réussir” sans discussion des limites a moins de valeur qu’une candidature qui démontre une vraie compréhension des contraintes de la modélisation empirique.

---

## 7. Limites du projet :

Le projet est solide, mais il a des limites que le candidat doit savoir formuler avec précision :

- faible nombre d’observations annuelles ;
- période de test marquée par un choc mondial inédit ;
- utilisation d’un nombre limité de variables macroéconomiques ;
- absence de variables externes comme le prix du pétrole, le climat, les transferts des MRE ou la conjoncture régionale ;
- modèles relativement simples, choisis à des fins pédagogiques et de reproductibilité plutôt que pour une optimisation poussée.

Ces limites ne diminuent pas la qualité du projet. Au contraire, elles renforcent son sérieux, car elles montrent une posture scientifique crédible.

---

## 8. Pistes d’amélioration :

Pour aller plus loin, plusieurs améliorations seraient pertinentes :

- utiliser des données trimestrielles ou mensuelles ;
- intégrer des variables exogènes comme le prix du pétrole ou la pluviométrie ;
- tester des modèles spécialisés sur séries temporelles courtes ;
- utiliser une validation croisée temporelle ;
- séparer explicitement la période de choc Covid dans une analyse complémentaire.

---

## 9. Valeur du projet :

Ce projet constitue un bon support de candidature en Data Science / Intelligence Artificielle, lorsque le dossier met en avant la démarche scientifique et la qualité de l'interprétation, et non seulement les métriques.

- capacité à traiter des données réelles ;
- maîtrise des outils Python et Pandas ;
- autonomie dans la structuration du pipeline ;
- compréhension des séries temporelles ;
- capacité à expliquer économiquement les résultats ;
- conscience des limites du modèle et du dataset ;
- qualité de la documentation et de la démonstration reproductible.

Ce projet démontre cette logique de manière claire. Il ne s’agit pas d’un simple projet de “plotter des courbes” ; il s’agit d’un projet de data science appliquée, avec une vraie réflexion méthodologique.

---

## 10. Conclusion :

Le projet montre qu’il est possible d’analyser la dynamique économique du Maroc avec des méthodes rigoureuses, d’extraire des tendances utiles, et de confronter des modèles prédictifs simples à un problème réel. Les résultats ne sont pas parfaits, et c’est précisément ce qui donne au projet sa valeur scientifique : il montre que le candidat sait formuler des résultats honnêtes, interpréter des écarts de performance, et relier les résultats statistiques à des faits économiques concrets.

C'est précisément cette posture qui est attendue dans une candidature en Data Science ou IA : qualité de la méthode, rigueur de l’interprétation, et réflexion critique sur les limites du modèle et du dataset.

---

## 11. Technologies utilisées :

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Scikit-learn
- Jupyter Notebook


---

## 12. English Summary :

### Executive summary :

This project analyzes Morocco's macroeconomic evolution from 2000 to 2024 using three official, comparable series: GDP, inflation, and unemployment. The goal is twofold: understand the structural dynamics of the Moroccan economy, and test whether simple predictive modeling can anticipate short-term unemployment.

The pipeline follows a standard high-quality Data Science approach: collection, cleaning, exploration, visualization, feature engineering, comparative modeling, evaluation, and interpretation. The point is not merely to achieve a high score, but to demonstrate real understanding of the problem, the time series, and the dataset's limitations.

### Methodology :

Data come from the World Bank (GDP, inflation, unemployment, 2000-2024, 25 annual observations). After cleaning and merging the three series, exploratory analysis revealed a strong negative correlation between GDP and unemployment (-0.74, consistent with Okun's law), a weak GDP-inflation link (0.15, inflation mainly driven by external shocks such as the 2022 energy price spike), and a weak inflation-unemployment relationship (-0.15).

For prediction, only lagged and rolling-window features (one-year lag, 3-year rolling mean) were used as inputs — never same-year values — to avoid data leakage. Data were split chronologically (training: 2002-2019, testing: 2020-2024), never randomly, since a random split would leak future information into training.

### Results :

Two models were compared to predict unemployment: Linear Regression (MAE 1.370, RMSE 1.545, R² -2.029) and Random Forest (MAE 0.736, RMSE 0.984, R² -0.229). Both produced negative R² scores on the test set, meaning neither model outperformed a simple constant-mean baseline over 2020-2024.

This is not a failure to hide: the test period coincides with the Covid-19 shock, an event with no precedent in the 18-year training window (2002-2019). No model trained on relatively stable pre-2020 dynamics could reasonably anticipate such a discontinuity. Random Forest degraded markedly less than Linear Regression, most likely because it weighted `pib_lag1` and `pib_rolling3` heavily (75% of its decision importance), partially capturing the post-Covid GDP recovery — something the more rigid linear model could not do.

### Limitations and value for applications :

The main limitations are a small sample size (25 annual observations, 23 after feature engineering), a test period covering an unprecedented shock, and the use of only three macroeconomic indicators without external variables (oil prices, rainfall, remittances).

These limitations do not diminish the project's value — they strengthen its credibility. The project's core contribution is not a high-performing model, but the demonstrated ability to interpret a negative result with statistical and economic rigor rather than concealing it behind a flattering but misleading metric. This is precisely the posture expected in Data Science and AI application dossiers: methodological rigor, honest evaluation, and critical thinking about a model's and dataset's boundaries.
