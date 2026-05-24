import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
caminho_csv = BASE_DIR / 'data' / 'datasus_suicidio_2014_2018.csv'

df_preview = pd.read_csv(caminho_csv, encoding='ISO-8859-1', delimiter=',')

print(df_preview)