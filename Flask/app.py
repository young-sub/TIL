from flask import Flask
from flask import render_template
from flask import request
import random
import requests

app = Flask(__name__)

# 데코레이터를 이용하여 해당 루트로 접근한 사람에게 원하는 메세지를 보내는 것
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/mulcam')
def mulcam():
    return 'This is mulcam'

@app.route('/greeting/<string:name>')
def greeting(name):
    return f'hello {name}'

# 요청값은 str여야 응답 가능하다.
@app.route('/cube/<int:num>')
def cube(num):
    result = num **3
    return str(result)

@app.route("/lunch/<int:people>")
def lunch(people):
    menu = ["paste","pizza","짜장면","짬뽕","라면","꽝"]
    import random
    order = random.sample(menu,people)
    return str(order)

# html 불러오는 것도 가능
@app.route('/html')
def html():
    return "<h1> 안녕하세요!! <h1>"

@app.route('/html_file')
def html_file():
    return render_template('html_file.html')

@app.route('/hi/<string:name>')
def hi(name):
    return render_template("hi.html", your_name =name)

# fake 네이버
@app.route('/naver')
def naver():
    return render_template('naver.html')

# 핑퐁하기
@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    name = request.args.get('name')
    message = request.args.get('message')
    return render_template('pong.html', name=name, message=message)

# 핑퐁 연습
@app.route('/inputing')
def inputing():
    return render_template('inputing.html')

@app.route('/outputing')
def outputing():
    name = request.args.get('name')
    result = ['당신은 힘이 쎄군요','돈이 많네요','운이 좋아요','없어요','꽝','성공','실패']
    result = random.sample(result,2)
    result = ", ".join(map(str, result))
    return render_template('outputing.html', name=name, result = result)

# 아스키 코드 출력하기 (ascii)
@app.route('/ascki')
def ascki():
    return render_template('ascki.html')

@app.route('/ascki_result')
def ascki_result():
    #1. form 태그로 날린 데이터(word)를 받는다.
    word = request.args.get('word')
    #2. word를 가지고 ascki_art API 요청 주소로 요청을 보낸다.
    result1 = requests.get(f'http://artii.herokuapp.com/make?text={word}').text

    #3. API 응답 결과를 html 파일에 넣어서 보여준다.
    return render_template('ascki_result.html',word=word, result1=result1)

@app.route('/lotte_check')
def lotte_check():
    return render_template('lotte_check.html')

@app.route('/lotte_result')
def lotte_result():
    lotte_round = request.args.get('lotte_round')

    response = requests.get(f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={lotte_round}')
    lotte = response.json()
    
    # drwtNo6 = lotte["drwtNo6"] # 반환하는 값이 없다면 에러
    # drwtNo6 = lotte.get("drwtNo6") # 반환하는 값이 없다면 NONE

    #1. for문 활용
    lotte_number = []
    for i in range(1,7):
        lotte_number.append(lotte[f"drwtNo{i}"]) # 반환하는 값이 없다면 NONE

    # #2. list comprehension
    # lotte_number = [lotte[f"drwtNo{i}"] for i in range(1,7)]
      
    l_numbers = request.args.get('l_numbers') #string
    numbers = l_numbers.split() # list안 string
    numbers_int = []

    for number in numbers :
        numbers_int.append(int(number))

    matched = len(set(lotte_number) & set(numbers_int))
    if matched == 6:
        result = "1등 입니다!!"
    else :
        result = "아쉽습니다."

        
    return render_template('lotte_result.html',
    lotte_round =lotte_round, 
    lotte_number=lotte_number,
    l_numbers=numbers_int, 
    result = result
    )



# 직접 파일을 커맨드에서 실행했을 때만 if 밑에가 실행됨 
# 다른 파일에서 import 시 실행 안됨
# if True일시 Flask를 매번 재기동 하지 않아도 자동으로 반영됨
if __name__ == '__main__':
    app.run(debug=True)
