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

PATH = "./chromedriver.exe"
driver = webdriver.Chrome(PATH)


# driver.maximize_window()


def waitforbutton(buttonclass):
    timeout = 5
    try:
        element_present = EC.presence_of_element_located((By.CLASS_NAME, buttonclass))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print(f"Page html did not load after {timeout} seconds. . .")
    driver.find_element_by_class_name(buttonclass).click()


def waitforfield(fieldid, fieldvalue):
    timeout = 5
    try:
        element_present = EC.presence_of_element_located((By.ID, fieldid))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print(f"Page html did not load after {timeout} seconds. . .")
    driver.find_element_by_id(fieldid).send_keys(fieldvalue)


def waitfordropdown(dropdownname, dropdownvalue):
    timeout = 5
    try:
        element_present = EC.presence_of_element_located((By.NAME, dropdownname))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print(f"Page html did not load after {timeout} seconds. . .")
    Select(driver.find_element_by_name(dropdownname)).select_by_visible_text(
        dropdownvalue)


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
    time.sleep(1)
    waitforbutton('btn-lg')
    waitforbutton('js-cia-guest-button')

    # fill in payment info
    waitforfield("user.emailAddress", Constants.userinfo["email"])
    waitforfield("user.phone", Constants.userinfo["phone"])
    driver.find_element_by_class_name("btn-secondary").click()
    waitforfield("optimized-cc-card-number", Constants.userinfo["ccn"])
    waitfordropdown("expiration-year", Constants.userinfo["ccexpirationyear"])
    waitfordropdown("expiration-month", Constants.userinfo["ccexpirationmonth"])
    waitforfield("credit-card-cvv", Constants.userinfo["cvv"])
    waitforfield("payment.billingAddress.firstName", Constants.userinfo["firstname"])
    waitforfield("payment.billingAddress.lastName", Constants.userinfo["lastname"])
    driver.find_element_by_class_name("autocomplete__toggle").click()
    waitforfield("payment.billingAddress.street", Constants.userinfo["address"])
    waitforfield("payment.billingAddress.city", Constants.userinfo["city"])
    waitfordropdown("state", Constants.userinfo["state"])
    waitforfield("payment.billingAddress.zipcode", Constants.userinfo["zipcode"])
