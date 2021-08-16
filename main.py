from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep
import os


CHROME_DRIVER_PATH = "C:\Program Files\Development\chromedriver.exe"
INSTAGRAM_USERNAME = os.environ.get("INSTAGRAM_USERNAME")
INSTAGRAM_PASSWORD = os.environ.get("INSTAGRAM_PASSWORD")
TARGET_ACCOUNT = "chefsteps"      #any Instagram account of your choice

print(INSTAGRAM_USERNAME)


class InstaFollower:
    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        self.driver.get("https://www.instagram.com/")
        sleep(5)

        username_field = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_field.send_keys(INSTAGRAM_USERNAME)

        password_field = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_field.send_keys(INSTAGRAM_PASSWORD)

        sleep(3)

        submit = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
        submit.click()

        sleep(5)

        notifications_popup = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        notifications_popup.click()

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{TARGET_ACCOUNT}")
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div')
        for i in range(10):
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', modal)
            sleep(3)

    def follow(self):
        sleep(5)
        subscription_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in subscription_buttons:
            sleep(2)
            try:
                button.click()
            except ElementClickInterceptedException:
                cancel_popup = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
                cancel_popup.click()

            sleep(5)


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()