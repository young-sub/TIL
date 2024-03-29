# 마크다운(Markdown)  # 1개

> 일반 텍스트 형식 구문을 사용하는 마크업 언어의 일종으로 사용법이 쉽고 간결하여 빠르게 문서 정리를 할 수 있습니다. 단, 모든 HTML 마크업을 대체하지는 않습니다.



## 1. 문법 # 2개

### 1.1 Header

> 헤더는 제목을 표현할 떄 사용합니다.

- `<h1>`부터 `<h6>`까지 표현 가능합니다.

- `#`의 개수로 표현하거나 `<h1></h1>` 의 형태로 표현 가능합니다.

  ## 세개 # 3개

  #### 네개 # 4개

  ##### 다섯개 # 5개

  ###### 여섯개 # 6

  

## 1.2 List

- `tab`키를 눌러서 하위항목 생성 가능합니다.
- `shift + tab` 키를 눌러서 상위항목으로 이동합니다.





## 1.3 Code Block

> 코드 블럭은 작성한 코드를 정리하거나 강조합니다. 또한 인라인과 블럭 단위로 구분 가능합니다.

- 코드  블럭

  ``` python
  #``` 이면 코드 블록이 생김
  print('helo')
  
  ```

- 인라인 `코드블록` ` 두개로 감싸면 코드블록



## 1.4 Image

> 로컬에 있는 이미지를 삽입하거나 이미지 링크를 활용합니다.

- `![]()`을 작성하거 `()`안에 이미지 주소를 입력합니다. `[]`안에는 이미지 파일의 이름을 작성합니다.
- 로컬에 이미 파일을 저장한경우 상대경로 이용하여 이미지를 저장합니다.



- 이미지

  ![test.png](C:\Users\student\Desktop\test.png)



## 1.5 Link

> 특정 주소로 링크를 걸때 사용합니다.

- `[]()`을 작성하고 `()`안에 링크 주소를 작성하고 `[]`안에 어떤 링크 주소인지 작성합니다.

- 링크

  [네이버](https://www.naver.com "test 용")



## 1.6 Table

> 표를 작성하여 요소를 구분합니다.

- `|`(파이프) 사이에 칼럼을 작성하고 `enter`키를 입력합니다.
- 마지막 칼럼을 작성하고 뒤에 |를 붙여줍니다.

| table 1                      |      |
| ---------------------------- | ---- |
| 표를만들때는 \|제목\|제목 \| |      |



## 1.7 기타

- 수평선 -----------------

----------------------------

> 인용문 > 

- - -  '-' 표시는 - 번호 없는 목록

- 확장자는 ***.md***
- **강조됨** **
- *기울임*  *	
- ~~취소선~~  ~~ 내용 ~~ 취소선

[이모티콘](https://steemit.com/steemkr-guide/@snow-airline/steemkr-quick-start-guide, 이모티콘 정리)

&#128513;

&#10005;

- [Typora 단축키](https://support.typora.io/Shortcut-Keys/)