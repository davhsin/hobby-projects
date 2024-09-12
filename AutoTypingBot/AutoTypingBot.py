from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class AutoTypingBot:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(options = chrome_options)  
        self.browser.get('https://monkeytype.com/')

    def run(self):
        # reject cookie
        WebDriverWait(self.browser, 10).until(
             EC.element_to_be_clickable(
                 (By.XPATH, "//*[@class='rejectAll']") 
             )
        ).click()

        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[@mode='words']")
            )
        ).click()

        time.sleep(1.0)

        for _ in range(0, 51):
            element = WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//div[@class='word active']")
                )
            )

            WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//input[@id='wordsInput']")
                )
            ).send_keys(element.text + ' ') 

    def exit(self):
        time.sleep(10)
        self.browser.quit()

if __name__ == "__main__":
    auto_typing_bot = AutoTypingBot()
    auto_typing_bot.run()
    auto_typing_bot.exit()
