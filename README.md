feat: script for analyzing data and plotting suicide rates (2014-2018)

# Data Analysis - DATASUS Suicides in Brazil

This module initiates the loading and structured visualization of the database.

- **Path Management:** Uses the native `pathlib` module to dynamically map project directories, preventing navigation errors across different operating systems (Windows/Linux/macOS).
- **Reading the Dataset:** Opens and decodes the raw CSV file (encoded in `ISO-8859-1`), loading it into memory as the `df_preview` DataFrame using Pandas.

# Data Cleaning Stage

In this stage of the project, we handled missing (null) values to ensure the integrity of subsequent demographic analyses.

- **Strategic Removal of Incomplete Records:** We used Pandas’ `.dropna(subset=[...])` method to eliminate rows where crucial demographic information was not provided by healthcare facilities.
- **Variables Processed:** The cleaning focused on the columns related to the individual’s profile and the death:
  - `SEXO` (Gender)
  - `ESTCIV` (Marital Status)
  - `RACACOR` (Ethnicity/Race)
  - `CIRCOBITO` (Circumstances of Death)
  - `DTNASC` (Date of Birth / Age)
  - `ESC` (Education Level)
  - `LOCOCOR` (Place of Occurrence)
- **Process Validation:** The script concludes by executing the `.isnull().sum()` combination, ensuring and visually validating in the console that none of the mapped columns contain residual null values in the final DataFrame (`df_clear`).

# Temporal Analysis and Data Visualization

This phase of the project is responsible for transforming individual DATASUS records into a consolidated indicator of historical trends, generating the project’s first layer of visual intelligence.

- **Regular Expression (Regex) Mapping:** Since the raw mortality data uses the international ICD-10 coding system, we applied the `.str.count()` method combined with a regex (`r'X6[0-9]|X7[0-9]|X8[0-4]'`) to the `CAUSABAS` column. This allowed us to accurately filter and count only the cases corresponding to intentional self-inflicted injuries.
- **Grouping and Aggregation:** We used the `.groupby(‘year’)` function combined with the `.sum()` mathematical operation to consolidate the microdata (over 58,000 rows) into a macro statistical summary by year.
- **Data Visualization with Matplotlib:** We developed a custom line chart to highlight the trend in the data over time. The chart features circular markers (`marker=‘o’`), a grid background (`plt.grid`) to make the axes easier to read, and explicit parameterization of the time labels (`plt.xticks`), preventing distortions in the timeline.

## Visualization of Results

Below is the graph generated from the cross-tabulation of DATASUS data, showing the trend in cases over the analyzed period:

![Imagem do grafico](dados_panda\images\my_grafic_datasus.png)
