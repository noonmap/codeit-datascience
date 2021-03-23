# Topic5: 데이터 만들기
## Chapter
1. 데이터를 만드는 방법
2. 웹 페이지 가져오기
3. 필요한 데이터 골라내기
## Contents
- 웹 스크레이핑 (Web Scraping)
<br> 특정 웹에서 내용을 수집하는 것
- 웹 크롤링 (Web Crawling)
<br> 컴퓨터에서 자동으로 웹의 내용을 수집하게 하는 것

### 파이썬으로 서버에 요청 보내기
```python
import requests
# 서버에 요청
page = requests.get("https://www.google.com")
# html 코드를 받아옴
page.text
```
### CSS 선택자 (CSS selector)
스타일 적용의 범위를 정하는 코드를 의미.
- HTML 태그 &rarr; 그냥 적음
	- ex) `p`, `li`, ...
- 아이디 (id) &rarr; #을 붙임
	- 아이디는 HTML 코드 중 단 한번만 적용해야 함
	- ex) `#specific_id`
- 클래스 (class) &rarr; 온점(.)을 붙임
	- 클래스는 여러 HTML 태그에 공통으로 적용가능
	- ex) `.specific_class`
- 속성 (attribute) &rarr; 대괄호에 `tag[key="value"]`로 넣음
	- ex) `specific_tag[specific_attr_name="specific_attr_value"]` `a[name='coffee']`
- Reference
	- https://www.w3schools.com/cssref/css_selectors.asp
### CSS selector의 operator
- OR &rarr; 쉼표(,)
	- ex) `.class1, .class2`
- AND &rarr; 붙여서 씀
	- ex) `.class1.class2`
- **자손** 태그 &rarr; 띄어쓰기
	- ex) `p i` : `<p>` 태그 아래에 있는 `<i>` 태그를 의미
- **자식** 태그 (바로 아래에 속한 태그) &rarr; `tag > tag`
	- ex) `p > i` : `<p>` 태그 바로 아래에 있는 `<i>` 태그를 의미
- Reference
	- https://gist.github.com/magicznyleszek/809a69dd05e1d5f12d01
### HTML 파싱: BeautifulSoup
python에서 HTML을 파싱하는 걸 도와주는 tool
```python
from bs4 import BeautifulSoup
  
# HTML 코드 받아오기 
html_code = requests.get("https://workey.codeit.kr/music/index")

# BeautifulSoup 타입으로 변환
# 'html.parser' : HTML을 파싱한다는 의미
soup = BeautifulSoup(html_code.text, 'html.parser')

# 모든 <li> 태그 선택하기
li_tags = soup.select('li')
# 첫 번째 <li> 태그의 텍스트를 추출하기
li_tag = li_tags[0].text

# 모든 <img> 태그 선택하기 
img_tags = soup.select('img') 
# 첫 번째 요소의 "src" 속성 값 가져오기 
img_src = img_tags[0]["src"]
```
