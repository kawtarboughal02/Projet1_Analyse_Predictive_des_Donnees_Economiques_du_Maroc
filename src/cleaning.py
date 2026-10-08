import pandas as pd


def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    """Ajoute les variables dérivées utiles à la prédiction du chômage."""
    df = df.copy()
    df['pib_lag1'] = df['pib'].shift(1)
    df['inflation_lag1'] = df['inflation_pct'].shift(1)
    df['chomage_lag1'] = df['chomage_pct'].shift(1)
    df['pib_rolling3'] = df['pib'].rolling(window=3).mean()
    df['inflation_rolling3'] = df['inflation_pct'].rolling(window=3).mean()
    df['pib_pct_change'] = df['pib'].pct_change()
    return df.dropna().copy()


def split_chronological(df: pd.DataFrame, target_col: str = 'chomage_pct', test_years: int = 5):
    """Découpe chronologiquement les données en train/test sans mélange aléatoire."""
    features = [col for col in df.columns if col != target_col]
    X = df[features]
    y = df[target_col]
    split_index = len(X) - test_years
    X_train, X_test = X.iloc[:split_index], X.iloc[split_index:]
    y_train, y_test = y.iloc[:split_index], y.iloc[split_index:]
    return X_train, X_test, y_train, y_test
