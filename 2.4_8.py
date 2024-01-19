import math
import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    cost = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    book_btn = browser.find_element(By.ID, "book")
    book_btn.click()

    x_value_locator = browser.find_element(By.ID, "input_value")
    x = calc(x_value_locator.text)

    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(x)

    submit_btn = browser.find_element(By.ID, "solve")
    submit_btn.click()

finally:
    time.sleep(10)
    browser.quit()
