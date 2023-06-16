# Bi-Weekly Report:

## Meeting 2:

- To-Do
  - Search for literature
  - get to know your data set
  - Write import script for data set and prepare data filtering (cities, pollutants, ...)
- Tools
  - workspace needed. [In-process]
  - HTW Cloud to share the PDF.
- Analytical goals
  - 1st goal is to predict 1 hour with input data of 6 hours.
  - 2nd could be weeks.
- Preparation of the project plan.
  - May
    - Data and Project understanding.
    - literature research
  - June
    - Selection of models as per the data.
  - July
    - Selection of autoML level. (mostly 3)
  - Aug
    - Finalizing the project.
    - along with paper work
  - Sept
    - Finishing the paper work.

## Meeting 3: (06-06-2023)

### Work done:

- Understanding of the data. [(refer dataUnderstanding.ipynb)](https://github.com/YashRevannavar/Auto-ML-On-De-Pollution/blob/master/script/dataUnderstanding.ipynb)
  - knowing the data set.
    - main db.
    - cities db.
    - chemicals db.
    - merging the dbs to as per convince.
- Graphs [(refer graphs)](https://github.com/YashRevannavar/Auto-ML-On-De-Pollution/tree/master/graphs).
  - Plotting bar graph the data for each chemical in a single
    - 6 graphs = 6 chemicals as **y** and cities as **x**
  - Correlation Matrix of all columns.
- Discovering facts about data. [(refer dataUnderstanding.ipynb >> Facts about data)](https://github.com/YashRevannavar/Auto-ML-On-De-Pollution/blob/master/script/dataUnderstanding.ipynb)
  - The number of cities with Stickstoffmonoxid [nitric oxide] data available is: 61
  - The number of cities with Stickstoffdioxid [nitrogen dioxide] data available is: 61
  - The number of cities with Schwefeldioxid [sulfur dioxide] data available is: 7
  - The number of cities with PM2.5 data available is: 46
  - The number of cities with PM10 data available is: 59
  - The number of cities with Ozon data available is: 29
  - The data is available from 2019-12-31 to 2022-10-01
