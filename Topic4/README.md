# Topic4: 데이터 퀄리티 높이기
## Chapter
1. 좋은 데이터의 기준
2. 데이터 클리닝
## Contents
```python
import pandas as pd
df = pd.read_csv("~.csv")
```
아래의 내용은 위의 코드를 전제한 내용임
### Table of Contents
- [좋은 데이터의 기준](#좋은-데이터의-기준)
- [완결성: 결측값(NaN) 다루기](#완결성-결측값nan-다루기)
- [유일성: 중복값 다루기](#유일성-중복값-다루기)
- [정확성: 이상점(Outlier) 다루기](#정확성-이상점outlier-다루기)

### 좋은 데이터의 기준
- 완결성 (Completeness)
	- 필수적인 데이터는 모두 작성되어있어야 함
	- 완결성을 확인할 수 있는 방법 &rarr; 결측값을 체크하기
	- 결측값(NaN): 채워져야 하는데 비어있는 값
- 유일성 (Uniqueness)
	- 동일한 데이터가 불필요하게 중복되면 안됨 
- 통일성 (Conformity)
	- 데이터가 동일한 형식으로 저장되어야 함
- 정확성 (Accuracy)
	- 데이터가 정확해야 함

### 완결성: 결측값(NaN) 다루기
- `df.isnull()`
<br> df 전체를 boolean DataFrame으로 변환 &rarr; NaN가 있는 위치를 True로 나타냄
- `df.isnull().sum()`
<br> 각 column의 NaN 개수를 알려줌
- `df.dropna(inplace=True)` `df.dropna(axis='index')`
<br> NaN가 있는 record들을 제거
- `df.dropna(axis='columns', inplace=True)`
<br> NaN가 있는 column들을 제거
- `df['특정 column'].dropna(inplace=True)`
<br> 특정 column에서 NaN가 있는 record들을 없앰
- `df.fillna(0, inplace=True)`
<br> NaN를 0으로 대체함
- `df.fillna( df.mean(), inplace=True )` 
<br> NaN를 평균값으로 대체함

### 유일성: 중복값 다루기
- `df.drop_duplicates( inplace=True )`
<br> 모든 값이 중복된 record들을 제거
- `df.T`
<br> df를 Transpose함 (row와 column을 바꿈)
- `df = df.T.drop_duplicates().T`
<br> 모든 값이 중복된 column들을 제거 (`inplace` 없음)

### 정확성: 이상점(Outlier) 다루기
- 이상점(outlier) : 너무 동떨어져 있는 값
- Pandas box plot에서 outlier 판단하는 방식

- `df['특정 col'].quantile(0.25)`
<br> 특정 column의 25% 지점의 값을 알 수 있음
- `df['특정 col'].quantile(0.75)`
<br> 특정 column의 75% 지점의 값을 알 수 있음
- `iqr = df['특정 col'].quantile(0.75) - df['특정 col'].quantile(0.25)`
<br> IQR 범위 계산
- 이상점 제거 Example
```python
q3 = df['budget'].quantile(0.75) # 75% 지점
q1 = df['budget'].quantile(0.25) # 25% 지점
iqr = q3 - q1					 # IQR 계산

# Outlier 기준 설정: IQR 5배보다 더 큰 값
condition = (df['budget'] > q3 + 5 * iqr)	

# Outlier를 가진 record들을 제거
df.drop(df.loc[condition].index, axis='index',inplace=True)
```
