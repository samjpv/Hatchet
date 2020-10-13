import Constants
import SiteMethods


def main():
    print("The following sites are available to Hatchet:\n")
    for site in Constants.Sites:
        print(site + '\n')
    site = input("Which site would you like to use?").lower()
    producturl = input("Please enter the URL of the product you would like to purchase:\n (must belong to inputted "
                       "site)\n")
    refreshrate = input("How often would you like to refresh the site in seconds?:\n")

    if site == Constants.Sites.NEWEGG:
        SiteMethods.newegg(producturl)
    elif site == Constants.Sites.BESTBUY:
        SiteMethods.bestbuy(producturl, refreshrate)


if __name__ == '__main__':
    main()
