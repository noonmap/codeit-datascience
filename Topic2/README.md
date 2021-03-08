# Topic2: DataFrame 다루기
Pandas 활용 기초를 다지는 챕터입니다.
## Chapter
- DataFrame 인덱싱
- 데이터 변형하기
- 큰 데이터 다루기
## Content
```python
import pandas as pd
df = pd.read_csv("~~.csv")
```
아래의 내용들은 위 코드를 전제로 함.
### data 1개 혹은 1줄을 받아오기
- `df.loc['row', 'column']` <br> df의 [row, column]번째 데이터를 보여줌
- `df.loc['row', :]` `df.loc['row']` <br> df의 row번째 데이터를 보여줌 (row번째에 해당하는 모든 column data들을 보여줌)
- `df.loc[:, 'column']` <del>`df.loc['column']`</del> <br> df의 column번째 데이터를 보여줌 (column번째에 해당하는 모든 row data들을 보여줌) **column만 표시하고 싶을 땐, row indexing이 생략되면 error가 뜸**
- `type(df.loc[:, 'column']` &rArr; `pandas.core.series.Series` <br> Series는 Pandas의 1차원 자료형임
### data 여러 줄 받아오기
- `df.loc[['row_1', 'row_2']]` `df[['row_1', 'row_2']]` <br> row_1번째와 row_2번째 data를 받아옴
- `df['row_1' : 'row_3']` : data가 연속적으로 있을 경우, row_1부터 row_3까지 slicing 적용
- `df[['col_1', 'col_2']]` <del>`df['col_1' : 'col_3']`</del> <br> col_1번째와 col_2번째 data를 받아옴 **column에 대해 slicing을 하고 싶으면, 아래와 같은 방식으로 해야 함**
- `df.loc[:, 'col_1' : 'col_3']` <br> col_1부터 col_2까지 slicing 적용
- `df.loc['row_1' : 'row_N', 'col_1' : 'col_N']` <br> slicing 적용 &rarr; row_1\~row_N, col_1\~col_N 에 해당하는 data를 받아옴
### 조건으로 data를 인덱싱하기
- `df.loc[[True, False, True, True]]` <br> True인 값의 index(0, 2, 3번째)의 row만 가져옴 (data의 총 row 개수가 4보다 큰 경우, 생략된 부분은 default로 False로 취급함)
- `df.loc[:, [True, False, True, True]]` <br> True에 해당하는 index의 column만 가져옴
- `df.loc['col_1'] == 5` &rArr; (ex:`[True, True, False, False]`) <br> 각 row들의 `col_1번째 값 == 5`의 조건 결과를 반환함 &rarr; **조건 필터링으로 사용 가능**
- `df.loc[ df['col_1'] == 5 ]` <br> df['col_1'] == 5를 만족하는 row들을 보여줌.
- `(df.loc['col_1'] == 5) & (df.loc['col_2'] < 5)` <br> 각 row에 대해 해당 조건의 결과를 반환함
- `df.loc[ (df.loc['col_1'] == 5) & (df.loc['col_2'] < 5) ]` <br> 위의 조건을 만족하는(True인) row들을 보여줌
### 위치(Index)로 인덱싱하기
- `df.iloc[2, 4]` <br> 2번째 row, 4번째 col의 data를 보여줌
- `df.iloc[[1, 3], [1, 4]]` <br> 1,3번째 row, 1,4번째 col의 data를 보여줌 (즉 4개의 data를 보여줌)
- `df.iloc[1:3, :4]` `df[1:3, :4]` <br> slicing을 적용해서 1\~2번째 row, 0\~3번째 col의 data를 보여줌

## Pandas 실습
1. 수강신청 준비하기
2. 강의실 배정하기 1
3. 강의실 배정하기 2
