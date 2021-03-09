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
  - 'col'에 대한 histogram이 그려짐 (막대의 default 개수는 10개)
  - **인자는 `y='col'`이지만, 'col'에 대한 값들은 x축에 나타남**
  - `bins=10` : histogram의 막대의 개수를 나타냄
### box plot
- `df.plot(kind='box', y='col')` `df['col'].plot(kind='box')`
<br> 'col'인 column에 대한 통계값을 box plot을 통해 볼 수 있음
- `df.plot(kind='box', y=['col1', 'col2', 'col3'])`
<br> 'col1','col2','col3'인 여러 column에 대한 통계값을 한번에 볼 수 있음
### Scatter plot
산점도(Scatter plot)는 두 데이터 간의 관계를 확인하기 쉬운 그래프 유형이다.
- `df.plot(kind='scatter', x='col1', y='col2')`
<br> x축='col1', y축='col2'인 scatter graph를 그려줌
