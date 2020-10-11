import time
from Constants import Sites
from WebsiteObject import WebsiteObject
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

PATH = "C:/Program Files (x86)/chromedriver.exe"
driver = webdriver.Chrome(PATH)


def main():
    bestbuynav("evga 2060")


if __name__ == '__main__':
    main()


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
    time.sleep(1)
    product = driver.find_element_by_partial_link_text(productObj.keyword)
    product.click()

    # try to add to cart
    while True:
        driver.refresh()
        try:
            time.sleep(1.5)
            cartbutton = driver.find_element_by_class_name("btn-lg")
            cartbutton.click()
            break
        except NoSuchElementException:
            print("no add to cart")

    # checkout
    time.sleep(1)
    driver.get("https://www.bestbuy.com/cart")
    # cardcontainer = driver.find_element_by_class_name("checkout-buttons__checkout")
    # cardcontainer.find_element_by_class("btn").click()
