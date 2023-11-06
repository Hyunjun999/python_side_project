from currency_converter import CurrencyConverter
from bs4 import BeautifulSoup
import requests


def fx_rate(target1, target2):
    # User-Agent: servers can notice the os, application(browser), or its version, etc through this
    # Content-Type: media type of actual returned content
    headers = {"User-Agent": "Mozilla/5.0", "Content-Type": "text/html; charset=utf-8"}
    res = requests.get(
        f"https://www.google.com/finance/quote/{target1}-{target2}", headers=headers
    )
    content = BeautifulSoup(res.content, "html.parser")
    containers = content.find("div", {"class": "YMlKec fxKbKc"})
    print(containers.text)


fx_rate("usd", "krw")
