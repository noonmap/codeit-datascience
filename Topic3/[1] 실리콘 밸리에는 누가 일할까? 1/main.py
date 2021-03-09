%matplotlib inline
import pandas as pd

df = pd.read_csv('data/silicon_valley_summary.csv')

# 코드를 작성하세요.
isManager = df['job_category'] == 'Managers'
isMale = df['gender'] == 'Male'
isNotAllRace = df['race_ethnicity'] != 'All'
racePlot = df.loc[isManager & isMale & isNotAllRace, ['race_ethnicity','count']]
racePlot.plot(kind='bar', y='count', x='race_ethnicity')