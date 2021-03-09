# Topic3: 데이터 분석과 시각화
## Chapter
1. 시각화와 그래프
2. Seaborn 시각화
3. 통계 기본 상식
4. Exploratory Data Analysis
5. 새로운 인사이트 발견하기
## 실습 문제
1. 실리콘 밸리에는 누가 일할까? 1 (막대 그래프)
2. 실리콘 밸리에는 누가 일할까? 2 (파이 그래프)
3. 스타벅스 음료의 칼로리는? 1    (히스토그램)
## Contents
```python
import pandas as pd
df = pd.read_csv("~.csv")
```
아래의 정리는 위의 코드를 전제한 내용임
### line graph
- `%matplotlib inline` 
<br> Jupyter 노트북에서 matplotlib를 사용하기 위해 이 문구를 설정해줘야 함
- `df.plot()` `df.ploy(kind='line')`
  - df라는 dataframe에 대한 line graph를 그림 (default: line)
  - kind로 graph 형식을 정해줄 수 있음.
- `df.plot(y='KBS')` 
<br> 'KBS'에 대한 line graph만 그려줌
- `df.plot(y=['KBS', 'JTBC'])` `df[:, ['KBS', 'JTBC']].plot()`
<br> 'KBS'와 'JTBC'에 대한 line graph만 그려줌
### bar graph
- `df.plot(kind='bar')`
<br> df라는 dataframe에 대한 bar graph가 그려짐
- `df.plot(kind='barh')`
<br> 가로로 눕혀진 bar graph가 그려짐
- `df.plot(kind='bar', stacked=True)`
<br> 쌓여진 bar graph가 나타남
### pie graph
- `df.loc['row'].plot(kind='pie')`
<br> df의 row=='row'인 Series에 대해 pie graph가 그려짐
### histogram
- `df.plot(kind='hist', y='col')` `df.plot(kind='hist', y='col', bins=10)`
  - x축='col'인 histogram이 그려짐 (막대의 default 개수는 10개)
  - `bins=10` : histogram의 막대의 개수를 나타냄
