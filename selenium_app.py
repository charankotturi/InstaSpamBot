from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from dotenv import load_dotenv
import os

class main:
    def __init__(self,username,count):
        instaMSG(username, count)

load_dotenv()

def instaMSG(username1, count):
    browser = webdriver.Chrome()
    browser.get("https://www.instagram.com/")
    print(browser.title)

    load_dotenv()

    INSTA_USERNAME = os.getenv('INSTA_USERNAME')
    INSTA_PASSWORD = os.getenv('INSTA_PASSWORD')

    try:
        user = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        )

        password = browser.find_element_by_name('password')

        user.clear()
        password.clear()

        user.send_keys(INSTA_USERNAME)
        password.send_keys(INSTA_PASSWORD)

        button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,"button[type='submit']"))
        )

        button.click()

        notNow = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH,"//button[contains(text(), 'Not Now')]"))
        )
        notNow.click()

        notNow2 = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH,"//button[contains(text(), 'Not Now')]"))
        )
        notNow2.click()

        message = browser.find_element_by_css_selector("svg[aria-label='Messenger']")
        message.click()

        strU = "//div[contains(text() , '"+username1+"']"
        print("//div[contains(text() , 'its_bora11']")

        Dude = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text() , '"+username1+"')]"))
        )
        
        Dude.click()

        textArea = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,"textarea[placeholder='Message...']"))
        )

        for i in range(count):
            textArea.send_keys('this message is automated!')
            textArea.send_keys(Keys.ENTER)

        time.sleep(2)
        browser.quit()

    except:
        browser.quit()