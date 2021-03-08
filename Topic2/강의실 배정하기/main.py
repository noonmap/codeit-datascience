import pandas as pd

df = pd.read_csv('data/enrolment_2.csv')

# 코드를 작성하세요.
stud_counts = df['course name'].value_counts()
cond2_1 = list( stud_counts[stud_counts >= 80].index )
cond2_2 = list( stud_counts[ (80 > stud_counts) & (stud_counts >= 40)].index )
cond2_3 = list( stud_counts[(40 > stud_counts) & (stud_counts>= 15)].index )
cond2_4 = list( stud_counts[(15 > stud_counts) & (stud_counts>= 5)].index )
df['room assignment'] = 'not assigned'
for i in cond2_1:
    df.loc[ df['course name'] == i, 'room assignment'] = 'Auditorium'
for i in cond2_2:
    df.loc[ df['course name'] == i, 'room assignment'] = 'Large room'
for i in cond2_3:
    df.loc[ df['course name'] == i, 'room assignment'] = 'Medium room'
for i in cond2_4:
    df.loc[ df['course name'] == i, 'room assignment'] = 'Small room'
df.loc[df['status'] == 'not allowed', 'room assignment'] = 'not assigned'

# execute in jupyter notebook
df
