import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


df = pd.read_csv('data/processed/donnees_economiques_maroc.csv', index_col=0)
print('Shape:', df.shape)
print(df.head())

# Feature engineering

df['pib_lag1'] = df['pib'].shift(1)
df['inflation_lag1'] = df['inflation_pct'].shift(1)
df['chomage_lag1'] = df['chomage_pct'].shift(1)
df['pib_rolling3'] = df['pib'].rolling(window=3).mean()
df['inflation_rolling3'] = df['inflation_pct'].rolling(window=3).mean()
df['pib_pct_change'] = df['pib'].pct_change()

# Drop invalid rows created by lag/rolling

df_features = df.dropna().copy()
print('Shape after feature engineering:', df_features.shape)

features = ['pib_lag1', 'inflation_lag1', 'chomage_lag1', 'pib_rolling3', 'inflation_rolling3']
X = df_features[features]
y = df_features['chomage_pct']

split_index = len(X) - 5
X_train, X_test = X.iloc[:split_index], X.iloc[split_index:]
y_train, y_test = y.iloc[:split_index], y.iloc[split_index:]

model_lr = LinearRegression()
model_lr.fit(X_train, y_train)
pred_lr = model_lr.predict(X_test)

model_rf = RandomForestRegressor(n_estimators=100, max_depth=4, random_state=42)
model_rf.fit(X_train, y_train)
pred_rf = model_rf.predict(X_test)

print('LR metrics:')
print('MAE=', mean_absolute_error(y_test, pred_lr))
print('RMSE=', np.sqrt(mean_squared_error(y_test, pred_lr)))
print('R2=', r2_score(y_test, pred_lr))

print('RF metrics:')
print('MAE=', mean_absolute_error(y_test, pred_rf))
print('RMSE=', np.sqrt(mean_squared_error(y_test, pred_rf)))
print('R2=', r2_score(y_test, pred_rf))

print('Corr PIB-Chomage =', df[['pib', 'inflation_pct', 'chomage_pct']].corr().iloc[0, 2])
print('Feature importances RF:')
print(pd.Series(model_rf.feature_importances_, index=features).sort_values(ascending=False))
