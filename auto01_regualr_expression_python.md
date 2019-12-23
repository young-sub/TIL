#  파이썬 정규표현식

```python
# 정규 표현식 없이 번호 찾기
def isPhoneNumber(text) :
    if len(text) !=12:
        return False
    for i in range(0,3) :
        if not text[i].isdecimal() :
            return False

    if text[3] != "-" :
        return False
    for i in range(4,7) :
        if not text[i].isdecimal() :
            return False

    if text[7] != "-" :
        return False
    for i in range(8,12) :
        if not text[i].isdecimal() :
            return False
    return True

message = 'call me at 010-548-1848 tomorrow. Or 010-548-4888 please.'
for i in range(len(message)) :
    chunk = message[i:i+12]
    if isPhoneNumber(chunk) :
        print("Phone number found: "+ chunk)
print('Done')
    
# 정규 표현식으로 찾기
import re
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneNumRegex.search('My num is 010-548-1848.')
print('Phone num :', mo.group())


## 괄호로 묶기
phoneNumRegex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
mo = phoneNumRegex.search('My num is 010-548-1848.') 
mo.group(0)
mo.group(1)
mo.group(2)
mo.groups()


## 파이프로 여러 그룹 대조하기
# 여러개라면 처음으로 일치하는 텍스트가 Match로 반환된다.
hero = re.compile(r'Bat(hman|mobile)|Tina')
mo1 = hero.search('Bathmae and Batmobile and Tina')
mo1.group()
mo1.group(1)

## 물음표와 선택적 대조
# ?란 '그 앞에 있는 그룹이 0번 혹은 1번 나타나면 일치한다.'
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batwoman')
mo1.group()

## 별표로 0개 또는 그 이상과 일치시키기
# *란 '그 앞에 있는 그룹과 0개 또는 그 이상과 일치'
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batwowowoman')
mo1.group()

## 더하기 기호로 하나 또는 그 이상과 일치시키기
# +란 '그 앞에 있는 그룹과 1개 또는 그 이상이 일치'
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batman')
mo1 == None
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
mo1.group()

## 중괄호로 특정 횟수 반복 일치시키기
# (Ha){3}  > HaHaHa 찾기
# (Ha){,3} > Ha가 0번에서 3번 나타나면 일치
# (Ha){1,3} > Ha가 1~3번 나타나면 일치

## 최대 일치와 최소 일치
# 파이썬은 기본적으로 최대 일치하는 값이 있다면 그 값을 반환한다.
# 최소 일치 값을 반환하려면 정규식 뒤에 ?를 놓아야 한다.

## findall() 메소드
# search()는 최소 일치 값만 돌려주나 findall()은 모든 일치 값을 리스트로 돌려준다.
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}') # no group
phoneNumRegex.findall('cell : 415-154-1545 work: 151-000-4878') 

# 그룹이 있을 시 리스트 안의 튜플로 반환한다.
phoneNumRegex = re.compile(r'(\d{3})-(\d{3})-(\d{4})') # has groups
phoneNumRegex.findall('cell : 415-154-1545 work: 151-000-4878')

## 문자 클래스
# \d \D 숫자 / 숫자아닌 모든 글자
# \w \W 문자,숫자 글자, 밑줄 글자 / 그 아닌 모든 글자
# \s \S 빈칸,탭, 줄바꿈 문자  / 그 아닌 모든 글자
xmasRegex = re.compile(r'\d+\s\w+')
xmasRegex.findall("12 dram 22 cake 1bird 222 stone 2    ki")

## 사용자 정의 문자 클래스 만들기
# 대괄호 안에서는 익스케이프 문자(\)가 필요 없다.
vowelRegex = re.compile(r'[aeiouAEIOU.]')
vowelRegex.findall('probono conecheese chicken star.')

# 캐럿(^)은 부정 연산자.
cosonantRegex = re.compile(r'[^aeiouAEIOU]')
cosonantRegex.findall('probono conecheese chicken star')

## 캐럿과 달러 기호 글자
# 검색 텍스트의 시작 부분에서 정규식과 일치하는 텍스트가 나타나도록 ^를 사용
beginWithHello = re.compile(r'^Hello')
beginWithHello.search('Hello world')
beginWithHello.search('He said Hello') == None

# 검색 텍스트의 끝 부분에서 정규식과 일치하는 텍스트가 나타나도록 $를 사용
endsWithNumber = re.compile(r'\d$')
endsWithNumber.search('Your number is 42')
endsWithNumber.search('456 is Your num') == None

# 둘다 사용할 시 전체 문장이 해당 정규 표현식과 일치해야한다.

## 와일드카드 문자
# . 은 줄바꿈을 제외한 모든 문자(한 글자)와 일치한다.
# .*로 모든 문자와 일치시킬 수있다. (최소일치를 사용하려면 ?를 붙일 것)
nameRegex = re.compile(r'First Name : (.*) Last Name : (.*)')
mo = nameRegex.search('First Name : AI Last Name : kinda')
mo.group(1)
mo.group(2)

# 두번째 매개변수에 re.DOTALL 입력하면 줄바꿈도 포함하여 찾아준다.
noNewLineRegex = re.compile('.*')
noNewLineRegex.search('Serve the public. \n protect the innocent').group()

noNewLineRegex = re.compile('.*', re.DOTALL)
noNewLineRegex.search('Serve the public. \n protect the innocent').group()

## 대소문자 구분하지 않게 하기 (re.IGNORECASE or re.I)
robocap = re.compile(r'robocap', re.IGNORECASE)
robocap.search('roboCap is part man ,cocopa').group()

## sub() 메소드로 문자열 대체하기
agentNameRegex = re.compile(r'Agent (\w)\w*')
agentNameRegex.sub(r'\1*****', 'Agent Alice 222 told Agent Carol 33 that Agent Eve 1 knew Agent Bob was a double agent')

## 복잡한 정규표현식 관리하기 (re.VERBOSE)
# re.VERBOSE|re.DOTALL이란 식으로 매개변수 여러개 주는 것도 가능
phoneRegex = re.compile(r'''
                        (\d{3})|\(\d{3}\))?             # area code
                        (\s|-|\/)?                      # separator
                        \d{3}                           # first 3 digits
                        (\s|-|\.)                       # separator
                        \d{4}                           # last 4 digits
                        (\s*(ext|x|ext.)\s*\d{2,5})?    # extension
                        ''', re.VERBOSE)


```

