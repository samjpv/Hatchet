import Constants
import SiteMethods


def main():
    print("The following sites are available to Hatchet:")
    for site in Constants.Sites:
        print(site.name)
    site = input("Which site would you like to use?:\n").lower()
    producturl = input("Please enter the URL of the product you would like to purchase:\n (must belong to inputted "
                       "site)\n")
    refreshrate = int(input("How often would you like to refresh the site in seconds?:\n"))
    if site == Constants.Sites.BESTBUY.value:
        SiteMethods.bestbuy(producturl, refreshrate)


if __name__ == '__main__':
    main()
