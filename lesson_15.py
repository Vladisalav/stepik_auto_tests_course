from selenium import webdriver
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.implicitly_wait(12)
browser.get("http://suninjuly.github.io/explicit_wait2.html")

WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))

button = WebDriverWait(browser, 0).until(
        EC.element_to_be_clickable((By.ID, "book"))
    )
button.click()

browser.execute_script("return arguments[0].scrollIntoView(true);", button)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
x = x_element.text
y = calc(x)
input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
input1.send_keys(y)

browser.find_element(By.CSS_SELECTOR, "#solve").click()


