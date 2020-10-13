# Hatchet
## About
#### This is a Selenium bot designed with the long-term goal of being able to access product pages on various etailer sites and passively poll for stock availability, purchasing the desired product once it becomes available. In particular, this bot is meant to give easier to access to products during a period of stock scarcity, or a limited quantity launch.
## Prerequisites
#### -Must have chrome Version 86.*<br/>
#### -Must have Python 3.* installed<br/>
## Usage
### Set up information for purchasing
#### 1. Locate the InfoFilePath.txt file in the repository. You will notice that it by default contains 'C:\Users\\*\Documents\HatchetUserInfo.txt'. This indicates the path on your local machine to your C drive documents where you will have to create a user information text file, the format of which will be specified in the next step. You can change this path if you wish to have your user information file stored elsewhere, but an incorrect path will likely crash the program.<br/>
#### 2. Create a text file named HatchetUserInfo.txt in the directory that has been specified in InfoFilePath.txt. This file contains semi-sensitive user information for the purpose of filling out checkout forms on the website you are purchasing from. Its format as is follows:<br/>
email: person@website.com<br/>
phone: 1112223333<br/>
firstname: john<br/>
lastname: doe<br/>
address: 1 helloworld street<br/>
city: flavortown<br/>
state: CA<br/>
zipcode: 11111<br/>
#### * The file must be formatted the same as the example, including line breaks and spacing.
#### * More sensitive information will be prompted by the program at runtime.<br/>
### Run the program
#### For windows, locate and execute the Hatchet.bat file. For 
#### unix systems, locate and execute the Hatchet.sh file.
#### 1. Upon launch, the program will prompt the user for information pertinent to the checkout process, the desired site refresh rate, as well as the site of purchase and the url from which the user would like to purchase a product.<br/>
#### 2. It will then open google chrome and navigate to the site that the user has entered. Note that if the url does not belong to the same origin domain as the site of purchase, the program will not function properly.<br/>
#### 3. Finally, the program will passively refresh the product page at a rate corresponding to that inputted by the user, and will purchase the product if/when the 'Add to cart' button becomes active.<br/>


