import requests
from random import randint


class HUNGRYWORKER:
    def __init__(self):
        self.headers = {
            "referer": "https://www.foodpanda.com.tw/",
            "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36",
        }

    def _pick_url(self):
        urls = ["z5uw", "n9qx", "rghb", "u6y4", "kd3t"]
        flag = 400
        while flag == 400:
            url = f"https://tw.fd-api.com/api/v5/vendors/{urls[randint(0, len(urls)-1)]}?include=menus,bundles,multiple_discounts&language_id=6&dynamic_pricing=0&opening_type=delivery&basket_currency=TWD&latitude=24.8055183&longitude=120.9915418"
            check = requests.get(url, headers=self.headers).json()
            flag = check["status_code"]
        return url

    def get_menu(self):
        url = self._pick_url()
        data = requests.get(url, headers=self.headers).json()
        title = data["data"]["name"]
        menus = data["data"]["menus"][0]["menu_categories"]
        emojis = ["🥤", "☕", "🧃", "🧉", "🍹"]
        output = ""
        output += f"訂飲料囉~!\n今天喝📢{title}!\n"
        for idx in range(len(menus)):
            output += emojis[randint(0, len(emojis) - 1)] + "\n"
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
                        output += f'{product["name"]} ($:{price})\n'
        return output
