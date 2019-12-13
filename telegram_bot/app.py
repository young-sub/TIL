from flask import Flask
from flask import request
from flask import render_template
from decouple import config
import requests
import random


app = Flask(__name__)

token = config("TELEGRAM_BOT_TOKEN")
app_url = f"https://api.telegram.org/bot{token}"
client_id = config("NAVER_CLIENT_ID")
client_secret = config("NAVER_CLIENT_SECRET")

@app.route(f"/{token}", methods=["POST"])
def telegram():
    from_telegram = request.get_json()
    
    chat_id = from_telegram.get("message").get("from").get('id')
    text = from_telegram.get("message").get("text")

    # lotto라고 입력하면 번호 출력하기 아니면 echo
    if text == "/lotto" :
        reply = random.sample(range(1,46),6)
        reply.sort()

    # 파파고 번역 (POST방식)
    if text[0:4] == "/번역 " : #/번역 번역할문장
        headers = {
            "X-Naver-Client-Id" : client_id,
            "X-Naver-Client-Secret" : client_secret
        }

        data = {
            'source': 'en',
            'target': 'ko',
            'text': text[4:]
        }

        papago_url = "https://openapi.naver.com/v1/papago/n2mt"
        papago_res = requests.post(papago_url, data=data, headers=headers)
        papago_res = papago_res.json()
        reply = papago_res.get("message").get("result").get("translatedText")

    else :
        reply = text

    requests.get(f'{app_url}/sendMessage?chat_id={chat_id}&text={reply}')
    return "", 200


# @app.route("/write")
# def write():
#     return render_template("write.html")

# @app.route("/send")
# def send():
#     message = request.args.get("message")
#     message_url = f"{app_url}/sendMessage?chat_id={chat_id}&text={message}"
#     requests.get(message_url)
#     return "메시지 전송 완료했어요!"

if __name__ == '__main__':
    app.run(debug=True)