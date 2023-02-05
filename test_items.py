
from selenium.webdriver.common.by import By
import time


def test_guest_should_see_add_to_cart_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    elements = browser.find_elements(By.CSS_SELECTOR, "#add_to_basket_form > button")
    time.sleep(5)
    print(f'\n>>>>>>  found elements: {elements}')
    assert elements, 'no appropriate elements found'
