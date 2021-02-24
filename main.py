from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
promise_down = 10
promise_up = 5
path = r'C:\Users\LENOVO\Devlopment\chromedriver.exe'
twitter_email = "----------Email-------------"
twitter_password = "-----------Password-------------"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        driver = self.driver
        driver.get("https://www.speedtest.net/")
        time.sleep(3)
        go_button = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go_button.click()
        # print('done')
        time.sleep(60)
        self.down = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.up = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text


    def tweet_at_provider(self):
        driver = self.driver
        driver.get('https://twitter.com/?lang=en')
        login = driver.find_element_by_xpath('/html/body/div/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]')
        login.click()
        time.sleep(1)

        useremail = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        useremail.send_keys(twitter_email)
        password = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        password.send_keys(twitter_password)
        password.send_keys(Keys.ENTER)

        time.sleep(5)
        tweet_compose = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {promise_down}down/{promise_up}up?"
        tweet_compose.send_keys(tweet)
        time.sleep(3)

        tweet_button = driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()

        time.sleep(2)
        driver.quit()


bot = InternetSpeedTwitterBot(driver_path=path)
bot.get_internet_speed()
bot.tweet_at_provider()