from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import requests
from random import randint

app = Flask(__name__)

line_bot_api = LineBotApi('nA9vhCF4KlM9/aJlYyxz/pJzLU2un+Otz1dpV+cViAGq+5N3Dn6qFz8i4OIQwsysQ5enSh30Dzxt/xNMAOhSS8k2WmAfbchfF4xFweeQUZ+SjxyMjko5K5mOrgLA0lQ+QdYGsOPjS8mbcZ6bJoxRmQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('76dce5251e48051e42ea6ddd1ed4aeb8')

@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print(
            "Invalid signature. Please check your channel access token/channel secret."
        )
        abort(400)
    return "OK"


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    keyword = event.message.text.lower()
    
    
    if keyword == "訂飲料":
        output = get_menu()
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=output))

headers = {
            "referer": "https://www.foodpanda.com.tw/",
            "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36",
        }
def _pick_url():
    urls = ['z5uw', 'n9qx', 'rghb', 'u6y4', 'kd3t']
    flag = 400
    while flag == 400:
        url = f"https://tw.fd-api.com/api/v5/vendors/{urls[randint(0, len(urls)-1)]}?include=menus,bundles,multiple_discounts&language_id=6&dynamic_pricing=0&opening_type=delivery&basket_currency=TWD&latitude=24.8055183&longitude=120.9915418"
        check = requests.get(url, headers=headers).json()
        flag = check["status_code"]
    return url

def get_menu():
    url = _pick_url()
    data = requests.get(url, headers=headers).json()
    title = data["data"]["name"]
    menus = data["data"]["menus"][0]["menu_categories"]
    emojis = ["🥤", "☕", "🧃", "🧉", "🍹"]
    output = ""
    output += (f"訂飲料囉~!\n今天喝📢{title}!\n")
    for idx in range(len(menus)):
        output += emojis[randint(0, len(emojis)-1)]+"\n"
        if "注意事項" not in menus[idx]["name"]:
            for product in menus[idx]["products"]:
                if not product["is_sold_out"]:
                    price = ""
                    for info in product["product_variations"]:
                        if "name" in info:
                            price += (
                                f'{int(round(info["price"], 0))}/{info["name"]} '
                            )
                        else:
                            price += f'{int(round(info["price"], 0))} '
                    output +=(f'{product["name"]} ($:{price})\n')
    return output

if __name__ == "__main__":
    app.run()
