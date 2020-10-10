# install selenium
# install chromedriver and copy it to C:/Program Files (x86)
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


PATH = "C:/Program Files (x86)/chromedriver.exe"
driver = webdriver.Chrome(PATH)

websites = {"newegg": "https://www.newegg.com/p/pl?d=rtx+3080"}
productNames = {"aorus master": 'GIGABYTE AORUS Geforce RTX 3080'}

siteUrl = websites["newegg"]

# open search bar and enter searchContents
driver.get(siteUrl)

# check for popups
time.sleep(5)
try:
    closePopup = driver.find_element_by_id("popup-close")
    closePopup.click()
except NoSuchElementException:
    print("no popup")
time.sleep(5)

# select the product
productName = productNames["aorus master"]
# product = driver.find_element_by_xpath(f'//a[contains(text(), \'{productName}\')]')
product = driver.find_element_by_xpath(f'a[@class=\'item-title\' and contains(text(), \"{productName}\")]')
product.click()






