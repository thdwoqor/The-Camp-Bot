import json
import os
from datetime import datetime, timedelta
from urllib.request import urlopen


def date_to_transform(date: str) -> str:
    return datetime.strftime(datetime.strptime(date, "%Y%m%d"), "%Y-%m-%d")


def time_to_transform(date: str) -> str:
    return datetime.strftime(datetime.strptime(date, "%H%M"), "%H:%M")


def sky_code(number: str) -> str:
    code = {"1": "맑음", "3": "구름많음", "4": "흐림"}
    return code[number]


def ptv_code(number: str) -> str:
    code = {"0": "없음", "1": "비", "2": "비/눈", "3": "눈", "4": "소나기"}
    return code[number]


def is_activate(dt_txt: str):
    time = int(dt_txt[0:2])
    if (time < 6 or time > 18) or time % 3 != 0:
        return False
    return True


def is_end(dt_txt: str):
    return True if dt_txt == "1800" else False


def get_weather():
    service_key = os.getenv("KEY")
    now = datetime.now() - timedelta(1)
    now_date = now.strftime("%Y%m%d")

    api_url = f"https://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst?serviceKey={service_key}&pageNo=1&numOfRows=1000&dataType=JSON&base_date={now_date}&base_time=0500&nx=62&ny=95"

    data = urlopen(api_url).read().decode("utf8")
    json_data = json.loads(data)["response"]["body"]["items"]["item"]

    text = ""

    for weather in json_data:
        if not is_activate(weather["fcstTime"]):
            continue

        if weather["category"] == "TMP":
            text += f'예측일자: {date_to_transform(weather["fcstDate"])} {time_to_transform(weather["fcstTime"])}, 기온: {weather["fcstValue"]}℃, '
        if weather["category"] == "SKY":
            text += f'하늘상태: {sky_code(weather["fcstValue"])}, '
        if weather["category"] == "PTY":
            text += f'강수형태: {ptv_code(weather["fcstValue"])}, '
        if weather["category"] == "POP":
            text += f'강수확률: {weather["fcstValue"]}%\n'
            if is_end(weather["fcstTime"]):
                text += "\n"
    return text
