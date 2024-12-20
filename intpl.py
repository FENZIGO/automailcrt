from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import json
import time
import random


chromedriver_path = "/usr/bin/chromedriver"
chromedriver_service = Service(chromedriver_path)

headless_mode = False
chrome_options = Options()


if headless_mode:
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-software-rasterizer")

browser = webdriver.Chrome(service=chromedriver_service, options=chrome_options)

random_append = random.randint(0, 999999)

def save_to_file(login, password):

    with open("logininfo.txt", "a") as file:
        file.write(f"{login+str(random_append)}:{password}\n")

def create_account_and_check_for_congratulations(login, password):
    try:
        congrat_message = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/section[2]/div[2]/div/div/div[1]/form[2]/div[1]/div/label'))
        )

        if congrat_message:
            save_to_file(login, password)
            print("Account was created. Added to logininfo.txt\n")

    except TimeoutException:
        print("Something went wrong. Account was not created.")

    finally:
        browser.quit()

class tools:

    def create_account(login, password):
        browser.get("https://int.pl/#/register")
        print(f"Creating account with LOGIN:{login+str(random_append)}, PASSWORD:{password}")


        login_field = browser.find_element(By.ID, 'loginId')
        login_field.send_keys(login)

        password_field = browser.find_element(By.ID, 'passwordId')
        password_confirm_field = browser.find_element(By.XPATH, '/html/body/section[2]/div[2]/div/div/div[1]/form[2]/div[3]/input')
        password_field.send_keys(password)
        password_confirm_field.send_keys(password)

        browser.execute_script("arguments[0].click();", WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="portalRulesId"]'))
))


        error_field = WebDriverWait(browser, 2).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/section/div[2]/div/div/div[1]/form[2]/div[1]/div[1]/div[3]/div/span[3]'))
        )

        if error_field.get_attribute('textContent') == "Zajęty":
            u_fix = browser.find_element(By.ID, 'loginId')
            u_fix.send_keys(str(random_append))


        submit = browser.find_element(By.XPATH, '//button[@class="button button--left button--mark button--moema ng-scope" and text()="zakładam konto"]')
        submit.click()
        time.sleep(1)
        browser.execute_script("arguments[0].click();", submit)
        time.sleep(1)

        create_account_and_check_for_congratulations(login, password)

