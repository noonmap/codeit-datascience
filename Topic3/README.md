# Topic3: 데이터 분석과 시각화
## Chapter
1. 시각화와 그래프
2. Seaborn 시각화
3. 통계 기본 상식
4. Exploratory Data Analysis
5. 새로운 인사이트 발견하기
## Contents
### line graph
- `%matplotlib inline` : Jupyter 노트북에서 matplotlib를 사용하기 위해 이 문구를를 설정해줘야 함
- `df.plot()` : df라는 dataframe에 대한 graph를 그림 (default: line)
- `df.ploy(kind='line')` : (위와 같음) kind로 graph 형식을 정해줄 수 있음.
- `df.plot(y='KBS')` : 'KBS'에 대한 line graph만 그려줌
- `df.plot(y=['KBS', 'JTBC'])` : 'KBS'와 'JTBC'에 대한 line graph만 그려줌
- `df[:, ['KBS', 'JTBC']].plot()` : (위와 같음)
### bar graph
- `df.plot(kind='bar') : df라는 dataframe에 대한 bar graph가 그려짐
- `df.plot(kind='barh') : 가로로 눕혀진 bar graph가 그려짐
- `df.plot(kind='bar', stacked=True) : 쌓여진 bar graph가 나타남
