from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / 'data' / 'processed'


def load_economic_data(file_name: str = 'donnees_economiques_maroc.csv') -> pd.DataFrame:
    """Charge le dataset Maroc nettoyé et prêt pour l'analyse."""
    path = DATA_DIR / file_name
    if not path.exists():
        raise FileNotFoundError(f'Fichier introuvable : {path}')
    df = pd.read_csv(path, index_col=0)
    df.index = pd.to_numeric(df.index, errors='coerce')
    df = df.sort_index()
    return df
