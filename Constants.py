from enum import Enum
from selenium import webdriver


class Sites(Enum):
    NEWEGG = "newegg"
    BESTBUY = "bestbuy"


userinfo = {}
PATH = "./chromedriver.exe"
driver = webdriver.Chrome(PATH)
