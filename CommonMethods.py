import glob
import Constants

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

