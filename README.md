# The Camp Bot
<a href="https://github.com/features/actions"><img src="https://img.shields.io/badge/GitHub Actions-2088FF?style=for-the-badge&logo=GitHub Actions&logoColor=white"/></a>
<a href="https://www.selenium.dev/"><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white"/></a>  
>더캠프 위문편지 매크로

| **일기예보** | 
| :---: | 
| ![일기예보](https://user-images.githubusercontent.com/83541246/164165614-9a69def9-3dbd-4434-8b73-0858ae0daf3f.PNG)| 
| [공공데이터포털](https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15084084)에서 기상청 API을 받아와서 위문편지를 보냅니다. |

| **인기 검색어** |
| :---: | 
| ![인기 검색어](https://user-images.githubusercontent.com/83541246/164166706-7016726b-aa11-4684-a4f5-18dcd7e28ceb.PNG) |
| [구글 트렌드](https://trends.google.co.kr/trends/trendingsearches/daily?geo=KR)에서 일별 인기 급상승 검색어 API을 받아와서 위문편지를 보냅니다. |  

| **스도쿠** |
| :---: | 
| ![스도쿠](https://user-images.githubusercontent.com/83541246/165344181-fe1c24a4-f430-4d61-8c5a-340caa7f3491.PNG) |
| [국방 일보](https://kookbang.dema.mil.kr)에서 스도쿠 이미지를 받아와서 위문편지를 보냅니다. |  

## Getting Started  

### Installation
<pre><code>git clone https://github.com/thdwoqor/The-Camp-Bot.git
pip install -r requirements.txt
echo "KEY=[<b>yourKEY</b>]" >> .env
echo "COOKIE=[<b>yourCOOKIE</b>]" >> .env
echo "TRAINEE=[<b>yourTRAINEE</b>]" >> .env
echo "CD=[<b>yourCD</b>]" >> .env
echo "EDUSEQ=[<b>yourEDUSEQ</b>]" >> .env
</code></pre>
`KEY는 공공 데이터 포털 인증키 입니다.`  
`COOKIE,TRAINEE,CD,EDUSEQ 값은 편지를 보냈을때 크롬 개발자옵션[F12]를 통해 확인할수있습니다.`  

![크롬 개발자옵션[F12]](https://user-images.githubusercontent.com/83541246/164168005-76c61c8e-ebc5-4e5a-bc9e-017101f6e97b.jpg)


### Run

<pre><code>python run.py</code></pre>

## LICENSE

[MIT License](./LICENSE)
