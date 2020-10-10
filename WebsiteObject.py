from Product import Product
from Constants import Sites


class WebsiteObject:
    siteurl = ""
    products = []

    def __init__(self, sitename):
        if sitename == Sites.NEWEGG:
            print("name was newegg")
            self.siteurl = "https://newegg.com"
            self.products = [Product("aorus master", "GV-N3080AORUS M-10GD")]
