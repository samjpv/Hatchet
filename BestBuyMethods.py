# install selenium
# install chromedriver and copy executable to C:/Program Files (x86)
import time
import js2py
import CommonMethods
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import Constants

PATH = "./chromedriver.exe"
driver = webdriver.Chrome(PATH)


def waitforbutton(elementxpath):
    timeout = 5
    try:
        element_present = EC.presence_of_element_located((By.XPATH, elementxpath))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print(f"Page html did not load after {timeout} seconds. . .")
    time.sleep(0.5)
    driver.find_element_by_xpath(elementxpath).find_element_by_xpath('../..').click()


def bestbuy(productUrl, refreshrate):
    # get personal info
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
        cartbutton = driver.find_element_by_class_name('btn-lg')
        if cartbutton.is_enabled():
            cartbutton.click()
            break
        else:
            driver.refresh()

    # checkout
    time.sleep(2)
    driver.get("https://www.bestbuy.com/cart")

    checkoutxpath = "//*[text()[contains(., \'Checkout\')]]"
    waitforbutton(checkoutxpath)

    time.sleep(2)
    driver.find_element_by_class_name("js-cia-guest-button").click()
    time.sleep(2)

    # fill in payment info
    # email, phone, and cc have to be exported locally as environment variables
    driver.find_element_by_id("user.emailAddress").send_keys(Constants.userinfo["email"])
    driver.find_element_by_id("user.phone").send_keys(Constants.userinfo["phone"])
    driver.find_element_by_class_name("btn-secondary").click()
    time.sleep(2)
    driver.find_element_by_id("optimized-cc-card-number").send_keys(Constants.userinfo["ccn"])
    time.sleep(1)
    Select(driver.find_element_by_name("expiration-year")).select_by_visible_text(Constants.userinfo["ccexpirationyear"])
    Select(driver.find_element_by_name("expiration-month")).select_by_visible_text(Constants.userinfo["ccexpirationmonth"])
    driver.find_element_by_id("credit-card-cvv").send_keys(Constants.userinfo["cvv"])
    driver.find_element_by_id("payment.billingAddress.firstName").send_keys(Constants.userinfo["firstname"])
    driver.find_element_by_id("payment.billingAddress.lastName").send_keys(Constants.userinfo["lastname"])
    driver.find_element_by_class_name("autocomplete__toggle").click()
    driver.find_element_by_id("payment.billingAddress.street").send_keys(Constants.userinfo["address"])
    driver.find_element_by_id("payment.billingAddress.city").send_keys(Constants.userinfo["city"])
    Select(driver.find_element_by_name("state")).select_by_visible_text(Constants.userinfo["state"])
    driver.find_element_by_id("payment.billingAddress.zipcode").send_keys(Constants.userinfo["zipcode"])
    # driver.find_element_by_class_name("btn-lg").click()
