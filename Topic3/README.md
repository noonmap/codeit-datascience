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
  * [line graph](#line-graph)
  * [bar graph](#bar-graph)
  * [pie graph](#pie-graph)
  * [histogram](#histogram)
  * [box plot](#box-plot)
  * [Scatter plot](#scatter-plot)
  * [Seaborn](#seaborn)
  * [KDE](#kde)
  * [카테고리 별 시각화](#카테고리-별-시각화)
  * [상관계수](#상관계수)
  * [scatter plot과 heatmap의 차이점](#scatter-plot과-heatmap의-차이점)
  * [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
  * [Cluster Analysis](#cluster-analysis)
  * [문자열 필터링](#문자열-필터링)
  * [문자열 분리](#문자열-분리)
  * [카테고리로 분류](#카테고리로-분류)
  * [groupby](#groupby)
  * [dataset merge](#dataset-merge)
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
### Seaborn
(Statistical Data Visualization) 통계를 기반으로 한 데이터 시각화를 도와주는 라이브러리

- PDF (Probability Density Function) : 확률 밀도 함수
	- 데이터 셋의 값들이 어떻게 분포되어있는지 보여주는 함수
	- 특정 구간의 확률은 그래프 아래 그 구간의 면적과 동일하다
	- 그래프 아래의 모든 면적의 합은 1이다
	- 연속적인 값일 경우, 특정 값의 확률을 찾는 건 무의미함. 특정 구간의 확률을 찾는 것이 유의미한 통계 결과임

### KDE
- KDE (Kernel Density Estimation)
	- 실제 데이터로 통계함수를 그리면 이상한 굴곡이 많음 
	- KDE를 쓰면 이 데이터를 기반으로 추측으로 진짜 분포에 가까운 (부드러운 곡선인) 함수를 그릴 수 있다
```python
import pandas as pd
import seaborn as sns
df = pd.read_csv('~.csv')
```
아래는 위의 코드를 전제로 정리한 내용이다.

- `sns.kdeplot( df['col'], bw=0.5)`
	- KDE를 사용한 부드러운 곡선 그래프를 그려줌
	- `bw`: 몇 구간으로 나눠줄지 결정
- `sns.distplot( df, bins=15 )`
	- `df.plot(kind='hist', y='Height', bins=15)`  와 비교해보기
	- `displot` : histogram 위에 kdeplot을 그려줌
- `sns.violinplot(y=df["Height"])`
	- `df.plot(kinds='box', y='Height')` 와 비교해보기
	- `violinplot` : box plot는 분포의 요약본인 것인 반면, 이건 데이터 전체의 분포를 그려줌. kde 그래프가 양쪽으로 그려진 모습
- `sns.kdeplot( df['Height'], df['Weight'])`
	- `df.plot(kind='scatter', x='Height', y='Weight')` 와 비교해보기
	- x축과 y축의 분포를 3차원으로 그림. 등고선처럼 그래프를 위에서 본 시점으로 나타남
- `sns.lmplot(data=df, x='Height', y='Weight')`
	- data에 대한 산점도를 그리고, 그 위에 regression line을 그려줌

### 카테고리 별 시각화

x축의 각 종류(=`df['col1'].unique()`)에 따른 그래프를 그려줌

- `sns.catplot(data=df, x='col1', y=col2', kind='box')`
	- 각 카테고리에 따른 데이터를 box plot으로 그려줌

![box](https://user-images.githubusercontent.com/36250213/111742106-ea439100-88ca-11eb-95af-70f19c24261f.png)
- `sns.catplot(data=df, x='col1', y=col2', kind='violin')`
	- 각 카테고리에 따른 데이터를 violin graph로 그려줌

![violin](https://user-images.githubusercontent.com/36250213/111742134-f29bcc00-88ca-11eb-84ba-34cde4b3781f.png)
- `sns.catplot(data=df, x='col1', y=col2', kind='strip')`
	- 각 카테고리에 따른 데이터를 한번에 볼 수 있음

![strip](https://user-images.githubusercontent.com/36250213/111742147-f891ad00-88ca-11eb-95f0-8734f963a0d9.png)
- `sns.catplot(data=df, x='col1', y=col2', kind='strip', hue='col3')`
	- `hue` : col3의 각 카테고리에 따라 데이터의 색을 다르게 칠해줌
![strip_hue](https://user-images.githubusercontent.com/36250213/111741903-9638ac80-88ca-11eb-9dde-ae6577ed94b9.png)
- `sns.catplot(data=df, x='col1', y=col2', kind='swarm', hue='col3')`
	- `kind=swarm` : `strip` 처럼 데이터를 모두 보여주는데, 분포를 더 잘 알 수 있도록 펼쳐서 보여줌
![swarm_hue](https://user-images.githubusercontent.com/36250213/111741920-9b95f700-88ca-11eb-9650-3b33c59af213.png)

### 상관계수
- 상관계수(Correlation Coefficient) : 두 변수의 연관성을 수치적으로 표현
- Pearson 상관계수
	- 0에 가까울수록 연관성이 없음
	- 1에 가까울수록 연관성이 있음
	- -1에 가까울수록 반대의 관계를 가짐
- `df.corr()`
<br> 숫자 데이터 사이의 상관 계수를 DataFrame 형태로 출력함
- `sns.heatmap( df.corr() )`
<img src="https://i.imgur.com/HE0ISzz.png" style="max-width: 50%; display: block; margin: 0 auto;">
	- heatmap : 상관 계수를 시각화하는 대표적인 방법. 
	- 색이 밝을수록 상관 계수가 더 높음. &rarr; $y ~= x$
	- 색이 진할수록 연관이 없거나, 반대되는 연관성을 가짐. &rarr; $y ~= -x$
- `sns.heatmap( df.corr(), annot=True )`
<br> `annot` : 색상 뿐만 아니라 숫자도 함께 보여줌
<p><img src="https://i.imgur.com/Tz5JpZs.png" style="max-width: 50%; display: block; margin: 0 auto;"></p>

### scatter plot과 heatmap의 차이점
scatter plot은 데이터가 한 곳에 모여있을 때 파악하기가 어려움.
반면 heatmap은 한 곳에 1000개의 점이 모여있으면, 그 밀집도가 색깔로 구분됨. 대신, 각 데이터가 정확히 어떤 값을 갖는지는 파악이 어렵다.
정리하자면 scatter plot은 얼마나 분산되어 있는지 보기에 좋고, heatmap은 얼마나 밀집되어 있는지 보기에 좋다.

### Exploratory Data Analysis (EDA)
탐색적으로 데이터를 분석하는 것. 
&rarr; 데이터셋을 다양한 관점에서 살펴보고 탐색하면서 인사이트를 도출해내는 것.

- `sns.jointplot(data=df, x='Height', y='Weight')`
<br> 키와 몸무게 분포에 대한 scatter plot과 histogram이 함께 나타남

### Cluster Analysis
- cluster : 무리로 나누는 것
- `sns.clustermap( df.corr() )`
<br> 연관성이 있는 관심사끼리 묶어서 보여줌
<p><img src="https://i.imgur.com/gRuu4zn.png"></p>

### 문자열 필터링
- `df['Genre'].str.contains('Blues')`
<br> 'Genre' column에서 'Blues' 라는 문자열이 포함된 record들을 찾음
- `df['Genre'].str.startswith('Blues')`
<br> 'Genre' column에서 'Blues' 라는 문자열로 시작하는 record들을 찾음

### 문자열 분리
- `df['col'].str.split()` `df['col'].str.split(pat=' ')`
<br> 띄어쓰기를 기준으로 문자열을 분리해서 lsit로 만듦
- `df['col'].str.split(pat='-', n=1, expand=True)`
	- `pat='-'` : '-'를 기준으로 문자열을 분리함
	- `n=1` : 첫번째 띄어쓰기에서만 문자열을 분리함 (2개로 나뉨)
	- `expand=True` : 분리된 문자열을 새로운 DataFrame으로 만듦 

### 카테고리로 분류
- `df['col'].map( new_dict )`
	- `new_dict` : { `df['col']`의 종류 : 새로 대체할 값 }
	- `df['col']`의 종류 중, new_dict의 key에 포함된 이름이면 value에 있는 값으로 변경해줌

### groupby
- `col_group = df.groupby('col')`
<br> col의 카테고리별로 묶어줌. 아래의 함수를 사용하면, 각 카테고리에 대한 다른 column들의 특정 값, 그래프를 볼 수 있다.
	- `col_group.count()` 횟수
	- `col_group.max()` 최댓값
	- `col_group.mean()` 평균
	- `col_group.first()` 처음 값
	- `col_group.last()` 마지막 값
	- `col_group.plot()` 각 카테고리 별 값 형성을 그래프로 그려줌

### dataset merge
- Inner Join : 두 데이터의 **겹치는 index**에 대해서만 합침
	- `pd.merge(df_a, df_b, on='겹치는 column')`
- Left Outer Join : 왼쪽 데이터를 기준으로 함 &rarr; 왼쪽 데이터에 존재하는 index에 대해 합침 (오른쪽에 없는 index이면 NaN을 넣음)
	- `pd.merge(df_a, df_b, on='겹치는 column', how='left')`
- Right Outer Join: 오른쪽 데이터를 기준으로 함 &rarr; 오른쪽 데이터에 존재하는 index에 대해 합침 (왼쪽에 없으면 NaN을 넣음)
	- `pd.merge(df_a, df_b, on='겹치는 column', how='right')`
- Full Outer Join: 양쪽 모두에 존재하는 index에 대해 합침 (없는 곳은 NaN을 넣음)
	- `pd.merge(df_a, df_b, on='겹치는 column', how='outer')`
