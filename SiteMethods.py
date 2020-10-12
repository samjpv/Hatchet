# install selenium
# install chromedriver and copy executable to C:/Program Files (x86)

import os
import time

from selenium.webdriver.support.select import Select

from Constants import Sites
from WebsiteObject import WebsiteObject
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

PATH = "./chromedriver.exe"
driver = webdriver.Chrome(PATH)


def neweggnav(productName):
    website = WebsiteObject(Sites.NEWEGG)
    productObj = None
    for product in website.products:
        if product.name == productName:
            productObj = product
            break

    # open site
    siteUrl = website.siteurl
    driver.get(siteUrl)

    # check for popups
    try:
        closePopup = driver.find_element_by_id("popup-close")
        closePopup.click()
    except NoSuchElementException:
        print("no popup")

    # search for product
    searchBar = driver.find_element_by_id("SearchBox2020")
    searchBar.send_keys(productObj.modelnumber)
    searchBar.send_keys(Keys.RETURN)

    # navigate to product page
    time.sleep(1)
    product = driver.find_element_by_xpath("//a[@class=\"item-title\"]")
    product.click()

    # try to add to cart
    time.sleep(1)
    while True:
        driver.refresh()
        try:
            cartbutton = driver.find_element_by_xpath(f"//button[contains(text(), \"Add to cart \")]")
            cartbutton.click()
            break
        except NoSuchElementException:
            print("no add to cart")
        time.sleep(15)


def bestbuynav(productName):
    # get personal info
    print("**The below information will be used to fill in site order forms and will not be recorded anywhere**")
    email = input("User email: ")
    phone = input("User phone: ")
    ccn = input("User ccn: ")
    cvv = input("User cvv: ")
    ccexpirationyear = input("User cc expiration year (----): ")
    ccexpirationmonth = input("User cc expiration month (--): ")
    firstname = input("First name: ")
    lastname = input("Last name: ")
    address = input("Address: ")
    city = input("City: ")
    state = input("State abbreviation (capitalized): ")
    zipcode = input("Zip code: ")
    print("Navigating to product page . . .")

    global productObj
    website = WebsiteObject(Sites.BESTBUY)
    for product in website.products:
        if product.name == productName:
            productObj = product
            break
    if productObj is None:
        print(f"product name not found in {Sites.BESTBUY} product list")

    # open site
    siteUrl = website.siteurl
    driver.get(siteUrl)

    # search for product
    searchBar = driver.find_element_by_id("gh-search-input")
    time.sleep(1)
    searchBar.send_keys(productObj.modelnumber)
    time.sleep(1)
    searchBar.send_keys(Keys.RETURN)

    # navigate to product page
    time.sleep(2)
    product = driver.find_element_by_partial_link_text(productObj.keyword)
    product.click()

    # try to add to cart
    while True:
        time.sleep(2)
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

