feat: adiciona script de analise de dados e plotagem de suicidios (2014-2018)

# Análise de Dados - DATASUS Suicídios no Brasil

Este módulo inicializa o carregamento e a visualização estruturada da base de dados.

- **Gerenciamento de Caminhos:** Utiliza o módulo nativo `pathlib` para mapear os diretórios do projeto de forma dinâmica, evitando falhas de navegação entre sistemas operacionais distintos (Windows/Linux/macOS).
- **Leitura do Dataset:** Realiza a abertura e decodificação do arquivo bruto em formato CSV (codificado em `ISO-8859-1`), carregando-o na memória como o DataFrame `df_preview` através do Pandas.

# Etapa de Limpeza de Dados (Data Cleaning)

Nesta etapa do projeto, realizamos o tratamento de valores ausentes (nulos) para garantir a integridade das análises demográficas posteriores.

- **Remoção Estratégica de Registros Incompletos:** Utilizamos o método `.dropna(subset=[...])` do Pandas para eliminar linhas onde informações demográficas cruciais não foram preenchidas pelos estabelecimentos de saúde.
- **Variáveis Tratadas:** A limpeza focou nas colunas de perfil do indivíduo e do óbito:
  - `SEXO` (Gênero)
  - `ESTCIV` (Estado Civil)
  - `RACACOR` (Etnia/Raça)
  - `CIRCOBITO` (Circunstância do Óbito)
  - `DTNASC` (Data de Nascimento / Idade)
  - `ESC` (Escolaridade)
  - `LOCOCOR` (Local de Ocorrência)
- **Validação do Processo:** O script encerra executando a combinação `.isnull().sum()`, garantindo e validando visualmente no console que nenhuma das colunas mapeadas possui valores nulos residuais no DataFrame final (`df_clear`).


# Análise Temporal e Visualização de Dados

Esta etapa do projeto é responsável por transformar os registros individuais do DATASUS em um indicador consolidado de evolução histórica, gerando a primeira camada de inteligência visual do projeto.

- **Mapeamento por Expressão Regular (Regex):** Como os dados brutos de mortalidade utilizam a codificação internacional CID-10, aplicamos o método `.str.count()` associado a uma regex (`r'X6[0-9]|X7[0-9]|X8[0-4]'`) na coluna `CAUSABAS`. Isso nos permitiu filtrar e contar com precisão apenas as ocorrências correspondentes a lesões autoprovocadas voluntariamente.
- **Agrupamento e Agregação:** Utilizamos a função `.groupby('ano')` combinada com a operação matemática `.sum()` para consolidar os microdados (mais de 58 mil linhas) em um resumo estatístico macro por ano.
- **Data Visualization com Matplotlib:** Desenvolvemos um gráfico de linha customizado para evidenciar a tendência dos dados ao longo do tempo. O gráfico conta com marcadores circulares (`marker='o'`), malha de fundo (`plt.grid`) para facilitar a leitura dos eixos e parametrização explícita dos rótulos temporais (`plt.xticks`), evitando distorções na linha do tempo.

## Visualização dos Resultados

Abaixo está o gráfico gerado a partir do cruzamento de dados do DATASUS, demonstrando a tendência dos casos ao longo do período analisado:

<img src="dados_panda\images\evolucao_suicidios.png" alt="Texto Alternativo" width="500">