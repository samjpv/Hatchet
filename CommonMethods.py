import glob

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import Constants

driver = Constants.driver


def setuserinfo():
    try:
        userinfopath = open("InfoFilePath.txt", "r").read()
        userinfofile = open(glob.glob(userinfopath)[0], "r").read()
    except Exception:
        print("There was a problem with your user information file. Check that you have the correct path to your info "
              "file in InfoFilePath.txt and check that your user info file is formatted according to readme "
              "specifications, then run the program again.")
        exit(-1)
    userinfoarray = userinfofile.split('\n')
    for field in userinfoarray:
        values = field.split(': ')
        fieldname = values[0]
        fieldvalue = values[1]
        Constants.userinfo[fieldname] = fieldvalue
    Constants.userinfo["ccn"] = input("User ccn: ")
    Constants.userinfo["cvv"] = input("User cvv: ")
    Constants.userinfo["ccexpirationmonth"] = input("User cc expiration month, e.g. 01: ")
    Constants.userinfo["ccexpirationyear"] = input("User cc expiration year, e.g. 2020: ")


def waitforbutton_byclass(buttonclass):
    timeout = 5
    try:
        element_present = EC.presence_of_element_located((By.CLASS_NAME, buttonclass))
        WebDriverWait(Constants.driver, timeout).until(element_present)
    except TimeoutException:
        print(f"Page html did not load after {timeout} seconds. . .")
    driver.find_element_by_class_name(buttonclass).click()


def waitforfield_byid(fieldid, fieldvalue):
    timeout = 5
    try:
        element_present = EC.presence_of_element_located((By.ID, fieldid))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print(f"Page html did not load after {timeout} seconds. . .")
    driver.find_element_by_id(fieldid).send_keys(fieldvalue)


def waitfordropdown_byname(dropdownname, dropdownvalue):
    timeout = 5
    try:
        element_present = EC.presence_of_element_located((By.NAME, dropdownname))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print(f"Page html did not load after {timeout} seconds. . .")
    Select(driver.find_element_by_name(dropdownname)).select_by_visible_text(
        dropdownvalue)
