%matplotlib inline
import pandas as pd

df = pd.read_csv('data/silicon_valley_details.csv')

# 코드를 작성하세요.

jobCategoryList = list (df['job_category'].unique() )[:-2]
jobCount = pd.DataFrame(jobCategoryList, columns=['job'])
jobCount.set_index('job', inplace=True)
jobCount['count'] = 0

for job_name in jobCategoryList:
    isJobEqual = df['job_category'] == job_name
    isAdobe = df['company'] == 'Adobe'
    jobCount.loc[job_name, 'count'] = df.loc[isJobEqual & isAdobe, 'count'].sum()
    if jobCount.loc[job_name, 'count'] == 0:
        jobCount.drop(job_name, inplace=True)

# jobCount['count'].plot(kind='pie', y='count') 를 하면
# jobCount['count']라는 Series 타입에 대한 그래프가 그려지기 때문에
# 'job'(index)에 대한 legend가 나타나지 않는다.
jobCount.plot(kind='pie', y='count')