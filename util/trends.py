import json
from urllib.request import urlopen


def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text


def get_trends():
    replacements = {"&#39;": "", "&quot;": "", "&nbsp;": ""}

    api_url = f"https://trends.google.co.kr/trends/api/dailytrends?hl=ko&tz=-540&geo=KR&ns=15"

    data = urlopen(api_url).read().decode("utf8")
    data = data[data.find(",") + 1 :]
    json_data = json.loads(data)["default"]["trendingSearchesDays"][0]["trendingSearches"]

    text = ""

    for data in json_data:
        text += f'{data["title"]["query"]}<br/>{replace_all(data["articles"][0]["title"], replacements)}<br/>{replace_all(data["articles"][0]["snippet"], replacements)}<br/><br/>'

    return text
