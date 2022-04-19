import os
import time
from datetime import datetime

from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from util.driver import driver
from util.weather import get_weather

load_dotenv(verbose=True)


def switch_text_editor():
    while True:
        try:
            time.sleep(1)
            driver.switch_to.default_content()
            driver.switch_to.frame(0)
            break
        except:
            pass


def switch_default():
    while True:
        try:
            time.sleep(1)
            driver.switch_to.default_content()
            break
        except:
            pass


def thecamp_login():
    login_url = "https://www.thecamp.or.kr/login/viewLogin.do"
    driver.get(login_url)

    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="emailLoginBtn"]')))

    id = driver.find_element(By.XPATH, '//*[@id="userId"]')
    id.send_keys(os.getenv("ID"))

    pw = driver.find_element(By.XPATH, '//*[@id="userPwd"]')
    pw.send_keys(os.getenv("PW"))

    driver.find_element(By.XPATH, '//*[@id="emailLoginBtn"]').click()

    time.sleep(1)

    if driver.current_url == login_url:
        thecamp_login()


def write_letter():
    driver.get("https://www.thecamp.or.kr/eduUnitCafe/viewEduUnitCafeMain.do")

    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="divSlide1"]/div[1]/div[2]/div/div[2]/a[1]')))
    driver.find_element(By.XPATH, '//*[@id="divSlide1"]/div[1]/div[2]/div/div[2]/a[1]').click()

    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[3]/button")))
    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[3]/button").click()

    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/section/div[2]/a[3]")))
    now = datetime.now()
    now_date = now.strftime("%Y-%m-%d")
    driver.find_element(By.XPATH, '//*[@id="sympathyLetterSubject"]').send_keys(f"[{now_date}] 일기예보")

    switch_text_editor()

    driver.find_element(By.XPATH, "/html/body/p").send_keys(get_weather())

    switch_default()

    driver.switch_to.default_content()
    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/section/div[2]/a[3]").click()


if __name__ == "__main__":
    thecamp_login()
    write_letter()
    driver.quit()
