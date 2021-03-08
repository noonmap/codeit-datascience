import pandas as pd

df = pd.read_csv('data/enrolment_1.csv')

# 코드를 작성하세요.
condition1 = (df['course name'] == 'information technology') & (df['year'] == 1)

condition2 = (df['course name'] == 'commerce') & (df['year'] == 4)

condition3 = df['course name'].value_counts() <= 5
condition3 = condition3[ condition3 ].index
# 정답 출력
df['status'] = 'allowed'
df['status'][condition1 | condition2] = 'not allowed'

for i in range(df.shape[0]):
    if df['course name'].iloc[i] in condition3:
        df['status'].iloc[i] = 'not allowed'

# execute in jupyter notebook
df
