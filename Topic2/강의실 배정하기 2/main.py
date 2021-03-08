import pandas as pd

df = pd.read_csv('data/enrolment_3.csv')

# 코드를 작성하세요.
allowed = df['status']=='allowed'

audit = df.loc[df['room assignment'] == 'Auditorium']
large = df.loc[df['room assignment'] == 'Large room']
mediu = df.loc[df['room assignment'] == 'Medium room']
small = df.loc[df['room assignment'] == 'Small room']

audit.sort_values(by='course name', ascending=True, inplace=True)
uniq = list(audit['course name'].unique())
for idx, i in enumerate(uniq):
    df.loc[ (df['course name'] == i) & allowed, 'room assignment'] = 'Auditorium-' + str(idx+1)

large.sort_values(by='course name', ascending=True, inplace=True)
uniq = list(large['course name'].unique())
for idx, i in enumerate(uniq):
    df.loc[ (df['course name'] == i) & allowed, 'room assignment'] = 'Large-' + str(idx+1)

mediu.sort_values(by='course name', ascending=True, inplace=True)
uniq = list(mediu['course name'].unique())
for idx, i in enumerate(uniq):
    df.loc[ (df['course name'] == i) & allowed, 'room assignment'] = 'Medium-' + str(idx+1)

small.sort_values(by='course name', ascending=True, inplace=True)
uniq = list(small['course name'].unique())
for idx, i in enumerate(uniq):
    df.loc[ (df['course name'] == i) & allowed, 'room assignment'] = 'Small-' + str(idx+1)

df.rename(columns={'room assignment' : 'room number'}, inplace=True)

# execute in jupyter notebook
df
