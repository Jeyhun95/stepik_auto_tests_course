from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id("input_value").text
    result = calc(x)

    result = browser.find_element_by_css_selector("[id='answer']").send_keys(result)
    robotcheckbox = browser.find_element_by_css_selector("[id='robotCheckbox']").click()
    robotbutton = browser.find_element_by_css_selector("[id='robotsRule']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robotbutton)
    robotbutton.click()
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()