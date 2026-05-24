from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
caminho_csv = BASE_DIR / 'data' / 'datasus_suicidio_2014_2018.csv'




df = pd.read_csv(caminho_csv, encoding='ISO-8859-1')

df['total_suicidios'] = df['CAUSABAS'].str.count(
    r'X6[0-9]|X7[0-9]|X8[0-4]'
    )


casos_por_ano =  df.groupby('ano')['total_suicidios'].sum().reset_index()



plt.figure(figsize=(10,6))
plt.plot(
    casos_por_ano['ano'], 
    casos_por_ano['total_suicidios'], 
    marker='o', 
    color='red',
    linestyle='-')

plt.title(
    'Evolução dos Casos de Suicídios no Brasil (2014 - 2018)' ,
      fontsize=14,
        fontweight='bold',
        )

plt.xlabel('Ano', fontsize=12)
plt.ylabel("Quantidade Total de Casos", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)

plt.xticks(casos_por_ano['ano'])

plt.show()

