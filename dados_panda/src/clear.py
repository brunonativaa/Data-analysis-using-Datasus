import pandas as pd
from pathlib import Path

diretorio_atual = Path(__file__).parent.parent
caminho_csv = diretorio_atual / 'data' / 'datasus_suicidio_2014_2018.csv'

df = pd.read_csv(caminho_csv, encoding='ISO-8859-1', delimiter=',')

colunas_para_limpar = [
    'SEXO',
    'ESTCIV',
    'RACACOR',
    'CIRCOBITO',
    'DTNASC',
    'ESC',
    'LOCOCOR'
    ]

df_clear = df.dropna(subset=colunas_para_limpar) # limpando alguns valores nullos das colunas

print(df_clear.isnull().sum()) # Verifica se restam valores ausentes. No caso sim pois não limpei todas as colunas

