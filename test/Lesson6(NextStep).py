from selenium import webdriver
import time


link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    browser.find_element_by_xpath("//div[@class='form-group first_class']").send_keys("TestName")
    time.sleep(10)
    browser.find_element_by_xpath("//input[@placeholder='Input your last name']").send_keys("TestSurname")
    browser.find_element_by_xpath("//input[@placeholder='Input your email']").send_keys("test@mail.ru")
    browser.find_element_by_xpath("//input[@placeholder='Input your phone:']").send_keys("89999999999")
    browser.find_element_by_xpath("//input[@placeholder='Input your address:']").send_keys("TestCity")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()