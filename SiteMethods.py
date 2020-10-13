# install selenium
# install chromedriver and copy executable to C:/Program Files (x86)
import glob
import os
import time

from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

PATH = "./chromedriver.exe"
driver = webdriver.Chrome(PATH)


def bestbuy(productUrl, refreshrate):
    # get personal info
    try:
        userinfopath = open("InfoFilePath.txt", "r").read()
        userinfofile = open(glob.glob(userinfopath)[0], "r").read()
    except Exception:
        print("There was a problem with your user information file. Check that you have the correct path to your info "
              "file in InfoFilePath.txt and check that your user info file is formatted according to readme "
              "specifications, then run the program again.")
        exit(-1)
    userinfoarray = userinfofile.split('\n')
    userinfo = {}
    for field in userinfoarray:
        values = field.split(': ')
        fieldname = values[0]
        fieldvalue = values[1]
        userinfo[fieldname] = fieldvalue
    email = userinfo['email']
    phone = userinfo['phone']
    firstname = userinfo['firstname']
    lastname = userinfo['lastname']
    address = userinfo['address']
    city = userinfo['city']
    state = userinfo['state'].upper()
    zipcode = userinfo['zipcode']
    ccn = input("User ccn: ")
    cvv = input("User cvv: ")
    ccexpirationyear = input("User cc expiration year, e.g. 2020: ")
    ccexpirationmonth = input("User cc expiration month, e.g. 01: ")

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
    driver.find_element_by_class_name("btn-primary").click()
    time.sleep(2)
    driver.find_element_by_class_name("js-cia-guest-button").click()
    time.sleep(2)

    # fill in payment info
    # email, phone, and cc have to be exported locally as environment variables
    driver.find_element_by_id("user.emailAddress").send_keys(email)
    driver.find_element_by_id("user.phone").send_keys(phone)
    driver.find_element_by_class_name("btn-secondary").click()
    time.sleep(2)
    driver.find_element_by_id("optimized-cc-card-number").send_keys(ccn)
    time.sleep(1)
    Select(driver.find_element_by_name("expiration-year")).select_by_visible_text(ccexpirationyear)
    Select(driver.find_element_by_name("expiration-month")).select_by_visible_text(ccexpirationmonth)
    driver.find_element_by_id("credit-card-cvv").send_keys(cvv)
    driver.find_element_by_id("payment.billingAddress.firstName").send_keys(firstname)
    driver.find_element_by_id("payment.billingAddress.lastName").send_keys(lastname)
    driver.find_element_by_class_name("autocomplete__toggle").click()
    driver.find_element_by_id("payment.billingAddress.street").send_keys(address)
    driver.find_element_by_id("payment.billingAddress.city").send_keys(city)
    Select(driver.find_element_by_name("state")).select_by_visible_text(state)
    driver.find_element_by_id("payment.billingAddress.zipcode").send_keys(zipcode)
    driver.find_element_by_class_name("btn-lg").click()

