# install selenium
# install chromedriver and copy executable to C:/Program Files (x86)
import time
import CommonMethods
from selenium.common.exceptions import NoSuchElementException

driver = CommonMethods.driver


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
