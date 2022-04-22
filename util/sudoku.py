from datetime import datetime

import radar
import requests
from bs4 import BeautifulSoup


def get_random_date():
    now = radar.random_datetime(start=datetime(year=2020, month=6, day=30), stop=datetime(year=2022, month=4, day=20))
    return now.strftime("%Y%m%d")


def get_sudoku():
    try:
        now_date = get_random_date()
        print(now_date)
        html = requests.get(f"https://kookbang.dema.mil.kr/newsWeb/{now_date}/1/BBSMSTR_000000010595/view.do")
        soup = BeautifulSoup(html.text, "html.parser")

        contents = soup.find("img", class_="txc-image")["src"]
        if contents is None:
            raise
    except:
        return get_sudoku()
    return f"https://kookbang.dema.mil.kr{contents}"
