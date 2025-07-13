import os
import time
import random
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def random_delay(min_sec=1, max_sec=3):
    time.sleep(random.uniform(min_sec, max_sec))

load_dotenv()

bank = os.getenv("MEROSHARE_BANK")
username = os.getenv("MEROSHARE_USERNAME")
password = os.getenv("MEROSHARE_PASSWORD")

options = Options()
options.binary_location = "/usr/bin/chromium-browser"
service = Service("/usr/lib/chromium-browser/chromedriver")

driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("https://meroshare.cdsc.com.np/#/login")
    wait = WebDriverWait(driver, 10)

    #dropdown for bank
    dp_dropdown_xpath = "/html/body/app-login/div/div/div/div/div/div/div[1]/div/form/div/div[1]/div/div/select2/span/span[1]/span/span[1]"
    dp_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, dp_dropdown_xpath)))
    dp_dropdown.click()
    #options
    option_xpath = f"//li[contains(text(), '{bank}')]"
    bank_option = wait.until(EC.element_to_be_clickable((By.XPATH, option_xpath)))
    bank_option.click()
    #fill username
    username_xpath = "/html/body/app-login/div/div/div/div/div/div/div[1]/div/form/div/div[2]/div/div/input"
    username_input = wait.until(EC.presence_of_element_located((By.XPATH, username_xpath)))
    username_input.send_keys(username)
    #password
    password_xpath = "/html/body/app-login/div/div/div/div/div/div/div[1]/div/form/div/div[3]/div/div/input"
    password_input = wait.until(EC.presence_of_element_located((By.XPATH, password_xpath)))
    password_input.send_keys(password)
    random_delay()

    #login
    login_button_xpath = "/html/body/app-login/div/div/div/div/div/div/div[1]/div/form/div/div[4]/div/button"
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, login_button_xpath)))
    login_button.click()
    
    
    #dashboard nav link
    dashboard_nav_xpath = "/html/body/app-dashboard/div/div[1]/nav/ul/li[8]/a"
    dashboard_nav_link = wait.until(EC.element_to_be_clickable((By.XPATH, dashboard_nav_xpath)))
    driver.execute_script("arguments[0].scrollIntoView(true);", dashboard_nav_link)
    driver.execute_script("arguments[0].click();", dashboard_nav_link)
    random_delay()
    





    input("Press Enter to exit and close browser...")

finally:
    driver.quit()
