from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
# options.add_argument("headless")  # headless 모드 설정
options.add_argument("window-size=1920x1080")
options.add_argument("--start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.page_load_strategy = "none"

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=options)
driver = webdriver.Chrome(executable_path="chromedriver", chrome_options=options)
