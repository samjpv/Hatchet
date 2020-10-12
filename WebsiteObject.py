from Product import Product
from Constants import Sites


class WebsiteObject:
    siteurl = ""
    products = []

    def __init__(self, sitename):
        if sitename == Sites.NEWEGG:
            self.siteurl = "https://newegg.com"
            self.siteurl = "https://newegg.com"
            self.products = [Product("aorus master", "GV-N3080AORUS M-10GD", "RTX 3080"),
                             Product("gskill ram", "F4-3600C16D-32GTZR", "RAM")]
        elif sitename == Sites.BESTBUY:
            self.siteurl = "https://bestbuy.com"
            self.products = [Product("aorus master", "GV-N3080AORUS M-10GD", "RTX 3080"),
                             Product("evga 2060", "06G-P4-2068-KB", "RTX 2060"),
                             Product("asus rog strix", "ROG-STRIX-RTX3080-O10G-GAMING", "RTX 3080"),
                             Product("evga ftw3", "10G-P5-3897-KR", "RTX 3080")]