# install selenium
# install chromedriver and copy executable to C:/Program Files (x86)
# login to site account

import logging
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


def tryaddtocart(refreshdelay):
    while True:
        driver.refresh()
        try:
            cartbutton = driver.find_element_by_xpath("//button[contains(text(), \"Add to cart \")]")
            cartbutton.click()
            break
        except NoSuchElementException:
            logging.info("No add to cart button")
            print("no add to cart")
        time.sleep(refreshdelay)
    logging.info("Add to cart button pressed")


PATH = "C:/Program Files (x86)/chromedriver.exe"
driver = webdriver.Chrome(PATH)

websites = {"newegg": "https://www.newegg.com"}
productNames = {"aorus master": "GIGABYTE AORUS GeForce RTX 3080", "gskill ram": ""}

# open site
siteUrl = websites["newegg"]
driver.get(siteUrl)

# check for popups
try:
    closePopup = driver.find_element_by_id("popup-close")
    closePopup.click()
except NoSuchElementException:
    print("no popup")

# search for product
searchBar = driver.find_element_by_id("SearchBox2020")
searchBar.send_keys("RTX 3080")
searchBar.send_keys(Keys.RETURN)

# navigate to product page
time.sleep(1)
productName = productNames["aorus master"]
driver.find_element_by_partial_link_text(f"{productName}").click()

# try to add to cart
tryaddtocart(30)
