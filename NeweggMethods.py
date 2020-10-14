# install selenium
# install chromedriver and copy executable to C:/Program Files (x86)
import time
import Constants
import CommonMethods
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = Constants.driver


def tryclosepopup(popupid):
    try:
        driver.find_element_by_id(popupid).click()
    except NoSuchElementException:
        pass


def newegg(productUrl, refreshrate):
    CommonMethods.setuserinfo()
    print("Navigating to product page . . .")

    # open site
    try:
        driver.get(productUrl)
    except Exception:
        print(">The site URL you entered was not valid. Please restart the program and try again.<")
        exit(-1)

    # try to add to cart
    while True:
        time.sleep(refreshrate)
        tryclosepopup('popup-close')
        time.sleep(1)
        cartbutton = driver.find_element_by_class_name('btn-primary')
        if cartbutton.is_enabled():
            cartbutton.click()
            break
        else:
            driver.refresh()
