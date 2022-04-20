import os
from datetime import datetime

import requests
from dotenv import load_dotenv

from util.weather import get_weather

load_dotenv()


def letter(subject: str, content: str):
    data = {
        "boardDiv": "sympathyLetter",
        "tempSaveYn": "N",
        "traineeMgrSeq": os.getenv("TRAINEE"),
        "sympathyLetterContent": content,
        "trainUnitCd": os.getenv("CD"),
        "trainUnitEduSeq": os.getenv("EDUSEQ"),
        "sympathyLetterSubject": subject,
        "sympathyLetterEditorFileGroupSeq": "",
        "fileGroupMgrSeq": "",
        "fileMgrSeq": "",
        "sympathyLetterMgrSeq": "",
    }
    url = "https://www.thecamp.or.kr/consolLetter/insertConsolLetterA.do"
    cookie = os.getenv("COOKIE")
    response = requests.post(url=url, data=data, headers={"cookie": cookie})
    print(response.text)


def today():
    return datetime.now().strftime("%Y-%m-%d")


if __name__ == "__main__":
    letter(f"[{today()}] 일기예보", f"<p>{get_weather()}</p>")
