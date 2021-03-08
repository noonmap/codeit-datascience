# Topic2: DataFrame 다루기
Pandas 활용 기초를 다지는 챕터입니다.
## Chapter
- DataFrame 인덱싱
- 데이터 변형하기
- 큰 데이터 다루기
## Pandas 실습
1. 수강신청 준비하기 (조건 인덱싱)
2. 강의실 배정하기 1 (조건 인덱싱, 값의 수정 및 추가)
3. 강의실 배정하기 2 (조건 인덱싱, 값의 수정 및 추가)
## Content
```python
import pandas as pd
df = pd.read_csv("~~.csv")
```
아래의 내용들은 위 코드를 전제로 함.
+ [data 1개 혹은 1줄을 받아오기](#data-1개-혹은-1줄을-받아오기)
+ [data 여러 줄 받아오기](#data-여러-줄-받아오기)
+ [조건으로 data를 인덱싱하기](#조건으로-data를-인덱싱하기)
+ [위치(Index)로 인덱싱하기](#위치index로-인덱싱하기)
+ [data 1개 혹은 1줄의 값 쓰기](#data-1개-혹은-1줄의-값-쓰기)
+ [data 여러 줄의 값 쓰기](#data-여러-줄의-값-쓰기)
+ [data 값 추가 및 삭제](#data-값-추가-및-삭제)
+ [index/column 설정하기](#indexcolumn-설정하기)
+ [큰 DataFrame 살펴보기](#큰-dataframe-살펴보기)
+ [큰 Series 살펴보기](#큰-series-살펴보기)

### data 1개 혹은 1줄을 받아오기
- `df.loc['row', 'col']` <br> df의 row=='row', col=='col'인 데이터를 보여줌
- `df.loc['row', :]` `df.loc['row']` <br> df의 row=='row'인 데이터를 보여줌 (row=='row'에 해당하는 모든 column data들을 보여줌)
- `df.loc[:, 'column']` <del>`df.loc['column']`</del> <br> col='col'인 데이터들을 보여줌 **column만 표시하고 싶을 땐, row indexing이 생략되면 error가 뜸**
- `type(df.loc[:, 'column']` &rArr; `pandas.core.series.Series` <br> Series는 Pandas의 1차원 자료형임
### data 여러 줄 받아오기
- `df.loc[['row_1', 'row_2']]` `df[['row_1', 'row_2']]` <br> row=='row1', row=='row2'인 data를 받아옴
- `df['row_1' : 'row_3']` : data가 연속적으로 있을 경우, row_1부터 row_3까지 slicing 적용
- `df[['col_1', 'col_2']]` <br> col=='col1', col=='col_2'인 data를 받아옴 
- `df.loc[:, 'col_1' : 'col_3']` <del>`df['col_1' : 'col_3']`</del> <br> col_1부터 col_2까지 slicing 적용 **column에 대해 slicing을 할 때 주의**
- `df.loc['row_1' : 'row_N', 'col_1' : 'col_N']` <br> row_1\~row_N, col_1\~col_N 에 해당하는 data를 받아옴
### 조건으로 data를 인덱싱하기
- `df.loc[[True, False, True, True]]` <br> True인 index(0, 2, 3번째)의 row만 가져옴 (data의 총 row 개수가 4보다 큰 경우, 생략된 부분은 default로 False로 취급함)
- `df.loc[:, [True, False, True, True]]` <br> True인 index의 column만 가져옴
- `df.loc['col_1'] == 5` &rArr; (ex:`[True, True, False, False]`) <br> 각 row들의 `'col_1'의 data의 값 == 5`의 조건 결과를 반환함 &rarr; **조건 필터링으로 사용 가능**
- `df.loc[ df['col_1'] == 5 ]` <br> `df['col_1'] == 5`를 만족하는 row들을 보여줌.
- `(df.loc['col_1'] == 5) & (df.loc['col_2'] < 5)` <br> 각 row에 대해 해당 조건의 결과를 반환함
- `df.loc[ (df.loc['col_1'] == 5) & (df.loc['col_2'] < 5) ]` <br> 위의 조건을 만족하는(True인) row들을 보여줌
### 위치(Index)로 인덱싱하기
- `df.iloc[2, 4]` <br> 2번째 row, 4번째 col의 data를 보여줌
- `df.iloc[[1, 3], [1, 4]]` <br> 1,3번째 row, 1,4번째 col의 data를 보여줌 (즉 4개의 data를 보여줌)
- `df.iloc[1:3, :4]` `df[1:3, :4]` <br> slicing을 적용해서 1\~2번째 row, 0\~3번째 col의 data를 보여줌
### data 1개 혹은 1줄의 값 쓰기
- `df.loc['row', 'col'] = 2`
<br>row=='row', col='col'인 data의 값을 2로 기입
- `df.loc['row'] = [A, B, C]`
<br>row=='row'인 data의 값을 [A, B, C]로 기입 (단, A, B, C는 각 column의 type에 맞춰줘야 함)
- `df['col'] = [A1, A2, A3]`
<br>0,1,2번째 row에 대해, col='col'의 data의 값이 [A1, A2, A3]로 바뀜 (단, 모두 col의 type에 맞춰야 함)
- `df['col'] = A`
<br>col=='col'인 data의 값이 모두 A로 바뀜
### data 여러 줄의 값 쓰기
- `df[['col_1', 'col_2']] = A` `df[['col_1' : 'col_3']] = A`
<br>col=='col_1', col=='col_2'인 data의 값이 A로 바뀜
- `df.loc[df['col'] > 5] = A`
<br> df['col'] > 5를 만족하는 row의 값을 모두 A로 바꿈
- `df.iloc[[1, 3], [2, 4]] = A`
<br> 1,3번째 row, 2,4번째 col의 값을 모두 A로 바꿈
### data 값 추가 및 삭제
- `df.loc['new_row'] = A`
<br> 'new_row'라는 새로운 row가 추가되며, 값이 A로 설정됨
- `df['new_col'] = A`
<br> 'new_col'라는 새로운 col이 추가되며, 값이 A로 설정됨
- `df.drop('del_row', axis='index', inplace=True)`
  - `axis='index'`는 row를 삭제하고 싶다는 의미
  - `inplace=True`를 적용해줘야 DataFrame에 반영됨 (False인 경우, 새로운 DataFrame을 만들어서 반환함)
  - row=='del_row'인 row를 삭제한다
- `df.drop('del_col', axis='columns', inplace=True)`
  - `axis='columns'`는 column을 삭제하고 싶다는 의미
  - `inplace=True`를 적용해줘야 DataFrame에 반영됨 (False인 경우, 새로운 DataFrame을 만들어서 반환함)
  - col=='del_col'인 column을 삭제한다
- `df.drop(['del_row1','del_row2','del_row3'], axis='index', inplace=True)`
  - `axis='index'`는 row를 삭제하고 싶다는 의미
  - `inplace=True`를 적용해줘야 DataFrame에 반영됨 (False인 경우, 새로운 DataFrame을 만들어서 반환함)
  - row=='del_row1','del_row2','del_row3'인 row들을 삭제한다
### index/column 설정하기
- `df.rename(columns={'bef_col' : 'aft_col'}, inplace=True)`
  - `inplace=True`를 적용해줘야 DataFrame에 반영됨 (False인 경우, 새로운 DataFrame을 만들어서 반환함)
  - col=='bef_col'인 columns의 이름을 'aft_col'으로 바꾼다.
- `df.index.name = 'AAA'`
<br> index의 이름을 'AAA'라고 설정
- `df['origin_index'] = df.index` &rarr; `df.set_index('other_col', inplace=True)`
  - `inplace=True`를 적용해줘야 DataFrame에 반영됨 (False인 경우, 새로운 DataFrame을 만들어서 반환함)
  - index를 다른 column으로 바꿈
    - `df['origin_index'] = df.index` &rarr; 기존 index를 df에 새로운 column으로 추가함 (이 단계가 없이 set_index를 수행하면 기존 index column이 사라짐)
    - `df.set_index('other_col', inplace=True)` &rarr; col='other_col'인 column을 index로 설정함.
- **index는 겹치는 값이 없는 unique한 column으로 설정하는 것이 좋음**
### 큰 DataFrame 살펴보기
- `df.head(7)`
<br> 상위 7개의 row를 출력
- `df.tail(7)`
<br> 마지막 7개의 row를 출력
- `df.shape`
<br> df의 차원 정보를 알려줌 (row, column의 개수)
- `df.columns`
<br> 모든 column의 이름을 list로 반환
- `df.info()`
<br> 모든 column들의 정보(column 이름, data의 개수, 설정, 타입)를 보여줌
- `df.describe()`
<br> 각 column에 해당하는 data들의 통계값을 정리해서 보여줌
- `df.sort_values(by='col', ascending=True, inplace=True)`
  - 'col'인 column에 대해서 data들을 정렬
  - `ascending=True` &rarr; 오름차순 정렬 설정
  - `inplace=True` &rarr; 정렬 결과를 df에 반영 (False이면 새로운 DataFrame을 만들어서 반환)
### 큰 Series 살펴보기
- `df['col'].unique()`
<br> col=='col'인 column Series에서, data값의 종류를 리스트로 반환
- `df['col'].value_count()`
<br> col=='col'인 column Series에서, 각 data 종류들의 개수를 보여줌
- `df['col'].describe()`
<br> col=='col'인 column Series의 요약 정보(총 data개수, unique개수, 가장 많은 data의 종류, 가장 많은 data의 개수)를 알려줌
