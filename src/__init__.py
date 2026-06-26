import pandas as pd
from pathlib import Path

diretorio_atual = Path(__file__).parent.parent
caminho_csv = diretorio_atual / 'data' / 'datasus_suicidio_2014_2018.csv'

df_preview = pd.read_csv(caminho_csv, encoding='ISO-8859-1', delimiter=',')

print(df_preview)