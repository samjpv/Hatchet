# install selenium
# install chromedriver and copy executable to C:/Program Files (x86)
import time
import Constants
import CommonMethods

driver = CommonMethods.driver


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
    CommonMethods.waitforbutton_byclass('btn-lg')
    CommonMethods.waitforbutton_byclass('js-cia-guest-button')

    # fill in payment info
    CommonMethods.waitforfield_byid("user.emailAddress", Constants.userinfo["email"])
    CommonMethods.waitforfield_byid("user.phone", Constants.userinfo["phone"])
    driver.find_element_by_class_name("btn-secondary").click()
    CommonMethods.waitforfield_byid("optimized-cc-card-number", Constants.userinfo["ccn"])
    CommonMethods.waitfordropdown_byname("expiration-year", Constants.userinfo["ccexpirationyear"])
    CommonMethods.waitfordropdown_byname("expiration-month", Constants.userinfo["ccexpirationmonth"])
    CommonMethods.waitforfield_byid("credit-card-cvv", Constants.userinfo["cvv"])
    CommonMethods.waitforfield_byid("payment.billingAddress.firstName", Constants.userinfo["firstname"])
    CommonMethods.waitforfield_byid("payment.billingAddress.lastName", Constants.userinfo["lastname"])
    driver.find_element_by_class_name("autocomplete__toggle").click()
    CommonMethods.waitforfield_byid("payment.billingAddress.street", Constants.userinfo["address"])
    CommonMethods.waitforfield_byid("payment.billingAddress.city", Constants.userinfo["city"])
    CommonMethods.waitfordropdown_byname("state", Constants.userinfo["state"])
    CommonMethods.waitforfield_byid("payment.billingAddress.zipcode", Constants.userinfo["zipcode"])
    driver.find_element_by_class_name("btn-lg").click()
